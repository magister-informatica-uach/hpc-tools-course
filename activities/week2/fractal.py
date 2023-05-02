import sys


def check_divergence(zi2, zr2):
    return zi2 + zr2 > 4.


def evaluate_z(zi, zr, maxiters=50, cr=-0.835, ci=-0.2321):
    nit = 0
    zi2 = zi**2
    zr2 = zr**2

    for nit in range(maxiters):
        if check_divergence(zi2, zr2):
            break
        zi = 2*zr*zi + ci
        zr = zr2 - zi2 + cr
        try:
            zr2 = zr**2
            zi2 = zi**2
        except OverflowError:
            break
    return nit


def create_coordinates(i, j, N, maxx=2., minx=-1., maxy=2., miny=-2.):
    return minx + i*maxx/N, miny + j*maxy/N


def make_fractal(N=500, maxiters=50):
    image = []
    for i in range(N):
        row = []
        for j in range(2*N):
            zi, zr = create_coordinates(i, j, N)
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
