# Actividades 6 de junio

## Resultados de aprendizaje

El estudiante es capaz de:

- Crear clusters de Ray en Google Cloud Engine
- Coordinar multiples procesos asíncronos en cluster Ray en la nube

## Antes de la actividad

En su ambiente predilecto instale ray

    pip install ray[default]

y luego el cliente de GCE

    pip install google-api-python-client

## Actividad:

El archivo `gce.yaml` tiene la configuración para el cluster que lanzaremos en GCE.

En primer lugar cree un proyecto utilizando la consola web de GCE.

Luego vaya a la línea 42 del archivo de configuración y cambie le valor `null` por la id de su proyecto en GCE. 

Otras líneas importantes son:

- 6: Número máximo de workers
- 18: Imagen docker que se utilizará
- 39-40-41: Tipo de servicio y región
- 56: Todo lo relacionado al nodo maestro (head)
- 86: Todo lo relacionado a los nodos trabajadores (workers)
- 173: Comandos a ejecutar en la creación de los nodos trabajadores, por ejemplo instalación de librerías
:wq

## Referencias y links:

- Ray en la nube: https://docs.ray.io/en/latest/cluster/getting-started.html
