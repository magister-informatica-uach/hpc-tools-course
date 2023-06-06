# Actividades 6 de junio

## Resultados de aprendizaje

El estudiante es capaz de:

- Entender la diferencia entre multiproceso y multihilo
- Coordinar multiples procesos en Python con joblib
- Coordinar multiples procesos asíncronos con Ray

## Antes de la actividad

Revisar la documentación de JobLib y Ray y los ejemplos de este carpeta.

Para joblib (si no lo tiene instalado)

    conda install joblib

Luego ejecute el ejemplo con:

    python example_joblib.py 10_000_000 16 4


Para ray

    pip install ray[default]


Para ejecutar un cluster ray local

    ray start --head --num-cpus=8

Donde el número de CPUs puede o no ser especificado. Por defecto Ray seteará el número máximo de nucleos disponible. Con el cluster corriendo ya puede ejecutar el ejemplo 

    python example_ray_local.py 10_000_000 16

Para detener el cluster

    ray stop



## Actividad:

