
# Uso: ./buscar_palabra.sh archivo palabra
ARCHIVO="$1"
PALABRA="$2"

if [ -z "$ARCHIVO" ] || [ -z "$PALABRA" ]; then
    echo "Uso: $0 <archivo> <palabra>"
    exit 1
fi

if grep -q "$PALABRA" "$ARCHIVO" 2>/dev/null; then
    echo "¡Encontrado!"
else
    echo "No encontrado."
fi
