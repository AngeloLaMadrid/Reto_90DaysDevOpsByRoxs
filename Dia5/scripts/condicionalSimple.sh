#!/bin/bash

read -p "¿Tenés sed? (si/no): "

if [ "$RESPUESTA" == "si" ]; then
	echo "Andá por un Cafecito"
else
	echo "Seguimos con DevOps 🚀"
fi