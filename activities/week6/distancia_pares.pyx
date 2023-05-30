import cython
cimport numpy as npc
import numpy as np

from cython.parallel import prange

# Por conveniencia podemos definir el tipo de data y dist con 
ctypedef npc.float64_t TIPO_t
TIPO = np.float64

cdef extern from "math.h" nogil:
    TIPO_t sqrt(TIPO_t)

# Deshabilitamos las comprobaciones de Python:
@cython.boundscheck(False)
@cython.wraparound(False)
def distancia_pares_parallel(TIPO_t [:, ::1] data, int n_jobs=4):
    cdef int N = data.shape[0]
    cdef int M = data.shape[1]
    dist = np.zeros(shape=(N, N), dtype=TIPO)
    cdef TIPO_t [:, ::1] dist_view = dist
    cdef Py_ssize_t i, j, k
    for i in prange(N, num_threads=n_jobs, nogil=True, schedule='static', chunksize=100):
        for j in range(i+1, N):
            for k in range(M):
                dist_view[i, j] += (data[i, k] - data[j, k])**2
            dist_view[i, j] = sqrt(dist_view[i, j])
            dist_view[j, i] = dist_view[i, j]
    return dist


@cython.boundscheck(False)
@cython.wraparound(False)
def distancia_pares(TIPO_t [:, ::1] data):
    cdef int N = data.shape[0]
    cdef int M = data.shape[1]
    dist = np.zeros(shape=(N, N), dtype=TIPO)
    cdef TIPO_t [:, ::1] dist_view = dist
    cdef Py_ssize_t i, j, k
    for i in range(N):
        for j in range(i+1, N):
            for k in range(M):
                dist_view[i, j] += (data[i, k] - data[j, k])**2
            dist_view[i, j] = sqrt(dist_view[i, j])
            dist_view[j, i] = dist_view[i, j]
    return dist
