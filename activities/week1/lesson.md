# Trabajando con un ambiente UNIX remoto

## Resultados de aprendizaje

- Saber conectarse y transferir archivos a un computador remoto
- Desenvolverse en un ambiente remoto basado en UNIX
- Usar editores e IDEs para programar remotamente
- Lanzar tareas en supercomputador Patagon

## Actividad en clase

Clone este repositorio en su computador o al menos el contenido de la carpeta `activities/week1`

### SSH

- Configure su cliente de SSH para acceder a Patagon. La dirección de patagon es patagon.uach.cl y el puerto es 2237. Se recomienda guardar esta información en `.ssh/config`.
- Transfiera los  contenidos de esta carpeta a patagon utilizando el comando `rsync`. HINT: `rsync -ve 'ssh -p 2237 -i mi_llave' carpeta_local usuario_remoto@direccion:carpeta_remota/`. Nota: También puede utilizar `scp` en lugar de `rsync`.

### BASH

Escriba un script de BASH que reciba un argumento y que realice la siguiente secuencia de operaciones:

- Crear una variable de entorno llamada CARPETA cuyo contenido sea su nombre
- Contar e imprimir la cantidad de archivos de la carpeta `data`
- Crear un subdirectorio en `data` llamado usando como nombre el contenido de la variable de entorno
- Crear un archivo en el subdirectorio llamado `new_data` cuyo contenido sea el argumento del script.
- Copiar el archivo recién creado al directorio `data`
- Imprimir recursivamente los nombres y los contenidos de todos los archivos en `data`
- Eliminar el archivo `data/new_data`
- Eliminar el subdirectorio que creo dentro de `data`

Ejecute el script redirigiendo el output a un archivo `activity.log`. Luego transfiera el archivo a su computador con SCP. Finalmente envíe el archivo por discord a su profesor. 

Nota: Podría ser necesario darle permiso de ejecución al *script*. Utilice `chmod +x script`.

### Editores de texto e IDEs remotas

- Modifique el contenido de `data/x.dat` utilizando el editor `nano`
- Instale la extensión SSH remote en VScode en su computador local. Luego conectese a patagon y complete la implementación de `run.py` según indican los comentarios.

### Patagon y SLURM

- Configure la autenticación para poder descargar contenedores desde [NGC y DockerHub en Patagon](https://patagon.uach.cl/patagon/tutoriales/autentificacion-contenedores)
- Cree un contenedor llamado *arch* con la imagen `archlinux` de Docker Hub. Ingrese al contenedor como usuario root e instale python con `pacman -S python`. Luego salga del contenedor. Referencia: https://patagon.uach.cl/patagon/tutoriales/administracion-contenedores
- Implemente un *script* (job submission file) de SLURM que ejecute el script `run.py`. Utilice la partición `cpu` y el contenedor que acaba de crear. Referencia: https://patagon.uach.cl/patagon/tutoriales/how-to-launch-slurm-jobs
- Lance el trabajo y verifique el resultado. Envié el log de resultado por discord a su profesor.

