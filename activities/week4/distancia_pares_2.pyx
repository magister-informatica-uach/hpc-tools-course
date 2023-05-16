import numpy as np

cdef extern from "math.h":
    double sqrt(double)

def distancia_pares(double [:, ::1] data):
    # Definimos el tipo de N, D, dist y data
    cdef int N = data.shape[0]
    cdef int D = data.shape[1]
    dist = np.zeros(shape=(N, N), dtype=np.double)
    cdef double [:, ::1] dist_view = dist
    # También definimos los índices, se puede usar int o Py_ssize_t 
    cdef Py_ssize_t i, j, k
    for i in range(N):
        for j in range(i+1, N):
            for k in range(D):
                dist_view[i, j] += (data[i, k] - data[j, k])**2
            dist_view[i, j] = sqrt(dist_view[i, j])
            dist_view[j, i] = dist_view[i, j]
    return dist
