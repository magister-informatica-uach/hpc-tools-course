# Actividades 18 de abril

## SSH

- Configurar su cliente de SSH para acceder a Patagon
- Transferir los datos de la carpeta `data` a patagon utilizando SCP

## BASH

Escriba un script de BASH que realice la siguiente secuencia de operaciones

- Cree una variable de entorno llamada ALUMNO cuyo contenido sea su nombre
- Imprima el contenido de la variable de entorno
- Cuente e imprima la cantidad de archivos de la carpeta `data`
- Cree un subdirectorio en `data` llamado `moredata`
- Cree un archivo en `data/moredata` llamado `new_data` con su nombre completo.
- Copie el archivo recién creado al directorio `data`
- Imprima recursivamente los contenidos de `data` y todos sus subdirectorios
- Imprima el contenido del archivo `new_data`
- Eliminar el archivo `data/new_data`
- Eliminar el subdirectorio `data/moredata`

Ejecute el script redirigiendo el output a un archivo `activity.log`. Luego transfiera el archivo a su computador con SCP. Finalmente envíe el archivo por discord a su profesor.


## Patagon y SLURM

- Crear una imagen docker con Python 3
- Crear un script (job submission file) de SLURM que ejecute el script `run.py`
- Lance el trabajo y verifique el resultado
