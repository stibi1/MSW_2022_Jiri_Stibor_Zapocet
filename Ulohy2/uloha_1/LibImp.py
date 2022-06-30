from sympy import *
import scipy.integrate as integrate
import numpy as np
from math import factorial
from time import process_time

FinalString = ""
# derivation

def DerivSym(func, var, val):
    var = symbols("x")
    deriv = diff(func, var)
    return (deriv.subs(x, val)).doit()


start = process_time()
x = symbols('x')
func = (6 * x ** 3) * (4 + 2 * x ** -2)
funRes = DerivSym(func, x, 7)

FullStop = process_time()


FinalString = FinalString + "| Sympy Library |"
FinalString = FinalString + "\n| Derivation = "+str(funRes)+" | Time to reach result = "+str(FullStop - start)+"(s)"+"\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"


#   Basic Python
def f(x):
    return (6 * x ** 3) * (4 + 2 * x ** -2)


def deriv(func, val, h=0.001):
    return (func(val + h) - func(val)) / h


start = process_time()
funRes = deriv(f, 7)
FullStop = process_time()


FinalString = FinalString + "\n| Basic Python |"
FinalString = FinalString + "\n| Derivation = "+str(funRes)+" | Time to reach result = "+str(FullStop - start)+"(s)"
FinalString = FinalString + "\n\n"

# Integration
start = process_time()
funRes = integrate.quad(lambda x: (2 * x ** 2 - 4 * x + 4) / 4, 0, 2)
FullStop = process_time()


FinalString = FinalString + "\n| Scipy Library |"
FinalString = FinalString + "\n| Integration = "+str(funRes)+" | Time to reach result = "+str(FullStop - start)+"(s)"+"\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"


#   Basic Python
def f(x):
    return (2 * x ** 2 - 4 * x + 4) / 4


start = process_time()
funRes = 0
x = 0
b = 2
dx = 0.0001
while x < b:
    funRes += dx * (f(x) + f((x + dx))) / 2
    x += dx
FullStop = process_time()


FinalString = FinalString + "\n| Basic Python |"
FinalString = FinalString + "\n| Integration = "+str(funRes)+" | Time to reach result = "+str(FullStop - start)+"(s)"
FinalString = FinalString + "\n\n"

# Scalar prodict
start = process_time()
a = np.array([2, 6, 10])
b = np.array([3, 9, 15])
funRes = sum(a * b)
FullStop = process_time()

FinalString = FinalString + "\n| Numpy Library |"
FinalString = FinalString + "\n| Scalar product = "+str(funRes)+" | Time to reach result = "+str(FullStop - start)+"(s)"+"\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"

#   Basic Python
start = process_time()
funRes = 0
a = (2, 6, 10)
b = (3, 9, 15)
for i in range(len(a)):
    funRes += a[i] * b[i]
FullStop = process_time()


FinalString = FinalString + "\n| Basic Python |"
FinalString = FinalString + "\n| Scalar product = "+str(funRes)+" | Time to reach result = "+str(FullStop - start)+"(s)"
FinalString = FinalString + "\n\n"

# Factorial
start = process_time()
x = 55200
funRes = factorial(x)
FullStop = process_time()
funRes = str(funRes)

FinalString = FinalString + "\n| Math Library |"
FinalString = FinalString + "\n| Factorial of "+str(x)+" = "+str(funRes[:10])+" | Time to reach result = "+str(FullStop - start)+"(s)"+"\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"

#   Basic Python
start = process_time()
x = 55200
funRes = 1
for i in range(1, x + 1):
    funRes = funRes * i
FullStop = process_time()
funRes = str(funRes)


FinalString = FinalString + "\n| Basic Python |"
FinalString = FinalString + "\n| Factorial of "+str(x)+" = "+str(funRes[:10])+" | Time to reach result = "+str(FullStop - start)+"(s)"
FinalString = FinalString + "\n\n"

# Matrix
start = process_time()
matrix = [[55, 1492, 2001], [606, 1526, 1944], [0, 1939, 2022]]
funRes = np.array(matrix) * 15
FullStop = process_time()


FinalString = FinalString + "\n| Numpy Library |"
FinalString = FinalString + "\n| Matrix = "+str(funRes)+" | Time to reach result = "+str(FullStop - start)+"(s)"+"\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"

#   Basic Python
start = process_time()
matrix = [[55, 1492, 2001], [606, 1526, 1944], [0, 1939, 2022]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] = matrix[i][j] * 15
FullStop = process_time()


FinalString = FinalString + "\n| Basic Python |"
FinalString = FinalString + "\n| Matrix = "+str(matrix)+" | Time to reach result = "+str(FullStop - start)+"(s)"

def LibraryPrint():
    print(FinalString)