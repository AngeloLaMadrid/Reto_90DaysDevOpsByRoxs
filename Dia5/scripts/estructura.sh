#!/bin/bash
# Comentario
echo "Hola Mundo"

# Variable
Nombre="Julio"
echo "Hola $Nombre"

# Condicionales
if [ "$Nombre" == "Julio" ]; then
	echo "¡Sos vos!"
else
	echo "¿Y Vos Quién Sos?"
fi

# Bucle
for i in {1..3}; do
	echo "Iteracion $i"
done