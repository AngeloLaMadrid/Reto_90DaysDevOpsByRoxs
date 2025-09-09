#!/bin/bash

echo "🔵 Creando script generador de mensajes..."
cat > generar_mensajes.sh << 'EOF'
#!/bin/bash
touch mensajes.txt
contador=1
while true; do
  echo "Mensaje #$contador - $(date)" >> mensajes.txt
  echo "Mensaje #$contador escrito a las $(date)"
  contador=$((contador+1))
  sleep 5
done
EOF

chmod +x generar_mensajes.sh

echo "🔵 Creando Dockerfile..."
cat > Dockerfile << 'EOF'
FROM alpine:latest
RUN apk add --no-cache bash
WORKDIR /app
COPY generar_mensajes.sh /app/
RUN chmod +x /app/generar_mensajes.sh
CMD ["/bin/bash", "/app/generar_mensajes.sh"]
EOF

echo "🔵 Construyendo imagen Docker..."
docker build -t mensaje-periodico .

echo "🔵 Ejecutando contenedor..."
docker run -d --name contenedor-mensajes mensaje-periodico

echo "🔵 Esperando 15 segundos para que se generen algunos mensajes..."
sleep 15

echo "🔵 Contenido del archivo mensajes.txt dentro del contenedor:"
docker exec contenedor-mensajes cat /app/mensajes.txt

echo "🔵 Copiando archivo mensajes.txt al host..."
docker cp contenedor-mensajes:/app/mensajes.txt ./mensajes.txt

echo "🔵 Contenido del archivo mensajes.txt en el host:"
cat mensajes.txt

echo "🔵 IP del contenedor:"
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' contenedor-mensajes

echo "🔵 Nombre de la imagen:"
docker inspect -f '{{.Config.Image}}' contenedor-mensajes

echo "🔵 Procesos activos en el contenedor:"
docker top contenedor-mensajes

echo "🔵 Deteniendo y eliminando el contenedor..."
docker rm -f contenedor-mensajes

echo "✅ Proceso completado correctamente."