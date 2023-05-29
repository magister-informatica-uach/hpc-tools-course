all:
	cython -3 distancia_pares.pyx
	${CONDA_PREFIX}/bin/x86_64-conda-linux-gnu-gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -o distancia_pares.so distancia_pares.c -I ${CONDA_PREFIX}/include/python3.9/ -I ${CONDA_PREFIX}/lib/python3.9/site-packages/numpy/core/include

clean:
	rm *.so
