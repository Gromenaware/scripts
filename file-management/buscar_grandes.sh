#!/bin/bash

# Directorio base desde donde buscar (puedes cambiarlo o usar el argumento del script)
DIRECTORIO=${1:-.}

# Encuentra archivos mayores a 1GB y muestra su tamaño ordenado
echo "Archivos mayores a 1GB en el directorio: $DIRECTORIO"
find "$DIRECTORIO" -type f -size +1G -exec du -h {} + | sort -hr
echo "Búsqueda completada."