# Actividades 6 de junio

## Resultados de aprendizaje

El estudiante es capaz de:

- Crear clusters de Ray en Google Cloud Engine
- Coordinar multiples procesos asíncronos en cluster Ray en la nube

## Actividad

Cree un ambiente de conda para utilizar los servicios de Google Cloud:

    conda create -n gce python=3.9 google-cloud-sdk google-api-python-client cryptography -c conda-forge

Luego instale ray:

    pip install ray[default]


Ahora cree un proyecto utilizando [la consola web de Google Cloud](https://console.cloud.google.com). Tenga en consideración la id del proyecto.

Los archivo `yaml` en este directorio tienen la configuración configuración para el cluster que lanzaremos en GCE. Vaya a la línea 42 del archivo de configuración (full) y cambie le valor `null` por la id de su proyecto en GCE. Otras líneas importantes son:

- 6: Número máximo de workers
- 18: Imagen docker que se utilizará
- 39-40-41: Tipo de servicio y región
- 56: Todo lo relacionado al nodo maestro (head)
- 86: Todo lo relacionado a los nodos trabajadores (workers)
- 173: Comandos a ejecutar en la creación de los nodos trabajadores, por ejemplo instalación de librerías

Ahora es necesario configurar sus credenciales de GCE mediante ADC (application default credentials) con:

    gcloud auth application-default login

Se levantará una pestaña de navegador donde debe verificar sus credenciales.

Luego active su proyecto para cargos con

    gcloud auth application-default set-quota-project la-id-del-proyecto

**Nota:** Si no lo ha hecho es necesario [activar la API de su proyecto](https://console.cloud.google.com/apis/api/iam.googleapis.com/). En particular es necesario activar la [API del Compute Engine](https://console.cloud.google.com/apis/library/compute.googleapis.com). Este paso puede tomar algunos minutos.

Inicie el cluster con 

    ray up -y minimal.yaml

Este proceso descargará las imágenes, lo cual puede demorar varios minutos.

Luego conéctese al cluster con:

    ray attach minimal.yaml

Los comandos que lancemos a continuación serán ejecutados en el nodo head. Revise el script de python en este directorio y luego ejecutelo con:

    python ray-cluster-hello-world.py

Observe el output impreso y finalmente detenga el cluster con:

    ray down -y minimal.yaml

## Referencias y links:

- https://cloud.google.com/docs/authentication/client-libraries#python
- https://docs.ray.io/en/latest/cluster/getting-started.html
- https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/k8s-cluster-setup.html
