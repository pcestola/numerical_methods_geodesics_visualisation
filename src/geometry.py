import numpy as np
from matplotlib.pyplot import axes

class Surface:
    def __init__(self) -> None:
        pass

    def dynamic(self, t:float, y:np.ndarray) -> np.ndarray:
        raise NotImplementedError("Method 'dynamic' not implemented.")
    
    def parametrization(self, u:np.ndarray, v:np.ndarray) -> np.ndarray:
        raise NotImplementedError("Method 'parametrization' not implemented.")
    
    def gauss_map(self, u:np.ndarray, v:np.ndarray) -> np.ndarray:
        raise NotImplementedError("Method 'gauss_map' not implemented.")
    
    def draw(self, ax, u, v, alpha=0.7, shade=True):
        u, v = np.meshgrid(u,v)
        x, y, z = self.parametrization(u,v)
        return ax.plot_surface(x, y, z, linewidth=0, alpha=alpha, shade=shade, antialiased=False)

class Sphere(Surface):
    def __init__(self) -> None:
        super().__init__()
    
    def dynamic(self, t: float, y: np.ndarray) -> np.ndarray:
        u, v, z, w = y[0], y[1], y[2], y[3]
        return np.array([
            z,
            w,
            -2/np.tan(v)*z*w,
            0.5*np.sin(2*v)*z*z
        ])
    
    def parametrization(self, u: np.ndarray, v: np.ndarray):
        x = np.sin(v)*np.cos(u)
        y = np.sin(v)*np.sin(u)
        z = np.cos(v)
        return x, y, z
    
    def gauss_map(self, u: np.ndarray, v: np.ndarray):
        # the sphere is a lucky case :)
        x, y, z = self.parametrization(u,v)
        return -x, -y, -z
    
class Torus(Surface):
    def __init__(self, R: float, r: float) -> None:
        super().__init__()
        self.R = R
        self.r = r
    
    def dynamic(self, t: float, y: np.ndarray) -> np.ndarray:
        u, v, z, w = y[0], y[1], y[2], y[3]
        temp1 = self.R + self.r * np.cos(v)
        temp2 = np.sin(v)
        Christoffel_uu_v = temp1 * temp2 / self.r
        Christoffel_uv_u = - self.r * temp2 / temp1
        return np.array([
            z,
            w,
            -2*Christoffel_uv_u*z*w,
            -Christoffel_uu_v*z*z
        ])
    
    def parametrization(self, u: np.ndarray, v: np.ndarray):
        x = (self.R + self.r * np.cos(v)) * np.cos(u)
        y = (self.R + self.r * np.cos(v)) * np.sin(u)
        z = self.r * np.sin(v)
        return x, y, z
