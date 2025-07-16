#!/bin/bash

# Bucle For
for i in {1..5}; do
	echo "Número: $i"
done


# Bucle While
contador=1
while [ $contador -le 3 ]; do
	echo "Contador: $contador"
	((contador++))
done