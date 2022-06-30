import numpy as np
from numpy import *
from scipy import integrate

def HarmFun(x):
    return 2 * sin(8 * x)

def LogFun(x):
    return log(7 * x) + (2 / 7)

def PolyFun(x):
    return x ** 2 - 3 * x + 9




def Rie(function,x,y):
    return integrate.quadrature(function, x, y)

def Simp(function,x,y, z=0.06):
    return integrate.simpson(function(np.arange(x, y + z, z)), np.arange(x, y + z, z))

def Romb(function, x, y):
    return integrate.romberg(function, x, y)


def Results():

    print("\n\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    print("| Harmonic function          |")
    print("| Fun  | Results             |")
    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    print(f"| Rie  | {Rie(HarmFun, 1, 2)[0]} |")
    print(f"| Simp | {Simp(HarmFun, 1, 2)} |")
    print(f"| Romb | {Romb(HarmFun, 1, 2)} |")
    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")

    print("\n\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    print("| Logarithnmical function   |")
    print("| Fun  | Results            |")
    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    print(f"| Rie  | {Rie(LogFun, 1, 2)[0]} |")
    print(f"| Simp | {Simp(LogFun, 1, 2)}  |")
    print(f"| Romb | {Romb(LogFun, 1, 2)}  |")
    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")

    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    print("| Polynomic function       |")
    print("| Fun  | Results           |")
    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    print(f"| Rie  | {Rie(PolyFun, 1, 2)[0]} |")
    print(f"| Simp | {Simp(PolyFun, 1, 2)} |")
    print(f"| Romb | {Romb(PolyFun, 1, 2)} |")
    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")

