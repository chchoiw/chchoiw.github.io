---
title: 'Optimization'
date: 2019-10-09
permalink: /posts/2019/10/optimization/
tags:
  - Optimization
category:
  - Machine Learning
---


- [Optimization](#Optimization)
  - [Optimization Examples in Machine Learning](#Optimization-Examples-in-Machine-Learning)
  - [Least-square Problem](#Least-square-Problem)
  - [Quadratic Function(Standard Form)](#Quadratic-FunctionStandard-Form)
  - [Solve an uncontrained MP](#Solve-an-uncontrained-MP)
  - [The First Order Tayor Expansion](#The-First-Order-Tayor-Expansion)
  - [Newton's Method](#Newtons-Method)
  - [Constrained Optimization Problem](#Constrained-Optimization-Problem)
  - [Definitions and Notations](#Definitions-and-Notations)
  - [The most important concept in optimization](#The-most-important-concept-in-optimization)
  - [Minimum Principle](#Minimum-Principle)
  - [Linear Programming Problem](#Linear-Programming-Problem)
  - [$L_1$- Approximation](#L_1--Approximation)
# Optimization
- Basically, this is my studying from [NTCU open course](http://ocw.nctu.edu.tw/index.php) - [Machine Learning](http://ocw.nctu.edu.tw/course_detail.php?bgid=1&gid=1&nid=563&page=1). I  take the key points for my references.
## Optimization Examples in Machine Learning
- Maximum likelihood estimation
- Maximum a posteriori estimation
- Least square estimates
- Gradient descent method
- Backpropagation

## Least-square Problem
$$
\min\limits_{x\in \mathbb R^n}\Vert Ax-b\Vert_2^2
$$

$$
\begin{aligned}
\nabla f(x) &=2A^TAx-2A^Tb \\
\nabla^2 f(x) &=2A^TA \\
x^* &= (A^TA)^{-1}A^Tb
\end{aligned}
$$

## Quadratic Function(Standard Form)

Let $f:\mathbb R^n \rightarrow \mathbb R$:
$$
f(x) =\frac{1}{2}x^THx+p^Tx
$$

$$
\begin{aligned}
\nabla f(x) &=Hx+p \\
\nabla^2 f(x) &=H \\
x^* &= H^{-1}p
\end{aligned}
$$

## Solve an uncontrained MP
- Get an intinal point and iteratively decrease the obj function
- stop once the stopping criteria satisfied
- steep decent might not be a good choice
- Newton's Method is highly recommded
    * Local and quadratic convergent algorithm
    * Need to choose a good step size to guarantee global convergence.
## The First Order Tayor Expansion
Let $f:\mathbb R^n \rightarrow \mathbb R$ be a differentiable function:
$$
f(x+d)=f(x)+ \nabla f(x)^Td+\alpha(x,d) \Vert  d\Vert
$$
where 
$$
\lim_{d \rightarrow 0}\alpha(x,d)  =0
$$
If $\nabla f(x)^Td<0$ and $d$ is small enough, then $f(x+d) < f(x)$. We call $d$ is descent direction.

## Newton's Method

$$
f(x+d)=\nabla f(x)^Td+d\frac{1}{2}d^T \nabla^2f(x)d+\beta(x,d) \Vert d\Vert
$$
where $\lim\limits_{d \rightarrow 0} \beta(x,d)=0.$

Start with $x_0 \in \mathbb R^n$. Having $x_i$, stop if $\nabla f(x_i)=0$. Else compute $x_i$ as follows:
1. Newton direction: $\nabla^2 f(x_i)d_i =-\nabla f(x_i)$. Have to solve a system of linear equation .
2. Updating:$x_{i+1}=x_i+d_i$
    - converge only if $x_0$ is close to $x^{*}$.

## Constrained Optimization Problem
Problem settting: Give function $f_i,g_i ,i=1,\dots,n$ and $h_j,j=1,\dots,m$, defined on a domain $\Omega \mathbb R^n$,

$$
\begin{aligned}
\min_{x\in \Omega} f(x) &\quad s.t. \\
g_i(x) \leq 0 &\quad \forall  i \\
h_j(x) = 0 &\quad \forall  j
\end{aligned} 
$$
where $f(x)$ is called the objective function and $g(x) \leq 0$, $h(x)=0$ are called constrains.

## Definitions and Notations
- Feasible region:
$$
\mathbf F= \{x \in \Omega | g(x) \leq 0, h(x)=0 \}
$$

- A solution of the optimization problem is a point $x^* \in \mathbf F$ s.t. $x \in \mathbf F$ for which $f(x) \leq f(x^{*})$ and $x^*$ is called global minimum.

- At the solution $x^{*}$, an inequality constraint $g_i(x)$ is said to be active if $g_i(x^*)=0$. Otherwise it is called an inactive constraint.

- $g_i(x) \leq 0 \Leftrightarrow g_i(x)+\xi_i=0,\quad \xi_i \geq 0$ where $\xi_i $ is called slack variable.

- Renew an inactive constraint is an optimization problem will **NOT** affect the optimal solution.

- If  $\mathbf F=\mathbb R^n $, then the problem is called an contrained minimization problem.
    * Least square problem is in this
    * SSVM 
    * Difficult to find the global minimum without convexity assumption.
     
## The most important concept in optimization
- A point is said to be an optimal solution of a unconstrained minimization if there exists no decent direction.  $ \Rightarrow$ $f(x^*)=0$.

- A point is said to be an optimal solution of a constrained minimization if there exists no feasible decent direction. $ \Rightarrow$ KKT conditions.
    * There might exist decent direction but move along this direction will leave out the feasible region.

## Minimum Principle
Let $f: \mathbb R^n \rightarrow \mathbb R$ be a convex and continously differentiable function $\mathbf F \subseteq \mathbb R^n$ be the feasible region.

$$
x^* \in \arg\min_{x \in \mathbf F} f(x) \Leftrightarrow \nabla f(x^*)(x-x^*) \geq 0 \quad \forall x \in \mathbf F
$$

## Linear Programming Problem
- An optimization problem in which the objective function and all constrains are linear functions is called a linear programming problem.

$$
\begin{aligned}
\min_{x\in \Omega} &p^T x \quad s.t. \\
A(x) &\leq b  \\
C(x) &= d  \\
L \leq x &\leq U
\end{aligned} 
$$

## $L_1$- Approximation
$$
\begin{aligned}
&\min\limits_{x \in \mathbb R^n} \Vert Ax-b \Vert_1 \\ 
\Leftrightarrow  &
\min\limits_{x,s} \sum\limits_{i=1}^n s_i \quad &s.t.  \quad  -s_i \leq Ax-b_i \leq s_i \\
\Leftrightarrow & \min_{x,s}[0 \dots 0,1,\dots,1]\left[ \begin{matrix}
   x \\
   s
  \end{matrix} \right] \quad &s.t. \quad 
  \left[ \begin{matrix}
   A, -I \\
   -A, I
  \end{matrix} \right]
  \left[ \begin{matrix}
   x \\
   s
  \end{matrix} \right] \leq 
  \left[ \begin{matrix}
   b \\
   -b
  \end{matrix} \right]
\end{aligned}
$$

This is  a linear programming problem.