import numpy as np
from matplotlib import cm
from typing import Callable, Tuple
import matplotlib.pyplot as plt
from geometry import Sphere, Torus, Surface
from ode_methods import OdeMethod, ForwardEuler, RungeKutta, AdamsBashforth
from abc import ABC, abstractmethod

class Solver(ABC):
    def __init__(self, geometry: Surface) -> None:
        self.geometry = geometry

    @abstractmethod
    def solve(self, initial_condition: np.ndarray, total_time: float, steps_number: int):
        pass

    
class MultiStepSolver(Solver):
    def __init__(self, geometry: Surface, initialization: OdeMethod, multistep: OdeMethod) -> None:
        super().__init__(geometry)
        self.initialization = initialization
        self.multistep = multistep

    def solve(self, initial_condition: np.ndarray, total_time: float, steps_number: int) -> np.ndarray:
        # Initialize solution array
        solution = np.zeros((steps_number,4), dtype=np.float32)
        solution[0] = initial_condition
        # Calculating the time step
        step = total_time/steps_number
        # Initialization
        for t in range(self.multistep.initial_steps):
            solution[t+1] = self.initialization(self.geometry.dynamic, step, t, solution)
        # Multistep
        for t in range(self.multistep.initial_steps, steps_number-1):
            solution[t+1] = self.multistep(self.geometry.dynamic, step, t, solution)
        return solution

def draw_solver_solution(geometry: Surface, solution: np.ndarray, u_domain: Tuple[float,float,int], v_domain: Tuple[float,float,int]) -> None:
    u_space = np.linspace(u_domain[0],u_domain[1],u_domain[2])
    v_space = np.linspace(v_domain[0],v_domain[1],v_domain[2])
    # Embedding of the curve
    x, y, z = geometry.parametrization(solution[:,0], solution[:,1])
    # Drawing
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # Drawing the surface and the solution curve
    surface = geometry.draw(ax, u_space, v_space)
    curve = ax.plot(x, y, z, '-k', linewidth=2, zorder=3)
    # Highlighting start and end points
    start_point = ax.plot(x[0], y[0], z[0], 'og', zorder=3, markeredgewidth=1, markeredgecolor='k')
    end_point = ax.plot(x[-1], y[-1], z[-1], 'or', zorder=3, markeredgewidth=1, markeredgecolor='k')
    ax.axis('equal')
    return fig, ax