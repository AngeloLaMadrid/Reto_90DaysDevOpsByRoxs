#!/bin/bash

echo -e "$ESTADO"
#Configuración
SERVICIOS=("nginx" "mysql" "docker" "apache2")
ADMIN="testDev@gmail.com"

hay_inactivos=0

for SERVICIO in "${SERVICIOS[@]}"; do
    if systemctl is-active --quiet "$SERVICIO"; then
        printf "✅ %s está ACTIVO\n" "$SERVICIO"
    else
        printf "❌ %s está INACTIVO\n" "$SERVICIO"
        hay_inactivos=1
    fi
done | tee /tmp/estado_servicios.txt

if [ $hay_inactivos -eq 1 ]; then
    mail -s "⚠️ Alerta: Servicios Inactivos" "$ADMIN" < /tmp/estado_servicios.txt
fi