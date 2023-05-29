import sys
from functools import partial
from timeit import timeit
import numpy as np
from distancia_pares import distancia_pares as distancia_pares_seq
from distancia_pares import distancia_pares_parallel


def distancia_pares_numpy(data):
    return np.sqrt(np.sum((data.reshape(-1, 1, 2) - data.reshape(1, -1, 2))**2, axis=-1))


if __name__ == "__main__":
    N = 1000
    assert len(sys.argv) == 3, "Llamar como python benchmark.py N n_jobs, donde N es la cantidad de datos y n_jobs la cantidad núcleos paralelos"
    N, n_jobs = [int(arg) for arg in sys.argv[1:]]
    repetitions = 10
    data = np.random.randn(N, 2)
    profile = partial(timeit, globals=globals(), number=repetitions)
    # result_numpy = distancia_pares_numpy(data)
    # time_numpy = profile('distancia_pares_numpy(data)')
    result_cython = distancia_pares_seq(data)
    time_cython = profile('distancia_pares_seq(data)')
    result_cython_par = distancia_pares_parallel(data, n_jobs)
    time_cython_par = profile('distancia_pares_parallel(data, n_jobs)')
    print(f"Cython Seq vs Par <=> allclose:{np.allclose(result_cython, result_cython_par)} tnumpy:{time_cython/repetitions:0.4f} tcython:{time_cython_par/repetitions:0.4f} SpeedUp:{time_cython/time_cython_par:0.4f} (time in secs)")
