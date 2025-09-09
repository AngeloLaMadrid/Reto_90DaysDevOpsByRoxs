# Actividad 3 - Semana2

## Descripción
En esta actividad crearás y gestionarás un contenedor personalizado que escribe mensajes periódicos en un archivo y practicarás comandos de administración de Docker.

## Pasos realizados

### 1. Crear un contenedor personalizado que escribe mensajes cada 5 segundos

Se creó un archivo `generar_mensajes.sh` con el siguiente contenido:

```bash
#!/bin/bash
touch mensajes.txt
contador=1
while true; do
  echo "Mensaje #$contador - $(date)" >> mensajes.txt
  echo "Mensaje #$contador escrito a las $(date)"
  contador=$((contador+1))
  sleep 5
done
```

Se creó el siguiente `Dockerfile`:

```dockerfile
FROM alpine:latest
RUN apk add --no-cache bash
WORKDIR /app
COPY generar_mensajes.sh /app/
RUN chmod +x /app/generar_mensajes.sh
CMD ["/bin/bash", "/app/generar_mensajes.sh"]
```

Se construyó la imagen y se ejecutó el contenedor:

```bash
docker build -t mensaje-periodico .
docker run -d --name contenedor-mensajes mensaje-periodico
```

### 2. Copiar el archivo mensajes.txt desde el contenedor al host y verificar su contenido

```bash
docker cp contenedor-mensajes:/app/mensajes.txt ./mensajes.txt
cat mensajes.txt
```

### 3. Obtener la IP del contenedor y el nombre de la imagen utilizada

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' contenedor-mensajes
docker inspect -f '{{.Config.Image}}' contenedor-mensajes
```

### 4. Comprobar los procesos activos dentro del contenedor

```bash
docker top contenedor-mensajes
```

### 5. Detener y eliminar el contenedor de forma forzada

```bash
docker rm -f contenedor-mensajes
```

### 6. (Opcional) Script bash para automatizar todo

```bash
#!/bin/bash
# Script completo en reto1.bash
```

## Evidencias

- Se generó el archivo `mensajes.txt` con mensajes cada 5 segundos.
- Se copió y verificó el contenido en el host.
- Se obtuvo la IP y el nombre de la imagen del contenedor.
- Se verificó el proceso activo con `docker top`.
- El contenedor fue eliminado correctamente.

## Conclusión

Se logró automatizar la creación, monitoreo y eliminación de un contenedor Docker personalizado, cumpliendo todos los requisitos