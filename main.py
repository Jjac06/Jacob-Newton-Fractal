from newton import newton
import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image

def test_cubic(x):
    return x**3 - 1

def test_cubic_prime(x):
    return 3*x**2

def test_quartic(x):
    return x**4 + (2*(x**3)) - x

def test_quartic_prime(x):
    return 4*x**3 + (6*x**2) - 1

def test_quintic(x):
    return x**5-1

def test_quintic_prime(x):
    return 5*x**4

def get_user_input():
    while True:
        try:
            n = int(input("how many terms do you want for your taylor polynomial: "))
            if n > 0:
                return n
            else:
                print("enter a positive integer.")
        except ValueError:
            print("i need a positive integer, nitwit. try again: ")

def taylor_sin(x, n=7):
    result = 0
    for k in range(n):
        coeff = (-1)**k / math.factorial(2*k + 1)
        result += coeff * x**(2*k + 1)
    return result

def taylor_sin_prime(x, n=7):
    result = 0
    for k in range(n):
        coeff = (-1)**k * (2*k + 1) / math.factorial(2*k + 1)
        result += coeff * x**(2*k)
    return result

def generate_roots_and_colors(n):
    roots = [k * np.pi for k in range(-n//2, n//2 + 1)]
    colors = [[int(np.random.uniform(0, 255)) for _ in range(3)] for _ in range(len(roots))]
    return roots, colors

def gen_complex_grid(xstart, xstop, nx, ystart, ystop, ny):
    xs = np.linspace(xstart, xstop, nx)
    ys = np.linspace(ystart, ystop, ny)
    return xs[:, None] + 1j*ys

def map_colors(zs, roots, colors):
    out_r = np.zeros_like(zs, dtype=int)
    out_g = np.zeros_like(zs, dtype=int)
    out_b = np.zeros_like(zs, dtype=int)
    for root, color in zip(roots, colors):
        mask = np.isclose(zs, root)
        #within 10^-8 by default
        out_r[mask]=color[0]
        out_g[mask]=color[1]
        out_b[mask]=color[2]
    return np.stack((out_r, out_g, out_b), axis=2)

def main():
    zs = gen_complex_grid(-1.5, 1.5, 1500, -1.5, 1.5, 1500)
    # cubic fractal
    ccoefficients = [1, 0, 0, -1]
    roots=np.roots(ccoefficients)
    newton_roots = newton(test_cubic, zs, fprime=test_cubic_prime)
    colors = [[255,0,0],[255,255,255],[0,0,255]]

    image_array = map_colors(newton_roots.T, roots, colors)
    plt.imshow(image_array)
    plt.show()

    plt.savefig("cubic_fractal.png")

    # quartic fractal
    quacoefficients = [1, 2, 0, -1, 0]
    roots=np.roots(quacoefficients)
    newton_roots = newton(test_quartic, zs, fprime=test_quartic_prime)
    colors = [[255,0,0],[0,255,0],[0,0,255],[128,128,0]]

    image_array = map_colors(newton_roots.T, roots, colors)
    plt.imshow(image_array)
    plt.show()

    plt.savefig("quartic_fractal.png")

    # quintic fractal
    quicoefficients = [1, 0, 0, 0, 0, -1]
    roots=np.roots(quicoefficients)
    newton_roots = newton(test_quintic, zs, fprime=test_quintic_prime)
    colors = [[230, 57, 70],[241, 250, 238],[168, 218, 220],[69, 123, 157],[29, 53, 87]]

    image_array = map_colors(newton_roots.T, roots, colors)
    plt.imshow(image_array)
    plt.show()

    plt.savefig("quintic_fractal.png")

    # sin fractal
    n_terms = get_user_input()
    print(f"using {n_terms} terms for the taylor polynomial of sin(x).")

    roots, colors = generate_roots_and_colors(10)
    zs = gen_complex_grid(-1, 1, 2000, -2, 2, 2000)
    
    newton_roots = newton(lambda x: taylor_sin(x, n_terms), zs, 
                           fprime=lambda x: taylor_sin_prime(x, n_terms), maxiter=300)

    image_array = map_colors(newton_roots.T, roots, colors)
    plt.imshow(image_array)
    plt.show()

    plt.savefig("sin_fractal.png")

if __name__ == '__main__':
    main()