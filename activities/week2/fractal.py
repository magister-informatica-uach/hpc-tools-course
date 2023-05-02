import sys


def evaluate_z(zi, zr, maxiters=50, cr=-0.835, ci=-0.2321):
    nit = 0
    zi2 = zi**2
    zr2 = zr**2
    while zi2 + zr2 <= 4. and nit < maxiters:
        zi = 2*zr*zi + ci
        zr = zr2 - zi2 + cr
        zr2 = zr**2
        zi2 = zi**2
        nit += 1
    return nit


def make_fractal(N=500, maxiters=50):
    image = []
    for i in range(N):
        row = []
        for j in range(2*N):
            zi = -1.0 + i*2/N
            zr = -2.0 + j*2/N
            row.append(evaluate_z(zi, zr, maxiters))
        image.append(row)
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
