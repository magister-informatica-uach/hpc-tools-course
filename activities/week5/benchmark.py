import sys
from timeit import timeit
import numpy as np
import jax
from jax import numpy as jnp


def distancia_pares_np(data):
    return np.sqrt(np.sum((data.reshape(-1, 1, 2) - data.reshape(1, -1, 2))**2, axis=-1))


def distancia_pares_jnp(data):
    return jnp.sqrt(jnp.sum((data.reshape(-1, 1, 2) - data.reshape(1, -1, 2))**2, axis=-1))


if __name__ == "__main__":
    assert len(sys.argv) == 3, "Llamar como python benchmark.py N prec dev, donde N es un entero, prec es 32 (float) o 64 (double) y dev es cpu o gpu"
    print(f" Devices: {jax.devices()}")
    N, prec = [int(arg) for arg in sys.argv[1:]]
    repetitions = 10 
    data = np.random.randn(N, 2)
    if prec == 64:
        jax.config.update("jax_enable_x64", True)
    else:
        data = np.random.randn(N, 2).astype('float32')
    data_jax = jnp.array(data)
    print(f"What type is data_jax: {data_jax.dtype}")
    print(f"Where is data_jax: {data_jax.device_buffer.device()}")
    result_np = distancia_pares_np(data)
    # distancia_pares_jnp = jax.jit(distancia_pares_jnp)
    result_jnp = distancia_pares_jnp(data_jax)

    time_np = timeit('distancia_pares_np(data)',
                     setup="from __main__ import distancia_pares_np, data",
                     number=repetitions)


    time_jnp = timeit('distancia_pares_jnp(data_jax).block_until_ready()',
                      setup="from __main__ import distancia_pares_jnp, data_jax",
                      number=repetitions)


    print(f"Numpy vs JAX <=> allclose:{np.allclose(result_np, result_jnp)} tnumpy:{time_np/repetitions:0.4f} tjax:{time_jnp/repetitions:0.4f} SpeedUp:{time_np/time_jnp:0.4f} (time in secs)")

