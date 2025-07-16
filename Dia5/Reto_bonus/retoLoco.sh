
#!/bin/bash

echo "¿Cúal es tú nombre? 🤔"
read nombre

echo "¿Cuántos años tienes? 🎂"
read edad

echo "¿Cuál es tu color favorito? 🎨"
read color

echo
echo "¡Hola, $nombre! 👋"

if [ "$edad" -lt 18 ]; then
  echo "Aún joven y lleno de energía 💥"
else
  echo "La experiencia es tu superpoder 🦸‍♂️"
fi

if [[ "$color" =~ [Aa]zul ]]; then
  echo "¡El azul es el color del cielo y el mar! 🌊"
elif [[ "$color" =~ [Rr]ojo ]]; then
  echo "¡El rojo es pasión y fuerza! 🔥"
elif [[ "$color" =~ [Vv]erde ]]; then
  echo "¡El verde es vida y naturaleza! 🌱"
else
  echo "¡$color es un color único! 🌈"
fi
