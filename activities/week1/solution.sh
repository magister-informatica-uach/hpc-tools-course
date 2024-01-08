#!/bin/bash
if [ $# -ne "1" ]; then
    echo "Se necesita sólo n argumento";
    exit;
fi
export CARPETA="Pablo"
ls -r data/ | wc -l
mkdir data/${CARPETA}
echo $1 > data/${CARPETA}/new_data
cp data/${CARPETA}/new_data data/new_data
for nombre in $(find data -type f);
do
    echo "Nombre: "$nombre;
    echo "Contenido:"
    cat $nombre
done;
cat data/new_data
rm data/new_data
rm -R data/${CARPETA}
