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

\begin{equation} \label{def_X}
X(\omega)=\int_{-\frac{T_0}{2} }^{\frac{T_0}{2}}x(t) e^{-j\omega t}dt 
\begin{equation} \label{Fourier2}

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

and $\eqref{def_X}$ becomes

\begin{equation}\label{Fourier6}
X(\omega)=\int_{-\infty}^{\infty}x(t) e^{-jk\omega_0 t}dt 
\end{equation}

## $X(\omega) meaning$

In fact, the Fourier transform $X(\omega)$ describes the frequency content of the signal $x(t)$. Usually using the magnitude spectrum and the phase spectrum to show.

Example:

$$
x(t)=e^{-3t}u(t)
$$

According $\eqref{Fourier6}$,

\begin{aligned}
X(\omega)
&=\int_{-\infty}^{\infty}x(t) e^{-jk\omega_0 t}dt  \\
&=\int_{0}^{\infty}e^{-3t} e^{-jk\omega_0 t}dt  \\
&=\frac{-1}{3+j\omega}e^{-(3+j\omega)t}\Bigg\vert_{0}^{\infty} \\
&=\frac{-1}{3+j\omega}
\end{aligned}

Hence,
$$
\vert X(\omega)\vert =\frac{1}{\sqrt{9+\omega^2}}
$$


<div style="text-align:center" id="image1"><img src="/images/signal/signal1.png" /><br>圖 1</div>


$$
\text{phase}(X(\omega) )=\tan^{-2}(\frac{\omega}{3})
$$


<div style="text-align:center" id="image2"><img src="/images/signal/signal2.png" /><br>圖 2</div>

Remark:by $\eqref{Fourier6}$

$$
X^{*}(\omega)=(\int_{-\infty}^{\infty}x(t) e^{-jk\omega_0 t}dt)^*=\int_{-\infty}^{\infty}x(t) e^{jk\omega_0 t}dt=X(-\omega)
$$

## Examples:
1. $x(t)=\delta(t)$, by shifting property

$$
X(\omega)=1
$$

2. 
$$x(t)=\Bigg\{
    \begin{aligned}
    &1 \quad &\t \in [-T_1,T_1] \\
    &0 \quad &\text{otherwise}
    \end{aligned}
$$

<div style="text-align:center" id="image3"><img src="/images/signal/signal3.png" /><br>圖 2</div>

$$
 \begin{aligned}
X(\omega)&=\int_{-T_1}^{T_1}e^(-j\omega t) dt=\frac{1}{j\omega}(e^{j\omega T_1}-e^{-j\omega T_1})\\
&=2T_1\frac{1}{\omega T_1}\sin(\omega T_1)=2T_1\sinc(\frac{\omega T_1}{\pi})
 \end{aligned}
 $$