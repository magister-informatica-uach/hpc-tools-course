# Herramientas de computación de alto rendimiento para científicos de datos

Este repositorio tiene las actividades de curso del mismo nombre del Magíster en Informática de la Universidad Austral de Chile.


**Resumen**

Este curso introduce al estudiante a conceptos, técnicas y herramientas que le permitan mejorar el desempeño de sus programas y así resolver eficientemente problemas intensivos en datos o cómputo. En particular el estudiante aprenderá a identificar cuellos de botella en sus programas y a optimizarlos utilizando técnicas como vectorización, paralelismo y cómputo distribuido. El estudiante implementará sus rutinas tanto en arquitecturas CPU multi-core convencional como en infraestructura de alto rendimiento (supercomputador).

**Contenidos**


- Unidad 1: Interactuando con un supercomputador
    - Arquitecturas de cómputo y supercomputadores
    - Manejo de shell UNIX y lenguaje BASH
    - Acceso y transferencia de archivos a sistemas remotos con SSH
    - Gestión de tareas de cómputo con SLURM 
- Unidad 2: Diagnóstico y optimización de programas en Python
    - Librerías de alto rendimiento en Python
	- Perfilado y benchmark de programas
	- Optimización básica mediante vectorización y caching
	- Creación y control de múltiples procesos con joblib
- Unidad 3: Lenguajes compilados y cómputo en GPU 
	- Conectar librerías C/C++ con Python
	- Cómputo multi-hilo con OpenMP
	- Compilación JIT con JAX
	- Accediento a la GPU con librerías de alto nivel
- Unidad 4: Computación distribuida y en la nube
	- Introducción a la computación distribuida con la librería Ray
	- Distribución de cómputo en ambiente local
	- Distribución de cómputo en la nube utilizando máquinas virtuales
    - Distribución de cómputo en la nube utilizando Kubernetes

**Referencias**

1. [Eijkhout V., Introduction to High Performance Scientific Computing, 2016](http://faculty.salisbury.edu/~jtanderson/teaching/cosc420/files/hpc.pdf)
1. Gorelick M., Ozsvald I., High Performance Python, 2nd Edition, O’really 2020
1- Pumperla M., Oakes E., Liaw R., “Learning Ray”, O’Reilly, 2023, 
Randau, L. “A Beginner’s Guide to High–Performance Computing“ 
1. Curso [“Introduction to High Performance Computing”](https://epcced.github.io/hpc-intro/)




