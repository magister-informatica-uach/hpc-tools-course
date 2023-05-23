# Actividades 23 de mayo

## Resultados de aprendizaje

El estudiante es capaz de:

- Entender la librería JAX y sus transformaciones 
- Escribir rutinas en JAX que procesan ndarrays
- Procesar con JAX tanto CPU como en GPU

## Antes de la actividad

Revisar el siguiente material junto al profesor:

- https://phuijse.github.io/tutorial_jax/README.html

y los ejemplos de este carpeta.

Para trabajar con JAX en CPU en su computador local, prepare el siguiente ambiente:

    conda create -n jax python=3.10 pip
    conda activate jax
    pip install --upgrade "jax[cpu]"

Para trabajar con JAX en GPU utilizaremos Patagon. Prepare un contenedor con:

    srun -p cpu -v --container-name=jax --container-image=nvcr.io/nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04 --container-remap-root --pty bash

Una vez dentro del  contenedor actualice los repos e instale python3

    apt update
    apt install python3 python3-pip
    exit

Vuelva a entrar en su contenedor pero como usuario regular 

    srun -p cpu -v --container-name=jax --pty bash

Finalmente instale JAX con:

    pip install --timeout 60 --upgrade "jax[cuda12_local]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html


## Actividad:

Utilizando como base la implementación en lenguaje Python vectorizada (numpy) fractal de Julia (semana 3) implemente una versión en JAX con las transformaciones vistas en clase. Compare los resultados con la versión vectorizada en numpy. Haga una curva de speed up entre la implementación en numpy, JAX en CPU, JAX con JIT en CPU, JAX en GPU y JAX con JIT en GPU en función de `N`. 
