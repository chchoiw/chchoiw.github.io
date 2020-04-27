---
title: 'DT LTI Systems and Convolution '
date: 2020-04-27
permalink: /posts/2020/04/signals_systems1/
tags:
  - DT LTI Systems and Convolution
category:
  - Signals and Systems
---


# LTI Systems
- A LTI system is a linear time-invaiant system, that is 

1. Linear:

```mermaid
graph LR
A(xn) --> B(System S) -->C(yn)
```


1. Time-invaiant:


## convolution sum 

\begin{equation}\label{convolution}
y[n]=\sum\limits_{k=-\infty}^{\infty}x[k]h[n-k]
\end{equation}

## unit pluse signal $\delta[n]$

$$
\delta[n]=\Bigg\{
\begin{aligned}
   &1 &\text{when} \quad &n=0 \\
   &0 &\text{when} \quad &n\neq 0   
\end{aligned}
$$

\begin{equation}\label{convolution identity}
x[n]=\sum\limits_{k=-\infty}^{\infty}x[k]\delta[n-k]
\end{equation}


## LTI system and convolution sum

Let $h[n]=y[n], x[n]=\delta[n]$, then $y[n]$ can be written as a convolution sum:

$$
y[n]=\sum\limits_{k=-\infty}^{\infty}h[k]x[n-k]
$$

```mermaid
graph LR
A("x[n]") --> B("LTI h[n]") -->C("y[n]")
```
