# Numerical methods for visualising geodesics on surfaces

The code in this repository is designed as support for the study of differential geometry by visualising geodesics using numerical methods. Given a surface, it is recommended to perform the calculations required to set up the geodesics equation manually, as a theoretical exercise, and then enter them into an appropriate subclass of 'Surface' in 'dyanmics.py' so that the equation can be solved numerically and the geodesics visualised as the initial parameters change.

## 💻Code
All the code is written using __python 3.10.12__. Below there is an example of the images that can be produced with the code. The creation of these two images is shown in the file __test.ipynb__.

<p align="center">
  <img src="/images/Sphere.png" width="400" />
  <img src="/images/Torus.png" width="400" /> 
</p>

## 🔢 Mathematical prerequisites
__Definition__ (Topological manifold)\
A topological manifold of dimension $n\in\mathbb{N}$ is a topological space $\mathcal{M}=(M,\tau)$ that is Hausdorff, has a countable base, and is locally Euclidean, i.e., for every point $p\in M$ there exists an open neighborhood $U$ of $p$ such that $U$ is homeomorphic to $\mathbb{R}^n$.

<img src="/images/local_chart.png" align="right" width="200px"/>

__Definition__ (Local chart)\
Let $\mathcal{M}$ be a topological manifold of dimension $n$, a __local chart__ is a pair $(U,\phi)$ with $U$ open of $\mathcal{M}$ and $\phi : U \rightarrow \Omega\subset\mathbb{R}^n$ homeomorphism from $U$ to a Euclidean open set $\Omega$ of $\mathbb{R}^n$.
<br clear="right"/>

<img src="/images/transition_function.png" align="right" width="200px"/>

__Definition__ (Transition function)\
If $(U_i,\phi_i)$ and $(U_j,\phi_j)$ are two local maps of a topological manifold $\mathcal{M}$ of dimension $n$ such that $U_i\cap U_j\neq\emptyset$, then the map
$$\phi_{ij} : \phi_{i}(U_i\cap U_j) \rightarrow \phi_{j}(U_i\cap U_j),\quad\phi_{ij}(x) = \phi_j \circ \phi_i^{-1}(x)$$
is a homeomorphism called __transition function__ from local chart $(U_i,\phi_i)$ to local chart $(U_j,\phi_j)$.
<br clear="right"/>

__Definition__ (Atlas)\
Let $\mathcal{M}$ be a topological manifold of dimension $n$, an \emph{atlas} is a collection of local charts $\mathcal{A} = \\{(U_i,\phi_i) : i\in I\\}$ such that $\\{U_i : i\in I\\}$ is a covering of $\mathcal{M}$.

__Definition__ (Smooth manifold)\
The pair $(\mathcal{M},\mathcal{A})$ is called a __Smooth manifold__ if $\mathcal{M}$ is a topological manifold, $\mathcal{A}$ is an atlas of $\mathcal{M}$, and every transition function between pairs of atlas maps is of class $C^\infty$.

__Definition__ (Affine connection)\
Let $(\mathcal{M},\mathcal{A})$ be a smooth manifold and let $\Gamma(TM)$ be the space of smooth vector fields on $M$. An affine __connection__ on $M$ is a bilinear map $$\nabla : \Gamma(TM)\times \Gamma(TM)\rightarrow\Gamma(TM)$$ such that for each $f\in C^\infty(M,\mathbb{R})$ and each $X,Y\in\Gamma(TM)$ the following holds
1. $\nabla(fX,Y) = f \nabla(X,Y)$
2. $\nabla(X,fY) = df(X) Y + f \nabla(X,Y)$

### Geodesic

Within the language of _Riemannian geometry_, a __geodesic__ on a smooth manifold $M$ with affine connection $\nabla$ is a curve such that parallel transport along the curve preserves the vector tangent to the curve, informally: $$\nabla(\dot{\gamma},\dot{\gamma})=0$$
To be formal, in order to define the covariant derivative in the equation it is first necessary to extend $\dot{\gamma}$ to a continuously differentiable vector field in an open set, calculate the covariant derivative of that field and finally restrict again to the curve $\gamma$. This procedure is well defined since it is shown to be independent of the choice of the extension. Using local coordinates $x = (x^1,\dots,x^n)$ on $M$, we can write the __geodesics equation__ (using the summation convention) as $$\frac{d^2\gamma^k}{dt^2} + \Gamma_{ij}^{k}\frac{d\gamma^i}{dt}\frac{d\gamma^j}{dt}=0$$
where $\gamma^k = x^k\circ\gamma$ are the coordinates of the curve $\gamma$ and $\Gamma_{ij}^{k}$ are the Christoffel symbols of the connection $\nabla$. The equation means that the acceleration vector of the curve has no components in the direction of the surface and is therefore perpendicular to the tangent plane of the surface at every point on the curve. Therefore, the motion is completely determined by the curvature of the surface.

In our case we are interested in the solution of the geodesic equation for surfaces: smooth varieties of dimension $2$. The geodesic equation is seen as a differential problem with initial conditions specified by a point on the manifold and a direction at that point.
