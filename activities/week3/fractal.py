import numpy as np
import sys
from timeit import timeit
from functools import partial

def make_fractal(N=500, maxiters=50, cr=-0.835, ci=-0.2321):
    image = np.zeros(shape=(N, 2*N))
    ZR, ZI = np.meshgrid(np.linspace(-2, 2, 2*N), 
                         np.linspace(-1, 1, N))
    for k in range(maxiters):
        ZI2 = ZI*ZI
        ZR2 = ZR*ZR
        mask = ZR2 + ZI2 <= 4.
        image[mask] += 1
        #image.at[mask].set(image[mask]+1)

        ZI = 2*ZR*ZI + ci
        ZR = ZR2 - ZI2 + cr
    return image


def print_fractal(fractal):
    from matplotlib import pyplot as plt
    fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
    ax.set_title("Set de Julia")
    ax.matshow(fractal, cmap=plt.cm.gray)
    plt.savefig("fractal.png")


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        raise ValueError("Debe llamar como python fractal.py N, donde N es un entero no negativo")
    N = int(sys.argv[1])
    print_fractal(make_fractal(N))
    profile = partial(timeit, globals=globals(), number=10)
    time_numpy = profile('make_fractal(N)')
    print(time_numpy)
