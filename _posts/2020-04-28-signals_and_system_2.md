---
title: 'DT LTI Systems and Convolution '
date: 2020-04-27
permalink: /posts/2020/04/signals_systems1/
tags:
  - CT Fourier Transform
category:
  - Signals and Systems
---


# Sources 
- This is the notes while studying [ECE 2200 Signals and Information](https://www.youtube.com/watch?v=pKBiM809pHg&list=PLbRC1c7YJfgBuWDCFI8kVYfdd_GnOkKmm).

- Also, another source I go through is [PDF](https://pages.jh.edu/~bcooper8/sigma_files/courses/214/signalsandsystemsnotes.pdf)


# CT Fourier Transform
If $x(t)$ is $T_0$-periodic, $x(t)$ can be written as 

\begin{equation} \label{Fourier1}
x(t)=\sum\limits_{k=-\infty}^{\infty}X_k e^{jk\omega_0 t}
\end{equation}

\begin{equation} \label{Fourier2}
X_k=\frac{1}{T_0}\int\limits_{k=-\frac{T_0}{2} }^{\frac{T_0}{2}}x(t) e^{-jk\omega_0 t}dt 
\end{equation}