# Actividades 20 de junio

## Resultados de aprendizaje

El estudiante es capaz de:

- Crear clusters de Ray en Google Cloud Engine
- Coordinar multiples procesos asíncronos en cluster Ray en la nube

## Actividad formativa

Cree un ambiente de conda para utilizar los servicios de Google Cloud:

    conda create -n gce python=3.9 google-cloud-sdk google-api-python-client cryptography -c conda-forge

Luego instale ray:

    pip install ray[default]

Ahora cree un proyecto utilizando [la consola web de Google Cloud](https://console.cloud.google.com). Tome nota de la id del proyecto.

Los archivo `yaml` en este directorio tienen la configuración configuración para el cluster que lanzaremos en GCE. 

Ahora es necesario configurar sus credenciales de GCE mediante ADC (application default credentials) con:

    gcloud auth application-default login

Se levantará una pestaña de navegador donde debe verificar sus credenciales.

Luego active su proyecto para cargos con

    gcloud auth application-default set-quota-project la-id-del-proyecto

**Nota:** Si no lo ha hecho es necesario [activar la API de su proyecto](https://console.cloud.google.com/apis/api/iam.googleapis.com/). En particular es necesario activar la [API del Compute Engine](https://console.cloud.google.com/apis/library/compute.googleapis.com). Este paso puede tomar algunos minutos.

Revise el script de python en este directorio y luego ejecutelo con:

    python ray_cluster_hello_world.py

Lo anterior creará un cluster de ray local. A continuación veremos como realizar lo anterior con un cluster en la nube.

Primero edite el archivo de configuración `gce-minimal.yaml` con la id de su proyecto.

Ahora inicie el cluster con 

    ray up -y gce-minimal.yaml

Este proceso descargará las imágenes, lo cual puede demorar varios minutos la primera vez. Cuando el proceso termine diríjase a la consola web para observar las máquina virtual creada (inicialmente sólo la del nodo head).

Para enviarle la rutina al nodo head puede utiliza

    ray rsync_up gce-minimal.yaml ray_cluster_hello_world.py .

Luego lance el script con:

    ray exec gce-minimal.yaml 'python ray_cluster_hello_world.py'

Observe el output impreso. Puede obtener acceso al dashboard con

    ray dashboard gce-minimal.yaml

Y luego abrir su navegador en: http://127.0.0.1:8265

Si bien en este caso no es necesario, se pueden descargar archivos desde el nodo head con el comando:

    ray rsync_down gce-minimal.yaml ruta_nube .

Finalmente puede detener el cluster con:

    ray down -v -y gce-minimal.yaml

Nota: Verifique que las máquinas virtuales se hayan destruido correctamente en la consola de Google. Si siguen ahí, puede borrarlas manualmente o intentar ejecutar nuevamente el comando anterior.

Finalmente puede deslogear los servicios de gcloud con:

    gcloud auth application-default revoke

## Actividad sumativa

Repita el procedimiento anterior para lanzar en un cluster ray en la nube el script `example_ray_local.py` de la semana 7.


## Referencias y links:

- https://docs.ray.io/en/latest/cluster/vms/getting-started.html
- https://docs.ray.io/en/latest/cluster/vms/references/ray-cluster-cli.html#cluster-commands
- https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/k8s-cluster-setup.html

El archivo `gce-full.yaml` expone más opciones para configurar su cluster, las líneas más importantes son:

- 6: Número máximo de workers
- 18: Imagen docker que se utilizará
- 39-40-41: Tipo de servicio y región
- 42: Nombre del proyecto
- 56: Todo lo relacionado al nodo maestro (head)
- 86: Todo lo relacionado a los nodos trabajadores (workers)
- 173: Comandos a ejecutar en la creación de los nodos trabajadores, por ejemplo instalación de librerías


