# Actividad 9 de Mayo

## Resultados de aprendizaje

    - Comprender las limitaciones del lenguaje Python 
    - Aprender buenas prácticas de programación para acelerar rutinas en Python
    - Vectorizar rutinas matemáticas con la librería NumPy

## Conceptos básicos

Revisar el siguiente material junto al profesor:

- https://phuijse.github.io/PythonBook/contents/hpc/opti1.html

Instale la librería NumPy en su ambiente de conda con:

    conda install numpy

Luego activate su ambiente, ejecute el interprete de python y escriba

    import numpy as np 
    np.__version__
    np.show_config()

Para comprobar su versión y las librerías de bajo nivel contra las que está compilada su instalación de NumPy.

- [¿Qué es BLAS y LAPACK?](https://superfastpython.com/what-is-blas-and-lapack-in-numpy/)
- Configurando la [cantidad de núcleos en NumPy](https://superfastpython.com/numpy-number-blas-threads/)
- Es posible [cambiar el backend de bajo nivel](https://conda-forge.org/docs/maintainer/knowledge_base.html#switching-blas-implementation)

## Actividad: Vectorizar el fractal de Julia

Escriba una versión vectorizada de la rutina que genera el fractal de Julia utilizada en la semana 2. 

- Considere el espacio de números complejos (z) como una ndarray de dos dimensiones. 
- Implemente la recursión del conjunto de julia con funciones de NumPy para actualizar todos los elementos de z al mismo. 
- Obtenga una gráfica de speed-up entre su nueva solución y la solución original. 
- Envíe su rutina vectorizada y el gráfico de speed-up por discord.
- Proyecte con los datos de tiempo de su nueva solución, con que valor de N se calcula un fractal durante 30 minutos. Luego genere dicho fractal y comparta su imagen en el canal de discord del curso.


## Otras referencias

- https://pythonspeed.com/articles/vectorization-python/
- https://lhoupert.fr/test-jbook/04-code-vectorization.html
