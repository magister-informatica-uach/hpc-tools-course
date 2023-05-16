# Actividades 16 de mayo

## Resultados de aprendizaje

El estudiante es capaz de:
- Explicar que es y para qué sirve C-Extensions for Python (cython) 
- Escribir y compilar rutinas en cython que procesan ndarrays de NumPy
- Acceder a funciones de lenguaje C desde Python

## Antes de la actividad

Revisar el siguiente material junto al profesor:

- https://phuijse.github.io/PythonBook/contents/hpc/cython.html

y los ejemplos de este carpeta.


Instale en su ambiente la librería cython y los compiladores de C o cree un ambiente nuevo:

    conda create -n cython2 python=3.9 numpy gcc_linux-64 cython

Luego active su ambiente.

Puede transpilar de cython a c con:

    cython -3 mi_codigo.pyx

Opcionalmente puede usar el flag `-a` para generar un reporte html con la cantidad de llamados a la API de Python. 

Luego compile el código generado con:

    $CONDA_PREFIX/bin/x86_64-conda-linux-gnu-gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -o my_lib.so mi_codigo.c -I $CONDA_PREFIX/include/python3.9/


Lo anterior crea una librería dinámica que puede llamarse desde Python como:

    import my_lib

o 

    from my_lab import mi_funcion

Opcionalmente puede hacer los pasos de transpilación y compilación al mismo tiempo con el comando `cithonize`.



## Actividad:

Utilizando como base la implementación en lenguaje Python ingenua del fractal de Julia (semana 2) implemente una versión cythonizada con las consideraciones vistas en clase. Compare los resultados con la versión vectorizada de la semana 3. Haga una curva de speed up entre la implementación en cython y la vectorizada con numpy en función de `N`. 
