from timeit import timeit
import numpy as np
import distancia_pares_2 as distancia_pares_cython


def distancia_pares_numpy(data):
    return np.sqrt(np.sum((data.reshape(-1, 1, 2) - data.reshape(1, -1, 2))**2, axis=-1))


if __name__ == "__main__":
    N = 1000
    repetitions = 10
    data = np.random.randn(N, 2)
    result_numpy = distancia_pares_numpy(data)
    time_numpy = timeit('distancia_pares_numpy(data)',
                        setup="from __main__ import distancia_pares_numpy, data",
                        number=repetitions)

    result_cython = distancia_pares_cython.distancia_pares(data)
    time_cython = timeit('distancia_pares_cython.distancia_pares(data)',
                         setup="from __main__ import distancia_pares_cython, data",
                         number=repetitions)
    print(f"Numpy vs Cython <=> allclose:{np.allclose(result_numpy, result_cython)} tnumpy:{time_numpy/repetitions:0.4f} tcython:{time_cython/repetitions:0.4f} SpeedUp:{time_numpy/time_cython:0.4f} (time in secs)")
