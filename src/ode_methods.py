import numpy as np
from typing import Callable
from abc import ABC, abstractmethod

class OdeMethod(ABC):
    def __init__(self) -> None:
        self.initial_steps = None

    @abstractmethod
    def __call__(self, f:Callable, h:float, t:int, u:np.ndarray) -> np.ndarray:
        pass

class ForwardEuler(OdeMethod):
    def __init__(self) -> None:
        super().__init__()
        self.initial_steps = 0

    def __call__(self, f: Callable, h: float, t: int, u: np.ndarray) -> np.ndarray:
        return u[t] + h * f(h*t, u[t])

class RungeKutta(OdeMethod):
    def __init__(self, order:int) -> None:
        super().__init__()
        self.initial_steps = 0
        self.initalize_method(order)
    
    # Runge Kutta 2
    def runge_kutta_2(self, f:Callable, h:float, t:int, u:np.ndarray) -> np.ndarray:
        k1 = h * f(h*t, u[t])
        k2 = h * f(h*t + h/2, u[t] + k1/2)
        return u[t] + k2

    # Runge Kutta 3
    def runge_kutta_3(self, f:Callable, h:float, t:int, u:np.ndarray) -> np.ndarray:
        k1 = h * f(h*t, u[t])
        k2 = h * f(h*t + h/2, u[t] + k1/2)
        k3 = h * f(h*t + h, u[t] - k1 + 2*k2)
        return u[t] + (k1 + 4*k2 + k3)/6

    # Runge Kutta 4
    def runge_kutta_4(self, f:Callable, h:float, t:int, u:np.ndarray) -> np.ndarray:
        k1 = h * f(h*t, u[t])
        k2 = h * f(h*t + h/2, u[t] + k1/2)
        k3 = h * f(h*t + h/2, u[t] + k2/2)
        k4 = h * f(h*t + h, u[t] + k3)
        return u[t] + (k1 + 2*k2 + 2*k3 + k4)/6

    def initalize_method(self, order):
        if order == 2:
            self.call = self.runge_kutta_2
        elif order == 3:
            self.call = self.runge_kutta_3
        elif order == 4:
            self.call = self.runge_kutta_4
        else:
            # TODO: implementa la versione n-sima
            raise ValueError

    def __call__(self, f: Callable, h: float, t: int, u: np.ndarray) -> np.ndarray:
        return self.call(f, h, t, u)

class AdamsBashforth(OdeMethod):
    def __init__(self, order:int) -> None:
        super().__init__()
        self.initial_steps = order-1
        self.initalize_method(order)
    
    # Adams Bashforth 2
    def adams_bashforth_2(self, f:callable, h:float, t:int, u:np.ndarray) -> np.ndarray:
        return u[t] + h * (3/2 * f(t*h,u[t]) - 1/2 * f((t-1)*h,u[t-1]))

    # Adams Bashforth 3
    def adams_bashforth_3(self, f:callable, h:float, t:int, u:np.ndarray) -> np.ndarray:
        return u[t] + h * (23/12 * f(t*h,u[t]) - 16/12 * f((t-1)*h,u[t-1]) + 5/12 * f((t-2)*h,u[t-2]))

    # Adams Bashforth 4
    def adams_bashforth_4(self, f:callable, h:float, t:int, u:np.ndarray) -> np.ndarray:
        return u[t] + h * (55/24 * f(t*h,u[t]) - 59/24 * f((t-1)*h,u[t-1]) + 37/24 * f((t-2)*h,u[t-2]) - 9/24 * f((t-3)*h,u[t-3]))

    def initalize_method(self, order):
        if order == 2:
            self.call = self.adams_bashforth_2
        elif order == 3:
            self.call = self.adams_bashforth_3
        elif order == 4:
            self.call = self.adams_bashforth_4
        else:
            # TODO: implementa la versione n-sima
            raise ValueError

    def __call__(self, f: Callable, h: float, t: int, u: np.ndarray) -> np.ndarray:
        return self.call(f, h, t, u)


## Implicit methods
# TODO: non utilizzare sempre un metodo iterativo

# Backward Euler
def backward_euler(f:Callable, h:float, t:int, u:np.ndarray, max_iter=100, tol=1e-5) -> np.ndarray:
    z = u[t]
    for _ in range(max_iter):
        z_old = z
        # Applica la formula di Eulero all'indietro come un'iterazione di punto fisso
        z = u[t] + h * f(h*(t+1), z)
        # Controlla la convergenza
        if np.linalg.norm(z - z_old) < tol:
            break
    return z
