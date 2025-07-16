#!/bin/bash

USUARIO="angelo"

DESTINO="/home/$USUARIO/backups"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

ARCHIVO="logs_backup_$TIMESTAMP.tar.gz"

# Crear carpeta en caso no exista
mkdir -p "$DESTINO"

# Comprimir /var/log
tar -czf "$DESTINO/$ARCHIVO" /var/log

# Eliminar backups si pasan más de 7 días
find "$DESTINO" -type f -name "logs_backup_*.tar.gz" -mtime +7 -exec rm {} \;

echo "Backup creado en el destino: $DESTINO/$ARCHIVO"
echo "Backups antiguos eliminados exitosamente."
