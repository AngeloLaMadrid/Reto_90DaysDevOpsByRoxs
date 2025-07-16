#!/bin/bash
echo -e "Hora\t\t\tMemoria\t\tDisco (root)\tCPU"
segundos="3600"
fin=$((SECONDS+segundos))
consecutivas=0

while [ $SECONDS -lt $fin ]; do
    TIEMPO=$(date "+%Y-%m-%d %H:%M:%S")
    MEMORIA=$(free -m | awk 'NR==2{printf "%.f%%\t\t", $3*100/$2 }')
    DISCO=$(df -h | awk '$NF=="/"{printf "%s\t\t", $5}')
    CPU=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{printf("%.f", 100 - $1)}')
    echo -e "$TIEMPO\t$MEMORIA$DISCO$CPU"

    if [ "$CPU" -gt 85 ]; then
        consecutivas=$((consecutivas+1))
        echo "$TIEMPO ALERTA: CPU al $CPU%" >> alertas_cpu.log
    else
        consecutivas=0
    fi

    if [ $consecutivas -ge 3 ]; then
        echo "Monitoreo detenido: CPU superó el 85% tres veces seguidas."
        break
    fi

    sleep 3
done
