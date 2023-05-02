# Actividades 2 de mayo

## Resultados de aprendizaje

- Aprender conceptos básicos sobre perfilado (*profiling*) con foco en problemas *compute-bound*
- Aplicar herramientas para medir tiempo de cómputo de una rutina en Python
- Aplicar herramientas para medir tiempo de cómputo de una rutina en C


### Conceptos básicos

Revisar el siguiente material junto al profesor:

- https://phuijse.github.io/PythonBook/contents/hpc/intro.html
- https://phuijse.github.io/PythonBook/contents/hpc/profiling.html

En linux puede consultar las características de su CPU con

    cat /proc/cpuinfo

**Escriba en su reporte** las siguientes características de su CPU:

- `model name`
- `cpu cores`
- `cpu MHz`

Más cualquier otra que considere relevante.


### Perfilado de rutina en Python

Utilizaremos como ejemplo la rutina `fractal.py` que se encuentra en este directorio. Antes de ejecutar el script se recomenda instalar montar un ambiente de conda con

    conda create -n info335 -c conda-forge python=3.9 matplotlib ipympl numpy scipy  cython

Luego activar con:

    conda activate info335

Finalmente ejecutar con:

    python fractal.py 500

Lo anterior debería generar un archivo `fractal.png` que puede ser visualizado como una imagen.

Se puede medir el tiempo de cómputo de un fragmento de código Python de forma robusta con el módulo [`timeit`](https://docs.python.org/3/library/timeit.html):

    python -m timeit -r 10 -s 'from fractal import make_fractal' 'make_fractal(500)'

**Escriba en su reporte** el resultado del comando anterior.

Modifique el comando anterior para medir el tiempo de llamar la función `evaluate_z` con `zi=zr=0` y agregue el resultado en su informe.
Lo anterior también se puede lograr desde desde un script Python importando el módulo `timeit`. 

Modifique `fractal.py` comentando el llamada a `print_fractal`, en su lugar importe el módulo `timeit` para medir el tiempo de la función `make_fractal` e imprimir el tiempo mínimo y tiempo promedio. **Escriba en su reporte** el resultado de llamar a su rutina modificada con N=50, 500 y 5000.

Para perfilar una rutina más larga y/o compleja podemos utilizar el módulo nativo [`cProfile`](https://docs.python.org/3/library/profile.html). Por ejemplo

    python -m cProfile fractal.py 500 

Lo anterior imprime una tabla con el número de llamadas, tiempo de lllamada y tiempo total de cada método de la rutina. Se puede utilizar los argumentos `-s` para ordenar según alguna de las columnas y `-o` para guardar la tabla en un archivo.

Podemos hacer perfilado desde un script de Python con:

    import cProfile
    with cProfile.Profile() as pr:
        # Correr nuestra rutina aquí
        pr.print_stats()

Modifique `fractal.py` para hacer un perfilado de `make_fractal` con sus valores por defecto, luego **imprima en su reporte** los 10 primeros métodos de la lista, ordenandos según tiempo acumulado. 

También es posible perfilar línea a línea en lugar de método a método. Para realizar perfilado por línea en Python se puede utilizar la librería: [`line_profiler`](https://github.com/pyutils/line_profiler)

Instale la librería en su ambiente y haga un perfilado de las funciones `make_fractal` y `evaluate_z`. **Describa en su informe** cuales son las líneas del programa que involucran más cómputo.


### Perfilado de rutina en C


