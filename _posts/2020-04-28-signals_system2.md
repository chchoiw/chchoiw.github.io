---
title: 'CT Fourier Transformm'
date: 2020-04-28
permalink: /posts/2020/04/signals_systems2/
tags:
  - CT Fourier Transformm
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
X_k=\frac{1}{T_0}\int_{-\frac{T_0}{2} }^{\frac{T_0}{2}}x(t) e^{-jk\omega_0 t}dt 
\end{equation}

Define the complex-valued function $X(\omega)$ by

$$
X(\omega)=\int_{-\frac{T_0}{2} }^{\frac{T_0}{2}}x(t) e^{-j\omega t}dt 
$$

Hence,

\begin{equation} \label{Fourier3}
X_k=\frac{1}{T_0}X(k\omega_0)=\frac{\omega_0}{2\pi}X(k\omega_0)
\end{equation}

\begin{equation}\label{Fourier4}
x(t)=\sum\limits_{k=-\infty}^{\infty} \frac{\omega_0}{2\pi}X(k\omega_0)e^{jk\omega_0 t}
\end{equation}

Considering $T_0 \rightarrow \infty$, that is, $\omega_0 \rightarrow 0$


\begin{equation}\label{Fourier5}
x(t)=\sum\limits_{k=-\infty}^{\infty} \frac{\omega_0}{2\pi}X(k\omega_0)e^{jk\omega_0 t}
=\frac{1}{2\pi}\int_{-\infty }^{\infty}X(\omega) e^{jk\omega t}d\omega 
\end{equation}

and $\eqref{Fourier2}$ becomes

\begin{equation}\label{Fourier6}
X_k=\frac{1}{T_0}\int_{-\frac{T_0}{2} }^{\frac{T_0}{2}}x(t) e^{-jk\omega_0 t}dt 
\end{equation}

## $X(\omega) meaning$

In fact, the Fourier transform $X(\omega)$ describes the frequency content of the signal $x(t)$. Usually using the magnitude spectrum and the phase spectrum to show.

