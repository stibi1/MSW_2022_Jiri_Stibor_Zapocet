import numpy as np
from matplotlib import pyplot as plt

def Rk4(f, y, h):
    k1 = f(y)
    k2 = f(y + (h/2.)*k1)
    k3 = f(y + (h/2.)*k2)
    k4 = f(y + h*k3)
    y = y + (h/6.)*(k1 + 2.*k2 + 2.*k3 + k4)
    return y

def LvPp(y):
    r = np.array([0.06,0.03])
    D = np.array([0.05,0.6])
    return np.array([r[0]*y[0] - D[0]*y[0]*y[1],r[1]*y[0]*y[1] - D[1]*y[1]])

h = 0.01
maxSteps = 9999
step = 0
fieldTime = np.zeros(maxSteps+1)
fieldPrey = np.zeros(maxSteps+1)
fieldPredator = np.zeros(maxSteps+1)
y = np.array([8.,2.])
fieldPrey[step] = y[0]
fieldPredator[step] = y[1]


while step < maxSteps:
    y = Rk4(LvPp,y,h)
    step += 1
    fieldPrey[step] = y[0]
    fieldPredator[step] = y[1]
    fieldTime[step] = step*h


preyPlot , = plt.plot(fieldTime ,fieldPrey ,'r',linewidth=2,label='Prey')
predatorPlot , = plt.plot(fieldTime ,fieldPredator ,'b',linewidth=2,label='Predator')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend(handles=[preyPlot , predatorPlot])

def DiffShow():
    plt.show()