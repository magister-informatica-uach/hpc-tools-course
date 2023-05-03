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

Utilizaremos como ejemplo la rutina `fractal.py` que se encuentra en este directorio. Referencia: https://en.wikipedia.org/wiki/Julia_set

Antes de ejecutar el script se recomienda instalar montar un ambiente de conda con:

    conda create -n info335 -c conda-forge python=3.9 pip matplotlib ipympl numpy scipy cython gprof2dot graphviz

Luego activar con:

    conda activate info335

Finalmente ejecutar con:

    python fractal.py 500

Lo anterior debería generar un archivo `fractal.png` que puede ser visualizado como una imagen.

Se puede medir el tiempo de cómputo de un fragmento de código Python de forma robusta con el módulo [`timeit`](https://docs.python.org/3/library/timeit.html):

    python -m timeit -r 10 -s 'from fractal import make_fractal' 'make_fractal(500)'

**Escriba en su reporte** el resultado del comando anterior. Modifique el comando anterior para medir el tiempo de llamar la función `evaluate_z` con `zi=zr=0` y agregue el resultado en su informe.

Lo anterior también se puede realizar desde desde un script de Python importando el módulo `timeit`: https://docs.python.org/3/library/timeit.html 

Escriba un script de Python llamado `fractal_timeit.py` que importe el módulo `timeit` para medir el tiempo de la función `make_fractal` de `fractal.py`. El script debe imprimir el tiempo mínimo y tiempo promedio. **Escriba en su reporte** el resultado de perfilar `make_fractal` con N=10, 100 y 1000.

Para perfilar una rutina más larga y/o compleja podemos utilizar el módulo nativo [`cProfile`](https://docs.python.org/3/library/profile.html). Por ejemplo mediante la interfaz de línea de comando:

    python -m cProfile fractal.py 500 

Lo anterior imprime una tabla con el número de llamadas, tiempo por llamada y tiempo total de cada método de la rutina. Se puede utilizar los argumentos `-s` para ordenar según alguna de las columnas y `-o` para guardar la tabla en un archivo.

También se puede hacer perfilado desde con script de Python, por ejemplo:

    import cProfile
    with cProfile.Profile() as pr:
        # Ejecutar aquí la rutina que deseamos perfilar
        pr.dump_stats("output.pstats") 
        # pr.print_stats()

Escriba un script de Python llamado `fractal_profiler.py` que importe `cProfile` para hacer un perfilado de la función `make_fractal` con sus valores por defecto, escriba el resultado en disco con `dump_stats`  y visualize una gráfica de su perfilado con:

    gprof2dot --colour-nodes-by-selftime -f pstats output.pstats | dot -Tpng -o output.png

Repita para la función `evaluate_z`. Documentación de `gprof2dot`: https://github.com/jrfonseca/gprof2dot

Trazado (*tracing*) de un programa con herramientas externas: https://functiontrace.com/. 

Instalación:

- Con su ambiente activado, instalar cliente con: `pip install functiontrace`
- Instalar `rustup` en su sistema operativo. Ver: https://www.rust-lang.org/tools/install
- Instalar el servidor con: `cargo install functiontrace-server`
- Agregar `.cargo/bin` a su variable `PATH`

Modifique `fractal.py` tal que  `main` sólo haga un llamado a `make_fractal(N)`. Luego:

- Ejecutar con `functiontrace fractal.py 500`
- Utilizar la UI de firefox para visualizar su trasa: https://profiler.firefox.com/ con la opción "cargar un perfil desde un archivo"

También es posible perfilar línea a línea en lugar de método a método. Para realizar perfilado por línea en Python se puede utilizar la librería: [`line_profiler`](https://github.com/pyutils/line_profiler). Instale la librería con `pip` en su ambiente de conda. Luego realice un perfilado de las funciones `make_fractal` y `evaluate_z`  y **describa en su informe** cuales son las líneas del programa que involucran más cómputo.

- Decore las funciones que desea perfilar con `@profile`
- Ejecute el comando `kernprof -l ...` según lo indicado en la documentación
- Obtenga la tabla de tiempos por línea con `python -m line_profiler ...`


### Perfilado de rutina en C

Próxima semana


