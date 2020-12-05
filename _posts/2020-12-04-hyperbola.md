---
title: '兩條雙曲線的交點'
date: 2020-12-04
permalink: /posts/2020/12/hyperbola/
tags:
  - hyperbola
category:
  - High School Math
---


## 求兩條雙曲線的交點
假設以下是兩條雙曲線,希望求出它們的交點<br>
$H_1$:設 $(a_1,b_1), (a_2,b_2)$是雙曲線的兩個焦點, 然後曲線上到兩焦點絕對距離差是$d_1$<br>
$H_2$:設 $(a_2,b_2), (a_3,b_3)$是雙曲線的兩個焦點, 然後曲線上到兩焦點絕對距離差是$d_2$

但因為計算繁複, 所以先假設以下特殊的雙曲線, 再推導到以述的一般情況

$$
\begin{align}
H_1 &: \frac{x'^2}{a^2}-\frac{y'^2}{b^2}=1 \label{H1}\\
H_2 &: A'^2x'^2+B'x'y'+C'y'^2+D'x'+E'y'+F'=0\label{H2}
\end{align}
$$



第一步是先聯立以上兩條方程會得出 

$$k_4y'^4+k_3y'^3+k_2y'^2+k_1y'+k_0=0,$$ 

只需要求出$k_4,k_3,k_2,k_1,k_0$就能透過一元四次求解公式得出$y'$,代回雙曲線方程求出$x'$,便能得到交點


$$
\begin{align}
\text{若令} \quad R&=\frac{A'(a^2)}{b^2}+C' \\
V&=F'+A'a^2\\
\text{則} \quad k_4&=R^2-\frac{a^2B'^2}{b^2}\\
k_3&=\frac{2E'R-2B'D'a^2}{b^2}\\
k_2&=E'^2+2R*V-\frac{(aD')^2}{b^2} -(aB')^2\\
k_1&=2E'V-2B'D'a^2\\
k_0&=V^2-D'^2a^2\\
\end{align}
$$


## 從焦點和距離差到一般式

因為題目已知是焦點和曲線上到兩焦點絕對距離差,但簡化的兩條曲線$\eqref{H1},\eqref{H2}$都是一般式$Ax^2+Bxy+Cy^2+Dx+Ey+F=0$。

所以先從已知焦點和曲線上到兩焦點絕對距離差求解出一般式的關係

設 $(a_1,b_1), (a_2,b_2)$是雙曲的兩個焦點, 然後曲線上到兩焦點絕對距離差是$d_1$
那麽, 假設原本的坐標是$x,y$

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
U&=2(a_2-a_1) \\
S&=2(b_2-b_1) \\
T&=a_1^2+b_1^2+d_1^2-a_2^2-b_2^2 
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

所以，若$(a_1,b_1), (a_2,b_2)$是雙曲的兩個焦點, 然後曲線上到兩焦點絕對距離差是$d_1$,
那麽它的一般式$A^2+Bxy+Cy^2+Dx+Ey+F=0$ 的係數是以下

$$
\begin{align}
\text{若令} \quad U&=2(a_2-a_1) \label{U}\\
S&=2(b_2-b_1) \label{S}\\
T&=a_1^2+b_1^2+d_1^2-a_2^2-b_2^2 \label{T} \\
\text{則} \quad A&=(U^2-4d_1^2) \label{A}\\
B&=2US \label{B}\\
C&=(S^2-4d_1^2)  \label{C}\\
D&=(2UT+8 d_1 a_2^2)  \label{D}\\
E&=(2ST+8 d_1 b_2^2) \label{E}\\
F&= (T^2-4d_1a_2^2-4d_1b_2^2) \label{F}\\
\end{align}
$$

## 由任意一般式$A^2+Bxy+Cy^2+Dx+Ey+F=0$,到典型的雙曲線$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$

現在, 從已知焦點和距離差,可根據$\eqref{A},\eqref{A},\eqref{B},\eqref{C},\eqref{D},\eqref{E},\eqref{F}$得出$H_1,H_2$的一般式

$$
\begin{align}
H_1 &: A_1^2x^2+B_1xy+C_1y^2+D_1x+E_1y+F_1=0 \label{H11}\\
H_2 &: A_2^2x^2+B_2xy+C_2y^2+D_2x+E_2y+F_2=0\label{H22}
\end{align}
$$

已經很$\eqref{H11},\eqref{H22}$接近$\eqref{H1},\eqref{H2}$,但與$\eqref{H11}$比較,$\eqref{H1}$是更簡化的情況, 所以考慮進一步簡化雙曲線$H_1$<br>

在直覺上,將雙曲線圖型反向平移兩焦點連線的中點, 再順時針旋轉一個角度$\theta$,就應該得到

$$
\frac{x'^2}{a^2}-\frac{y'^2}{b^2}=1
$$

這個$\theta$是甚麽?

$$
\begin{aligned}
\text{兩焦點斜率}&=\frac{a_1-a_2}{b_1-b_2} \\
\theta&=\text{arctan}(\text{兩焦點斜率})
\end{aligned}
$$

所以我們想得到$\eqref{H11} \rightarrow \eqref{H1}$是需要2個步驟
1. 平移
2. 順時針旋轉
   





## 兩條雙曲線同時平移旋轉


$H_1$:設 $(a_1,b_1), (a_2,b_2)$是雙曲線的兩個焦點, 然後曲線上到兩焦點絕對距離差是$d_1$<br>
$H_2$:設 $(a_2,b_2), (a_3,b_3)$是雙曲線的兩個焦點, 然後曲線上到兩焦點絕對距離差是$d_2$

令順時針旋轉$\theta$的矩陣是

$$
\begin{align}
\label{rotation}
A(\theta) = \left(
\begin{matrix}
\cos(\theta) & -\sin(\theta)  \\
\sin(\theta)  & \cos(\theta)  \\
\end{matrix} 
\right)
\end{align}
$$

令$(x,y)$平移後的坐標是$(x_m,y_m)$,$(x,y)$平移再旋轉後的坐標是$(x',y')$

$$
\begin{aligned}
H_1 &\rightarrow \text{平移}-(\frac{a_1+a_2}{2},\frac{b_1+b_2}{2}) &\rightarrow \text{順時針旋轉}\theta \\
\left(
\begin{matrix}
x  \\
y
\end{matrix} 
\right)  
&\rightarrow  
\left(
\begin{matrix}
x-\frac{a_1+a_2}{2}  \\
y-\frac{b_1+b_2}{2}  
\end{matrix} 
\right)  
=\left(
\begin{matrix}
x_m  \\
y_m
\end{matrix} 
\right)   
&\rightarrow 
A(\theta)
\left(
\begin{matrix}
x_m  \\
y_m
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

現在已找到$H_1$以$(x',y')$表示$\eqref{H1}$, 那麽$H_2$在同樣的平移旋轉以坐標$(x',y')$表示的一般式呢？

想像一下, $H_2$平移$-(\frac{a_1+a_2}{2},\frac{b_1+b_2}{2})$, 即是等價於<br>

$H_3:$焦點是$(a_2-\frac{a_1+a_2}{2},b_2-\frac{b_1+b_2}{2}),(a_3-\frac{a_1+a_2}{2},b_3-\frac{b_1+b_2}{2})$,距離差是$d_2$


$$
\begin{aligned}
H_2 &\rightarrow \text{平移}-(\frac{a_1+a_2}{2},\frac{b_1+b_2}{2}) &\rightarrow \text{順時針旋轉}\theta \\
H_3(\text{已經是坐標} (x_m,y_m)) &\rightarrow \text{順時針旋轉}\theta \\
H_3 &\rightarrow 
A(\theta)
\left(
\begin{matrix}
x_m  \\
y_m  \\
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


$H_3$以$x_m,y_m$表示的新的一般式可根據$\eqref{A},\eqref{B},\eqref{C},\eqref{D},\eqref{E},\eqref{F}$得出<br>
只要求出新的$H_3$以$x',y'$表示的新的一般式$A'^2x'^2+B'x'y'+C'y'^2+D'x'+E'y'+F'=0$即可

若使

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

則發現


$$
0=Ax_m^2+Bx_my_m+Cy_m^2+Dx_m+Ey_m+F=\overrightarrow{x_m^T}T\overrightarrow{x_m}
$$

$$
0=\overrightarrow{x_m^T} T \overrightarrow{x_m}=\overrightarrow{x'}^T (A(\theta))^T T A(\theta)\overrightarrow{x'}
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


現在我們終於可以從任意兩條雙曲線得到$\eqref{H1},\eqref{H2}$, 所以是可以求出以$(x',y')$的交點。

## 再次逆時針旋轉和平移得出真實交點
假設$\overrightarrow{x'_0}$是$H_1,H_2$以$(x',y')$表示的解


$$
\overrightarrow{x_{m,0}}=A(\theta)\overrightarrow{x'_0}
$$


$$
\begin{aligned}
\text{交點}&=\overrightarrow{x}\\
&=\overrightarrow{x_{m,0}}+\left(
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
