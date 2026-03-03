#!/bin/bash

# Comprovem que s'han passat exactament 2 paràmetres
if [ "$#" -ne 2 ]; then
    echo "❌ Error: Falten paràmetres."
    echo "💡 Ús correcte: $0 <carpeta_origen> <carpeta_desti>"
    exit 1
fi

# Assignem els paràmetres a les variables
origen="$1"
desti="$2"

# Creem la carpeta destí si no existeix
mkdir -p "$desti"

# Executem la cerca i còpia
echo "Cercant i copiant els arxius .epub..."
find "$origen" -type f -name "*.epub" -exec cp {} "$desti" \;

echo "✅ Procés completat! Tots els epubs estan a $desti"