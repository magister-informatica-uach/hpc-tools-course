# Actividades 30 de mayo

## Resultados de aprendizaje

El estudiante es capaz de:

- Entender que es el GIL en Python
- Paralelizar una rútina con cython y OpenMP
- Comparar los distintos schedulers para paralelizar de OpenMP

## Antes de la actividad

Revisar el siguiente material junto al profesor:

- https://phuijse.github.io/PythonBook/contents/hpc/parallel.html

y los ejemplos de este carpeta.

Utilice el ambiente de conda con cython creado en la semana 4. Puede compilar el ejemplo con

    make

Utilice `benchmark.py` para comparar el tiempo de la rutina en Cython con y sin OpenMP. Modifique la linea 23 de `distancia_pares.pyx` (for paralelo) para probar distintos `scheduler` y `chunksize`. Refiérase a la documentación para entender las diferencias entre los mecanismos de scheduling disponibles.



## Actividad:

Utilizando como base la implementación en Cython del fractal de Julia (semana 4) implemente una versión paralela con openmp según las consideraciones vistas en clase. Haga una curva de speed up entre la implementación en cython original y paralela en función de `N` y el número de nucleos (considere 2, 4 y 8). Utilice patagon en la cola de CPU. Realice un análisis de speed-up preliminar para para decidir cual scheduler utilizar. 
