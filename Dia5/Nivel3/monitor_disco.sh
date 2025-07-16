#!/bin/bash
ADMIN="admin@ejemplo.com"
LOG="monitor_disco.log"
FECHA=$(date "+%Y-%m-%d %H:%M:%S")
USO_RAIZ=$(df / | grep / | awk '{print $5}' | sed 's/%//g')
TAMANO_HOME=$(du -sh /home | awk '{print $1}' | sed 's/G//g')

if [ "$USO_RAIZ" -ge 90 ]; then
    MENSAJE="${FECHA} ¡Alerta: Partición / al ${USO_RAIZ}%!"
    echo "$MENSAJE" | mail -s "Alerta Partición /" $ADMIN
    echo "$MENSAJE" >> "$LOG"
fi

if (( $(echo "$TAMANO_HOME > 2" | bc -l) )); then
    MENSAJE="${FECHA} ¡Alerta: /home ocupa ${TAMANO_HOME}GB!"
    echo "$MENSAJE" | mail -s "Alerta Directorio /home" $ADMIN
    echo "$MENSAJE" >> "$LOG"
fi