def forward_derivate(f, x0, h):
    return (f(x0+h) - f(x0))/h

def backward_derivate(f, x0, h):
    return (f(x0) - f(x0-h))/h

def central_derivate(f, x0, h):
    return (f(x0+h) - f(x0-h))/(2*h)

def forward_derivate_adaptive(f, x0, h_adaptive):
    return (f(x0+h_adaptive) - f(x0))/h_adaptive

def backward_derivate_adaptive(f, x0, h_adaptive):
    return (f(x0) - f(x0-h_adaptive))/h_adaptive

def central_derivate_adaptive(f, x0, h_adaptive):
    return (f(x0+h_adaptive) - f(x0-h_adaptive))/(2*h_adaptive)


def DerivPrint():
    f = lambda x: x**2 + 3
    x0 = 4
    h = 0.526
    h_adaptive = float(input("Input adaptive step(only numbers please): ").replace(",", "").replace(" ", ""))

    TmpFd = forward_derivate(f, x0, h)
    TmpBd = backward_derivate(f, x0, h)
    TmpCd = central_derivate(f, x0, h)
    TmpFda= forward_derivate_adaptive(f, x0, h_adaptive)
    TmpBDa = backward_derivate_adaptive(f, x0, h_adaptive)
    TmpCda = central_derivate_adaptive(f, x0, h_adaptive)

    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    print(f"| No Input forward = {TmpFd} | Input forward = {TmpFda} |")
    print(f"| No Input backward = {TmpBd} | Input backward = {TmpBDa} |")
    print(f"| No input central = {TmpCd} | Input central = {TmpCda} |")
    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")