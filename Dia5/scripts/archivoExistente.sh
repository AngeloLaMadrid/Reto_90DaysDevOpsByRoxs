#!/bin/bash

#ARCHIVO="config.txt"

read ARCHIVO

if [ -f "$ARCHIVO" ]; then
	echo "El archivo $ARCHIVO existe"
else
	echo "No encontré el archivo $ARCHIVO"
fi