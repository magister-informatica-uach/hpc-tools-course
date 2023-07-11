# Actividades 11 de julio

## Resultados de aprendizaje

El estudiante es capaz de:

- Ejecutar programas distribuidos con Ray en un cluster de kubernetes alojado en GKE
- Administrar clusters dinámicos con el operador KubeRay

## Actividad en clase

En tu consola de Google Cloud habilita la API de Kubernetes: *Kubernetes Engine*. Luego crea un cluster con las opciones por defecto tomando nota del `CLUSTER_NAME` (e.g. autopilot-cluster) y la `COMPUTE_REGION` (e.g. us-central1).

Se utilizará el mismo ambiente de la actividad anterior con GCE. Instalamos la herramienta de configuración kubectl con:

    conda activate gce
    gcloud components install kubectl

El componente kubectl se instalará en una ruta del estilo `~/.conda/envs/gce/share/google-cloud-sdk-435.0.1-0/bin`. Se recomienda añadirla a su variable de entorno `PATH` para poder llamarla directamente. Verifique que la variable de entorno funciona ejecutando:

    kubectl version --short

La instalación de kubectl debería instalar el complemento de autenticación de GKE, compruebe con:

    gke-gcloud-auth-plugin --version

Ahora es momento de autenticar en sus servicios de Google Cloud, ejecutando:

    gcloud auth login

Lo anterior levantará una ventana de navegador donde debe seleccionar su cuenta. Ahora configure su proyecto con:

    gcloud config set project ID_PROYECTO

Puede obtener la ID de sus proyectos desde la consola de Google Cloud o ejecutando:

    gcloud projects list

Ahora configure las credenciales de su cluster con:

    gcloud container clusters get-credentials CLUSTER_NAME --region=COMPUTE_REGION

Si lo anterior funcionó correctamente debería poder ver una lista de servicios de kubernetes al ejecutar el siguiente comando:

    kubectl get namespaces

También se puede verificar la configuración del kubernetes con:

    kubectl config view

Cabe destacar que se puede tener más de un cluster. Para verificar cual es el cluster que está actualmente configurado utilice:

    kubectl config current-context

A continuación levantaremos el operador de Kubernetes provisto por Ray: KubeRay. Un operador es una extensión de software para Kubernetes que le permite usar recursos personalizados. En este caso particular KubeRay ofrece tres recursos: RayCluster, RayJobs y RayService.

Utilice helm para instalar KubeRay en su cluster:

    kubectl create -k "github.com/ray-project/kuberay/ray-operator/config/default?ref=v0.5.0&timeout=90s"

Debería poder ver el operador activo con:

    kubectl get pods -n ray-system

Un *pod* es la unidad mínima que puede ser creada, levantada y administrada por Kubernetes. Un pod es típicamente un principal contenedor y un conjunto de contenedores. Un pod es entonces un recurso más abstracto que una máquina virtual como las que ocupamos en la sesión anterior.

Ahora levante un cluster de ray con utilizando el archivo de configuración de ejemplo en esta carpeta. Revise el archivo `yaml` y luego ejecute con:

    kubectl create -f ray-cluster.complete.yaml

y verifique con: 

    kubectl get rayclusters
    kubectl get pods

Lo anterior debería mostrar el nodo head y un worker.

**Importante:** La columna STATUS muestra que está ocurriendo con los pods en el momento. Antes de seguir espere hasta que todos estén en STATUS=Running

Puede verificar los servicios que están ejecutándose con:

    kubectl get services

En particular debería aparecer un servicio con un nombre similar a `raycluster-complete-head-svc` con el puerto 8265 abierto. Para acceder al dashboard de ray desde nuestro computador ejecute el siguiente mapeo de puertos en una terminal distinta:

    kubectl port-forward --address 0.0.0.0 service/raycluster-complete-head-svc 8265:8265

Opcionalmente puede utilizar el mismo terminal agregando `2>&1 >/dev/null &` al comando para silenciar el *output* y luego enviarlo al *background* (Ctrl+z + `bg`).

Si lo anterior funcionó correctamente debería poder acceder al dashboard visitando: http://127.0.0.1:8265

Ahora ya está listo para enviar trabajos con Ray. Envíe un trabajo de ejemplo utilizando el comando `ray job submit`:

    ray job submit --address http://localhost:8265 -- python -c "import ray; ray.init(); print(ray.cluster_resources())"

También se puede evitar proveer la dirección declarando la variable de ambiente

    export RAY_ADRESS="http://127.0.0.1:8265"

Visualice el resultado en el dashboard.

Más en general nos interesará lanzar un script de Python. La semana pasada vimos como transferir archivos al nodo head. Otra manera simple es especificar un directorio de trabajo al hacer el subir el trabajo (job), por ejemplo:

    ray job submit --working-dir . -- python example_script.py

donde el contenido del directorio actual se enviará al nodo head automáticamente.

Para eliminar su RayCluster programaticamente:

    kubectl delete raycluster --all
    kubectl get pods

Espere a que los pods hayan sido eliminados antes de borrar el operador:

    kubectl delete -k "github.com/ray-project/kuberay/ray-operator/config/default"
    kubectl get pods -n ray-system

## Trabajo personal

Repita el procedimiento anterior para lanzar en un cluster ray en la nube el script `example_ray_local.py` de la semana 7.

## Referencias y links:

- [Configuración de acceso a GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)
- [Esquema de cobro de GKE](https://cloud.google.com/kubernetes-engine/pricing?hl=es)
- [Documentación de KubeRay](https://ray-project.github.io/kuberay/)
- [Autoescalamiento en KubeRay](https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/configuring-autoscaling.html)
- [Documentación de Ray Jobs](https://docs.ray.io/en/latest/cluster/running-applications/job-submission/quickstart.html)
- [Contenedores vs Máquinas virtuales](https://www.atlassian.com/microservices/cloud-computing/containers-vs-vms) y [¿Por qué pods y no sólo contenedores?](https://www.youtube.com/watch?v=5cNrTU6o3Fw)
- Ejemplo de servicio de LLM con GKE y Ray AIR: https://github.com/richardsliu/ray-on-gke


