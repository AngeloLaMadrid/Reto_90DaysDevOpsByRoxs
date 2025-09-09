#!/bin/bash
touch mensajes.txt
contador=1
while true; do
  echo "Mensaje #$contador - $(date)" >> mensajes.txt
  echo "Mensaje #$contador escrito a las $(date)"
  contador=$((contador+1))
  sleep 5
done
