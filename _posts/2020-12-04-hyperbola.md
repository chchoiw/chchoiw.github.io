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
\Vert \sqrt((x-a_1)^2+(y-b_1)^2)-\sqrt((x-a_1)^2+(y-b_1)^2)\Vert & =d_1\\
\sqrt((x-a_1)^2+(y-b_1)^2)&= \pm d +\sqrt((x-a_2)^2+(y-b_2)^2) \\
(x-a_1)^2+(y-b_1)^2 &= (\pm d +\sqrt((x-a_2)^2+(y-b_2)^2) ) ^2\\
2(a_2-a_1)x+2(b_2-b_1)y+a_1^2+b_1^2d_1^2-a_2^2-b_2^2 &= d_1^2 +2d \sqrt((x-a_2)^2+(y-b_2))
\end{aligned}
$$

若令

$$
\begin{aligned}
U&=2(a_2-a_1) \\
S&=2(b_2-b_1) \\
T&=a_1^2+b_1^2d_1^2-a_2^2-b_2^2
\end{aligned}
$$


$$
\begin{aligned}
(Ux+Sy+T) &= 2d_1 \sqrt((x-a_2)^2+(y-b_2)) \\
(Ux+Sy+T)^2 &= ( 2d_1 \sqrt((x-a_2)^2+(y-b_2)^2 ) )^2 \\
U^2x^2+S^2y^2 +T^2+2USxy +2UTx +2STy+T^2 &= 4d_1^2\left( (x-a_2)^2+(y-b_2)^2 \right)
(U^2-4d^2)x^2+(S^2-4d^2)y^2 +2USxy+(2UT+8 d_1 a_2^2)x+(2ST+8 d_1 b_2^2)y +(T^2-4d_1a_2^2-4d_1b_2^2)=0
\end{aligned}
$$

$$
\frac{x^2}{a^2}-\frac{y^2}{b^2}=1
$$