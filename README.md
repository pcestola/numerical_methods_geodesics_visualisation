# Numerical methods for visualising geodesics on surfaces

This project introduces a solver for the **geodesics equation** on surfaces. Given a differentiable manifold $M$ equipped with a connection $\nabla$ and a parameterisation $x : \Omega \rightarrow M$ with $\Omega$ open set of $\mathbb{R}^2$, solving the geodesics equation on $\Omega$ requires finding a curve $\gamma : I\rightarrow \Omega$ such that:
$$\frac{d^2\gamma^k}{dt^2} + \Gamma_{ij}^{k}\frac{d\gamma^i}{dt}\frac{d\gamma^j}{dt}=0$$
where $\gamma^k = x^k\circ\gamma$ are the coordinates of the curve $\gamma$ and $\Gamma_{ij}^{k}$ are the Christoffel symbols of the connection $\nabla$.

### Note
The code in this repository is designed as support for the study of differential geometry by visualising geodesics using numerical methods. Given a surface, it is recommended to perform by hand the calculations required to set up the geodesics equation manually, as a theoretical exercise, and then enter them into an appropriate subclass of *Surface* in *dyanmics.py* so that the equation can be solved numerically.

## 💻Code
All the code is written using __python 3.10.12__. Below there is an example of the images that can be produced with the code. The creation of these two images is shown in the file __test.ipynb__.

<p align="center">
  <img src="/images/Sphere.png" width="400" />
  <img src="/images/Torus.png" width="400" /> 
</p>

Same images produced with matlab

<p align="center">
  <img src="/images/Sphere_matlab.png" width="400" />
  <img src="/images/Torus_matlab.png" width="450" /> 
</p>
