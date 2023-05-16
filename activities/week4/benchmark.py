from timeit import timeit
import numpy as np
import distancia_pares_0


def distancia_pares_numpy(data):
    return np.sqrt(np.sum((data.reshape(-1, 1, 2) - data.reshape(1, -1, 2))**2, axis=-1))


if __name__ == "__main__":
    N = 1000
    data = np.random.randn(N, 2)
    result_numpy = distancia_pares_numpy(data)
    time_numpy = timeit('distancia_pares_numpy(data)', setup="from __main__ import distancia_pares_numpy, data", number=3)

    result_cython = distancia_pares_0.distancia_pares(data)
    time_cython = timeit('distancia_pares_0.distancia_pares(data)', setup="import distancia_pares_0; from __main__ import data", number=3)
    print(f"test cython 0: {np.allclose(result_numpy, result_cython)} tref:{time_numpy:0.4f} tnew:{time_cython:0.4f} SU:{time_numpy/time_cython:0.4f}")
