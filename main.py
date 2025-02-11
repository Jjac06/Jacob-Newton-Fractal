from newton import newton
import numpy as np
import matplotlib.pyplot as plt

def test_quad(x):
    return x**2 - 1

def test_quad_prime(x):
    return 2*x

def main():
    xs = np.linspace(-2, 2, 101)
    ys = test_quad(xs)
    roots = newton(test_quad, xs, fprime=test_quad_prime)

    plt.plot(xs, ys, label="Test Quadratic")
    plt.plot(xs, roots, label="Root found with Newton's method")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()