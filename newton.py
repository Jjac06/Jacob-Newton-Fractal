import numpy as np
from scipy.differentiate import derivative
from scipy.optimize import fsolve


def newton(func, x0, fprime=None, tol=1.48e-08, maxiter=50):
    x = x0
    for _ in range(maxiter):
        fx = func(x)
        notnan = ~np.isnan(fx)
        if np.all(np.abs(fx[notnan]) < tol):
            return x

        if fprime is not None:
            dfdx = fprime(x)
        else:
            dfdx = derivative(func, x,).df

        if np.all(dfdx == 0):
            raise ValueError("zero derivative")

        x = x - fx / dfdx
        
    return x