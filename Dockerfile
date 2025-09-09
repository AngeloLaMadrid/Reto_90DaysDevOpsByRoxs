FROM alpine:latest
RUN apk add --no-cache bash
WORKDIR /app
COPY generar_mensajes.sh /app/
RUN chmod +x /app/generar_mensajes.sh
CMD ["/bin/bash", "/app/generar_mensajes.sh"]
