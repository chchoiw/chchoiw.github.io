---
title: '兩條雙曲線的交點'
date: 2020-12-04
permalink: /posts/2020/12/hyperbola/
tags:
  - hyperbola
category:
  - High School Math
---


## 從焦點和距離差到一般式
設 $(a_1,b_1), (a_2,b_2)$是雙曲的兩個焦點, 然後曲線上到兩焦點絕對距離差是$d_1$
那麽
$$
\begin{aligned}
\Bigg\vert \sqrt{(x-a_1)^2+(y-b_1)^2}-\sqrt{ (x-a_1)^2+(y-b_1)^2}\Big\vert & =d_1\\
\sqrt{(x-a_1)^2+(y-b_1)^2}&= \pm d_1 +\sqrt{(x-a_2)^2+(y-b_2)^2} \\
(x-a_1)^2+(y-b_1)^2 &= \left( \pm d_1 +\sqrt{(x-a_2)^2+(y-b_2)^2 } \right) ^2\\
2(a_2-a_1)x+2(b_2-b_1)y+a_1^2+b_1^2-d_1^2-a_2^2-b_2^2 &= d_1^2 +2d_1 \sqrt{(x-a_2)^2+(y-b_2)}
\end{aligned}
$$

若令

$$
\begin{align}
U&=2(a_2-a_1) \label{U}\\
S&=2(b_2-b_1) \label{S}\\
T&=a_1^2+b_1^2+d_1^2-a_2^2-b_2^2 \label{T}
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
(U^2-4d_1^2)x^2+(S^2-4d_1^2)y^2 +2USxy+(2UT+8 d_1 a_2^2)x+(2ST+8 d_1 b_2^2)y +(T^2-4d_1a_2^2-4d_1b_2^2)=0 \label{general_form}
\end{equation}

所以，若$(a_1,b_1), (a_2,b_2)$是雙曲的兩個焦點, 然後曲線上到兩焦點絕對距離差是$d_1$,根據$\eqref{U},\eqref{S},\eqref{T}$定義下的$U,S,T$,
那麽它的一般式$A^2+Bxy+Cy^2+Dx+Ey+F=0$ 的係數是以下

$$
\begin{align}
A&=(U^2-4d_1^2) \label{A}\\
B&=2US \label{B}\\
C&=(S^2-4d_1^2)  \label{C}\\
D&=(2UT+8 d_1 a_2^2)  \label{D}\\
E&=(2ST+8 d_1 b_2^2) \label{E}\\
F&= (T^2-4d_1a_2^2-4d_1b_2^2) \label{F}\\
\end{align}
$$

## 由任意一般式,到典型的雙曲線$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$

在直覺上,將雙曲線圖型反向平移兩焦點連線的中點, 再順時針旋轉一個角度$\theta$,就應該得到

$$
\frac{x^2}{a^2}-\frac{y^2}{b^2}=1
$$

這個$\theta$是甚麽?

$$
\begin{aligned}
\text{兩焦點斜率}&=\frac{a1-a2}{b1-b2} \\
\theta&=\text{arctan}(\text{兩焦點斜率})
\end{aligned}
$$


令順時針旋轉$\theta$的矩陣是

$$
\begin{align}
\label{rotation}
A(\theta) = \left(
\begin{matrix}
\cos(\theta) & -\sin(\theta)  \\
-\sin(\theta)  & \cos(\theta)  \\
\end{matrix} 
\right)
\end{align}
$$

## 兩條雙曲線同時平移旋轉


$H_1$:設 $(a_1,b_1), (a_2,b_2)$是雙曲線的兩個焦點, 然後曲線上到兩焦點絕對距離差是$d_1$<br>
$H_2$:設 $(a_2,b_2), (a_3,b_3)$是雙曲線的兩個焦點, 然後曲線上到兩焦點絕對距離差是$d_2$

$$
\begin{aligned}
H_1 &\rightarrow \text{平移}-(\frac{a_1+a_2}{2},\frac{b_1+b_2}{2}) &\rightarrow \text{順時針旋轉}\theta \\
\left(
\begin{matrix}
x_\text{orig}  \\
y_\text{orig} 
\end{matrix} 
\right)  
&\rightarrow  
\left(
\begin{matrix}
x_\text{orig}-\frac{a_1+a_2}{2}  \\
y_\text{orig}-\frac{b_1+b_2}{2}  
\end{matrix} 
\right)  
=\left(
\begin{matrix}
x  \\
y
\end{matrix} 
\right)   
&\rightarrow 
A(\theta)
\left(
\begin{matrix}
x  \\
y  
\end{matrix} 
\right)  
=
\left(
\begin{matrix}
x'  \\
y'  
\end{matrix} 
\right)
\end{aligned}
$$

那麽以$x',y'$表達$H_1$是

$$
\frac{x'^2}{a^2}-\frac{y'^2}{b^2}=1
$$

其中

$$
\begin{aligned}
c^2&=\frac{(a_1-a_2)^2+(b_1-b_2)^2 }{4}\\
a&=\frac{d_1}{2}\\
b&=\sqrt{c^2-a^2}
\end{aligned}
$$

現在已找到$H_1$以$(x',y')$表示的一般式, 那麽$H_2$呢？

想像一下, $H_2$平移$-(\frac{a_1+a_2}{2},\frac{b_1+b_2}{2})$, 即是等價於<br>
$H_3:$焦點是$(a_2-\frac{a_1+a_2}{2},b_2-\frac{b_1+b_2}{2}),(a_3-\frac{a_1+a_2}{2},b_3-\frac{b_1+b_2}{2})$,距離差是$d_2$


$$
\begin{aligned}
H_2 &\rightarrow \text{平移}-(\frac{a_1+a_2}{2},\frac{b_1+b_2}{2}) &\rightarrow \text{順時針旋轉}\theta \\
H_3 &\rightarrow \text{順時針旋轉}\theta \\
H_3 &\rightarrow 
A(\theta)
\left(
\begin{matrix}
x  \\
y  \\
\end{matrix} 
\right)  
=
\left(
\begin{matrix}
x'  \\
y'  \\
\end{matrix} 
\right)
\end{aligned}
$$


$H_3$以$x,y$表示的新的一般式$A^2x^2+Bxy+Cy^2+Dx+Ey+F=0$可根據$\eqref{A},\eqref{B},\eqref{C},\eqref{D},\eqref{E},\eqref{F}$得出
只要求出新的$H_3$以$x',y'$表示的新的一般式$A'^2x'^2+B'x'y'+C'y'^2+D'x'+E'y'+F'=0$即可


因為
$$
\begin{aligned}
T=\left(
\begin{matrix}
A &\frac{B}{2} &\frac{D}{2} \\
\frac{B}{2} & C&\frac{E}{2} \\
\frac{D}{2}  &\frac{E}{2}&F
\end{matrix} 
\right)
\end{aligned}
$$

可將


$$
0=A^2+Bxy+Cy^2+Dx+Ey+F=\overrightarrow{x^T}T\overrightarrow{x}
$$

$$
0=\overrightarrow{x^T} T \overrightarrow{x}=\overrightarrow{x'}^T (A(\theta))^T T A(\theta)\overrightarrow{x'}
$$



那麽得出

$$
\begin{aligned}
(A(\theta))^T T A(\theta)=\left(
\begin{matrix}
A' &\frac{B'}{2} &\frac{D'}{2} \\
\frac{B'}{2} & C'&\frac{E'}{2} \\
\frac{D'}{2}  &\frac{E'}{2}&F'
\end{matrix} 
\right)
\end{aligned}
$$



## 求交點
$$
\begin{aligned}
H_1 &: \frac{x'^2}{a^2}-\frac{y'^2}{b^2}=1 \\
H_2 &: A'^2x'^2+B'x'y'+C'y'^2+D'x'+E'y'+F'=0
\end{aligned}
$$

會得出 $a_4y^4+a_3y^3+a_2y^2+a_1y^1+a_0=0$, 只需要求出$k_4,k_3,k_2,k_1,k_0$就能透過四次求解公式得出交點

$$
\begin{align}
R&=\frac{A'(a^2)}{b^2}+C' \\
V&=F'+A'a^2\\
k_4&=R^2-\frac{a^2B'^2}{b^2}\\
k_3&=\frac{2E'R-2B'D'a^2}{b^2}\\
k_2&=E'^2+2R*V-\frac{(aD')^2}{b^2} -(aB')^2\\
k_1&=2E'V-2B'D'a^2\\
k_0&=V^2-D'^2a^2\\
\end{align}
$$

## 再次逆時針旋轉和平移得出真實交點
假設$\overrightarrow{x'_0}$是$H_1,H_2$以$(x',y')$表示的解


$$
\overrightarrow{x_0}=A(\theta)\overrightarrow{x'_0}
$$


$$
\begin{aligned}
\text{交點}&=\overrightarrow{x_0}+\left(
\begin{matrix}
\frac{a_1+a_2}{2} \\
\frac{b_1+b_2}{2} 
\end{matrix} 
\right)\\
&=A(\theta)\overrightarrow{x'_0}+\left(
\begin{matrix}
\frac{a_1+a_2}{2} \\
\frac{b_1+b_2}{2} 
\end{matrix} 
\right)
\end{aligned}
$$
