# Numerical Methods for Visualizing Geodesics on Surfaces

This project provides a numerical solver for the **geodesic equation** on surfaces. Given a differentiable manifold $M$ equipped with a connection $\nabla$ and a parameterization $x : \Omega \rightarrow M$ (where $\Omega$ is an open set of $\mathbb{R}^2$), the goal is to solve the geodesic equation on $\Omega$ by finding a curve $\gamma : I \rightarrow \Omega$ such that:

$$\frac{d^2\gamma^k}{dt^2} + \Gamma_{ij}^{k}\frac{d\gamma^i}{dt}\frac{d\gamma^j}{dt} = 0$$

Here:  
- $\gamma^k = x^k \circ \gamma$ are the coordinates of the curve $\gamma$,  
- $\Gamma_{ij}^k$ are the Christoffel symbols of the connection $\nabla$.

## 🛠️ Project Features

### Purpose
This repository serves as a tool to support the study of **differential geometry** by enabling the visualization of geodesics using numerical methods. It bridges the theoretical foundation with computational practices by solving geodesic equations for surfaces.

### Key Workflow
1. **Theoretical Preparation**:  
   Perform the required calculations to derive the geodesic equation for a given surface by hand. This exercise strengthens understanding of the underlying mathematics.
2. **Numerical Implementation**:  
   Input the geodesic equations into a subclass of `Surface` in `dynamics.py` to enable numerical solving and visualization.

---

## 💻 Code
All code is written in **Python 3.10.12**. Below are examples of the visualizations produced using this repository. These images are obtained with the **test.ipynb** file.

### Examples

#### Geodesics on a Sphere and Torus
<p align="center">
  <img src="/images/Sphere.png" width="400" />
  <img src="/images/Torus.png" width="400" />
</p>

#### Same Visualizations Using MATLAB
<p align="center">
  <img src="/images/Sphere_matlab.png" width="400" />
  <img src="/images/Torus_matlab.png" width="400" />
</p>
