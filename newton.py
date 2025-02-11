import numpy as np
from scipy.differentiate import derivative

def newton(func, x0, fprime=None, tol=1.48e-08, maxiter=50):
    '''Find a zero of a function using Newton's method.
    func: The function to find the root. This should represent a function of a
    single variable, but should act on a numpy array elementwise.
    x0: The initial guess for Newton's method. Can be an ndarray to try
    multiple guesses at once.
    fprime: Derivative of the given function. If None, use finite difference
    method from scipy to estimate the derivative.
    tol: Allowable error in the value of the root. Used to determine when to 
    stop iterating.
    maxiter: Maximum number of iterations to run.
    '''
    return x0 # Obviously, this implementation is somewhat incomplete.