---
title: '兩條雙曲線的交點'
date: 2020-12-04
permalink: /posts/2020/12/hyperbola/
tags:
  - hyperbola
category:
  - High School Math
---


# Introduction
設 $(a_1,b_1), (a_2,b_2)$是雙曲的兩個焦點, 然後曲線上到兩焦點絕對距離差是$d_1$
那麽
$$
\begin{aligned}
\Bigg\vert \sqrt{(x-a_1)^2+(y-b_1)^2}-\sqrt{ (x-a_1)^2+(y-b_1)^2}\Big\vert & =d_1\\
\sqrt{(x-a_1)^2+(y-b_1)^2}&= \pm d +\sqrt{(x-a_2)^2+(y-b_2)^2} \\
(x-a_1)^2+(y-b_1)^2 &= (\pm d +\sqrt{(x-a_2)^2+(y-b_2)^2) } ^2\\
2(a_2-a_1)x+2(b_2-b_1)y+a_1^2+b_1^2d_1^2-a_2^2-b_2^2 &= d_1^2 +2d \sqrt{(x-a_2)^2+(y-b_2)}
\end{aligned}
$$

若令

$$
\begin{align}
U&=2(a_2-a_1) \label{U}\\
S&=2(b_2-b_1) \label{S}\\
T&=a_1^2+b_1^2d_1^2-a_2^2-b_2^2 \label{T}
\end{align}
$$

則上述等式可轉化為

$$
\begin{aligned}
(Ux+Sy+T) &= 2d_1 \sqrt{(x-a_2)^2+(y-b_2)} \\
(Ux+Sy+T)^2 &= ( 2d_1 \sqrt{(x-a_2)^2+(y-b_2)^2  } )^2 \\
U^2x^2+S^2y^2 +T^2+2USxy +2UTx +2STy+T^2 &= 4d_1^2\left( (x-a_2)^2+(y-b_2)^2 \right) \\
\end{aligned}
$$

\begin{equation}
(U^2-4d^2)x^2+(S^2-4d^2)y^2 +2USxy+(2UT+8 d_1 a_2^2)x+(2ST+8 d_1 b_2^2)y +(T^2-4d_1a_2^2-4d_1b_2^2)=0 \label{general_form}
\end{equation}

所以，若$(a_1,b_1), (a_2,b_2)$是雙曲的兩個焦點, 然後曲線上到兩焦點絕對距離差是$d_1$,根據$\eqref{U},\eqref{S},\eqref{T}$定義下的$U,S,T$,
那麽它的一般式$A^2+Bxy+Cy^2+Dx+E+F=0$ 的係數是以下

$$

\begin{align}
A&=(U^2-4d^2) \label{A}\\
B&=2US \label{B}\\
C&=(S^2-4d^2)  \label{C}\\
D&=(2UT+8 d_1 a_2^2)  \label{D}\\
E&=(2ST+8 d_1 b_2^2) \label{E}\\
F&= (T^2-4d_1a_2^2-4d_1b_2^2) \label{F}\\
\end{align}
$$

令 fff



$$
\begin{aligned}
\label{rotation}
A(\theta) = \left(
\begin{matrix}
\cos(\theta) & -\sin(\theta)  \\
-\sin(\theta)  & \cos(\theta)  \\
\end{matrix} 
\right)
\end{aligned}
$$
和

$$
x=A(\theta) x'
$$

參考[旋轉後的係數]()




$$
\frac{x^2}{a^2}-\frac{y^2}{b^2}=1
$$