---
title: 'DT LTI Systems and Convolution '
date: 2020-04-27
permalink: /posts/2020/04/signals_systems1/
tags:
  - DT LTI Systems and Convolution
category:
  - Signals and Systems
---

- [Sources](#sources)
- [LTI Systems](#lti-systems)
  - [convolution sum](#convolution-sum)
  - [unit pluse signal $\delta[n]$](#unit-pluse-signal-math-xmlns%22httpwwww3org1998mathmathml%22semanticsmrowmi%ce%b4mimo-stretchy%22false%22mominmimo-stretchy%22false%22momrowannotation-encoding%22applicationx-tex%22deltanannotationsemanticsmath%ce%b4n)
  - [LTI system and convolution sum](#lti-system-and-convolution-sum)
  - [properties of convolution sum](#properties-of-convolution-sum)
    - [Causal System](#causal-system)
    - [Memoryless System](#memoryless-system)
    - [Stable System](#stable-system)
  - [Complex Eigenfunctions](#complex-eigenfunctions)

# Sources 
- This is the notes while studying [ECE 2200 Signals and Information](https://www.youtube.com/watch?v=pKBiM809pHg&list=PLbRC1c7YJfgBuWDCFI8kVYfdd_GnOkKmm).

- Also, another source I go through is [PDF](https://pages.jh.edu/~bcooper8/sigma_files/courses/214/signalsandsystemsnotes.pdf)


# LTI Systems
- An LTI system is a linear time-invaiant system, that is 

1. Linear:
```mermaid
graph LR
A("x[n]")-->B("System S")
B-->C("y[n]")
```
```mermaid
graph LR
A("r[n]") --> B("System S") 
B-->C("s[n]")
```
```mermaid
graph LR
A("x[n]+r[n]") --> B("System S") 
B-->C("y[n]+s[n]")
```

2. Time-invaiant:
```mermaid
graph LR
A("x[n-n0]") --> B("System S") 
B-->C("y[n-n0]")
```

## convolution sum 

\begin{equation}\label{convolution}
y[n]=\sum\limits_{k=-\infty}^{\infty}x[k]h[n-k]\triangleq (h*x)[n]
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

We will represent this LTI system as following digram:
```mermaid
graph LR
A("x[n]") --> B("LTI h[n]") 
B-->C("y[n]")
```

## properties of convolution sum
- Commutativity

$$
(x*h)[n]=(h*n)[n]
$$

- Associativity

$$
(x*(h_1*h_2))[n]=((x*h_1)*h_2)[n]
$$

- Distributivity

$$
(x*(h_1+h_2))[n]=(x*h_1)[n]+(x*h_2)[n]
$$

- Shift property
let $\hat x [n]=x[n-n_0]$

$$
(\hat x * h)[n]=(x*h)[n-n_0]
$$

- Identity

$$
(x*\delta)[n]=x[n]
$$

### Causal System
- Def: An LTI shstem is causal iff 
  
$$
h[n]=0 \quad \text{if } \quad n<0
$$

### Memoryless System
- Def: An LTI shstem is memoryless iff 
  
$$
h[n]=c\delta[n]
$$


### Stable System
- Def: An LTI shstem is stable iff 

$$
\sum\limits_{n=-\infty}^{\infty} |h[n]| < \infty
$$

## Complex Eigenfunctions

$$
x[n]=x_R[n]+jx_I[n]
$$

$$
y[n]=\sum\limits_{k=-\infty}^{\infty}x_R[k]h[n-k] +j \sum\limits_{k=-\infty}^{\infty}x_I[k]h[n-k]
$$

Hence,

$$
\begin{aligned}
\text{Re}\{y[n]\}&=\text{Re}\{(x*h)[n]\}=(x_R*h)[n] \\
\text{Im}\{y[n]\}&=\text{Im}\{(x*h)[n]\}=(x_I*h)[n]
\end{aligned}
$$

Example:
If $x[n]=e^{j \omega_0 n}$,then

$$
y[n]=\sum\limits_{k=-\infty}^{\infty} h[k]e^{j \omega_0 (n-k)}
=\sum\limits_{k=-\infty}^{\infty} h[k] e^{j \omega_0 (n)}e^{j \omega_0 (-k)}
$$

Say, 

$$
H(\omega_0)=\sum\limits_{k=-\infty}^{\infty} h[k] e^{-j \omega_0 (k)}
$$

then,

$$
y[n]=H(\omega_0)e^{j \omega_0 (n)}
$$

Example:
If $x[n]=\cos(\omega_0 n)=\text{Re}\{ e^{j\omega_0 n } \}$,
then

$$
y[n]=\text{Re}\{ H(\omega_0) e^{j\omega_0 n } \}
$$

Remark:
CT LTI Systems and Convolution is similar to DT one, just replace $\sum$ to $\int$.
