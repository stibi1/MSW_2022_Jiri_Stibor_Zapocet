import numpy as np
from numpy import *
import time
import matplotlib.pyplot as plt



def Jacobi(A, b, niteraci, x0):
    x = x0
    D = np.diag(A)
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)
    for i in range(niteraci):
        x = (b - np.matmul((L + U), x)) / D
        if (
        np.allclose(x, gaussSolution, rtol=1e-8, atol=1e-9, )) == True:
            break
    return x


def gaus(A, b):
    x = np.linalg.solve(A, b)
    return x




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    casyG = []
    casyJ = []
    CASYG = []
    CASYJ = []

    m = int(input("Entre matrix size: ").replace(",", "").replace(" ", ""))
    print("Matrix size = ", m)
    m = int(m)
    print("Loading")

    for M in range(m - 1):
        M = M + 2
        a = np.ones(M)  # řada 1
        array
        A1 = np.diagflat([a])
        diag
        A2 = np.ones((M, M), dtype=int)
        array
        A = A1 + A2
        b1 = np.ones(M)
        array
        b = b1 * (M + 1)
        for v in range(100):
            x0 = np.ones(len(A))
            g_start = time.perf_counter()
            gaussSolution = gaus(A, b)
            g_end = time.perf_counter()
            g = g_end - g_start
            g = round(1000000 * g)
            jStart = time.perf_counter()
            jacobiSolution = Jacobi(A, b, 100, x0)
            jEnd = time.perf_counter()
            j = jEnd - jStart
            j = round(1000000 * j)

            casyG.append(g)
            casyJ.append(j)

        PG = mean(casyG)
        PJ = mean(casyJ)
        casyG = []
        casyJ = []
        CASYG.append(PG)
        CASYJ.append(PJ)

    fig, ax = plt.subplots()
    line = plt.plot(CASYG, label="Gauss elimination method")
    line = plt.plot(CASYJ, label="Jacobi iteration method")
    plt.title(
        r'Time required for solution')
    plt.xlabel('Size of the matrix')
    plt.ylabel('Time of solution [10^-6 s]')

    ax.legend(loc=2)

    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
