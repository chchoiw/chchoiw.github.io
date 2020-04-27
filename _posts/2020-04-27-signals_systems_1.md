---
title: 'DT LTI Systems and Convolution '
date: 2020-04-27
permalink: /posts/2020/04/signals_systems1/
tags:
  - DT LTI Systems and Convolution
category:
  - Signals and Systems
---

# convolution sum 

\begin{equation}\label{convolution}
y[n]=\sum\limits_{k=-\infty}^{\infty}x[k]h[n-k]
\end{equation}

# unit pluse signal $\delta[n]$
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