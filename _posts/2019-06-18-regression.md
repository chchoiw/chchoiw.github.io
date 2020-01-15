---
title: 'Regression'
date: 2019-04-26
permalink: /posts/2019/04/regression/
tags:
  - regression
category:
  - Statistic
---

# 一元簡單線性迴歸
令 
$$
\hat y_i=\beta_0-\beta_i x_i
$$
最小二法是選出$\beta_0,\beta_1$使得$Q$最小。

$$
Q=\sum_{i=1}^n (y_i -\hat y_i)^2=\sum_{i=1}^n (y_i -\beta_0-\beta_i x_i)^2
$$

通常采用偏微$ \frac{\partial Q}{\partial \beta_0},\frac{\partial Q}{\partial \beta_1}=0$ 計算出$\beta_0,\beta_1$，

$$
\left\{
    \begin{array}{lr}
    \hat \beta_1=\frac{l_{xy}}{l_{xx}}
    \\
    \hat \beta_0=\bar y - \hat \beta_1 \bar x 
    \end{array} 
\right.
$$

其中，

$$
\begin{aligned}
l_{xy} &=\sum(x_i -\bar x)(y_i-\bar y) = \sum x_iy_i- n \bar x \bar y =\sum x_iy_i- \frac{1}{n} \sum x_i \sum y_i \\
l_{xx} &=\sum(x_i -\bar x)^2 =\sum x_i^2 -n\bar x^2 =\sum x_i^2- \frac{1}{n} \left(\sum x_i \right) ^2
\\
l_{yy} &=\sum(y_i -\bar y)^2 =\sum y_i^2 -n\bar y^2 =\sum x_i^2- \frac{1}{n} \left(\sum y_i \right) ^2
\end{aligned}
$$

其中改寫$\beta_0,\beta_1$
$$
\begin{aligned}
\hat \beta_1 &=\sum \left( \frac{x_i-\bar x}{l_{xx}}\right)y_i \\
\hat \beta_0 &=\bar y -\hat \beta_i \bar x=\sum \left[\frac{1}{n} -\frac{(x_i-\bar x)\bar x}{l_{xx}}\right]y_i
\end{aligned}
$$


而進行簡單的計算得出：
- $E(\hat \beta_0)$
- $E(\hat \beta_1)$
- $\text{Var}( \hat \beta_0)$
- $\text{Var}(\hat \beta_1)$
- $\text{Cov}(\hat \beta_0,\hat \beta_1)$


# 多元線性迴歸
$$
C = 
\begin{bmatrix} 
1 & x_{11} & x_{12}  &\cdots & x_{1m}\\
1 & x_{21} & x_{22}  &\cdots & x_{2m} \\
\vdots & \vdots & \vdots &\cdots & \vdots\\
1 & x_{n1} & x_{n2}  &\cdots & x_{nm}
\end{bmatrix}
$$

$$
y =
\begin{bmatrix} 
y_1 \\
y_2 \\
\vdots \\
y_n
\end{bmatrix},
\beta =
\begin{bmatrix} 
\beta_0 \\
\beta_1 \\
\vdots \\
\beta_m
\end{bmatrix},
\varepsilon =
\begin{bmatrix} 
\varepsilon_0 \\
\varepsilon_1 \\
\vdots \\
\varepsilon_n
\end{bmatrix}
$$

$$Y=C\beta+\varepsilon $$

## 最小二乘法
## $\beta$的估計
$$
Q(\beta)=\sum_{t=1}^n \varepsilon_t^2=\sum_{t=1}^n( y_t - \hat y_t)^2=\sum_{t=1}^n[ y_t - (\beta_0+\beta_1 x_{t1}+\cdots+\beta_mx_{tm})]^2
$$

**最小二乘法是**取$\beta_i$使得$Q$達到最小。
從這個方法可得出以下結果
$$
\begin{aligned}
\widehat{\beta} &=(C'C)^{-1}C'Y \\
\hat Y &=C\widehat{\beta}=C(C'C)^{-1}C'Y \\
\hat \varepsilon &=Y-\hat Y \\
Q(\hat \beta) &= \hat \varepsilon' \varepsilon
\end{aligned}
$$

## $\hat \sigma$的估計
利用最大似然原理，仍可得出$\beta$最大似然估計仍為$\hat \beta$,$\sigma$的估計是

$$\hat \sigma^2=\frac{1}{n}\sum_{t=1}^n[ y_t - (\beta_0+\beta_1 x_{t1}+\cdots+\beta_mx_{tm})]^2=\frac{1}{n}Q(\beta)$$

但因$\hat \sigma$不是無偏估計量，通常取
$$
s^2=\frac{1}{n-m-1}Q(\beta)
$$

## 殘差

$$
\begin{aligned}
Q &=(Y-\hat Y)'(Y-\hat Y)=\sum(y_i-\hat y_i)^2 \\
U &=(\bar Y-\hat Y)'(\bar Y-\hat Y)=\sum(\hat y_i-\bar y_i)^2 \\
E(y) &= (Y-\bar Y)'(Y-\bar Y)=\sum( y_i-\bar y_i)^2=U+Q
\end{aligned}
$$
其中
- $U$為所建立迴歸式的$X$所引起
- $Q$為隨機誤差所引起

## 殘差檢定

1. 常態分配
2. 獨立性
3. 變異數同質性

這個請參閱另一篇[BLOG]()
## 離群值檢定
- 標準化殘差


## 回歸方程的顯著性檢驗

已知：
$$
\begin{aligned}
\hat \beta &\sim \beta N_{m+1}(\beta,\sigma^2(C'C)^{-1})\\
\frac{1}{\sigma^2} Q &\sim \chi_{n-m-1}^2
\end{aligned}
$$
$H_0 :\beta_1=\beta_2=\cdots=\beta_n=0$

在已知$H_0$下，
$$
\frac{1}{\sigma^2} U \sim \chi_{m}^2
$$
所以，
$$
F=\frac{U/m}{Q/n-m-1}
$$

如果

$
F >F_\alpha \text{ or } p <\alpha
$，則否定$H_0$。


## 額外平方和
> 這是台灣考題中經常出現，未必有需要，但對厘清概念是非常好的。

假設$Q_i,U_i$表示去掉自變量$x_i$後的各自定義的殘差平方和。
$P_i=U-U(i)=Q(i)-Q$

在台灣的定義中，
$\text{SSR}=U,\quad \text{SSE}=Q$
$$
\begin{aligned}
\text{SSR}(x_1| x_2,x_3) 
&=\text{SSR}(x_1 ,x_2,x_3)-\text{SSR}(x_1,x_2) \\
&=\text{SSE}(x_1,x_2)-\text{SSE}(x_1 ,x_2,x_3)
\\
\text{SSR}(x_1, x_2|x_3) 
&=\text{SSR}(x_1 ,x_2,x_3)-\text{SSR}(x_3) \\
&=\text{SSE}(x_3)-\text{SSE}(x_1 ,x_2,x_3)
\end{aligned}
$$
有關更詳細的資料，請參閱 [link](http://web.ncyu.edu.tw/~lanjc/lesson/C7/class/ch07-AN.pdf)。

## 判定係數
$$R^2=1-\frac{Q}{U+Q}=\frac{U}{T}$$
這裏 $T=U+Q=\sum(y_i-\bar y_i)^2$ 是總偏差平方和。
- 判定係數$R$的分子$U$為所建立迴歸式的$X$所引起
- $R$越大，即$X$能解釋$Y$的能力越強

## 修定判定係數
$$R^2_{\text{adj}}=1-\frac{Q/\text{df}Q}{T/\text{df}T}$$
這裏 $\text{df}Q,\text{df}T$分別是$Q$和$T$的自由度。

這主要是修正因樣本量太小而變大的$R$。



## 標準化後的$\beta$
>受到不同尺度衡量的影響，由標準化的自變數所計算而得到的迴歸係數，我們稱為$\beta$係數 (beta 係數)，擁有$\beta$係數愈高的自變數($x_n$)，對依變數(Y)的影響力愈大。

 ref:[link](http://www.gotop.com.tw/epaper/e0719/AEM000900n.pdf)

## 方差膨脹因子
- 容忍度：$1-R_i=\frac{Q}{T}$表示以其它自變數來預測第$i$個自變數之決定係數。
- 當容忍度愈小時表示$R_i$愈大 ，即其他$\{ x_j \vert j\neq i \} $能解釋$x_i$的能力愈大。
- 方差膨脹因子$\text{VIF}=\frac{1}{1-R_i}$，與$R_i$成正比。$\text{VIF}>10$時，為顯著共線性。


## 共線性問題
- 檢查方法
1. 檢查看相關係數，超過 0.8 就已經太高了，可能有共線性問題
2. 查看容忍值(tolerance)，容忍值( 0~1 之間)，愈大愈好，容忍值愈大，代表共線性問題愈小
3. 變異數膨脹因素(VIF)，VIF 的值愈小愈好，代表愈没有共線性問題。

- 消除共線性的方法：
1. 從彼此相關係數較高的自變數中只取一個重要的變項
2. 使用脊迴歸（ridge regression）分析
3. 用主成份迴歸

## 偏判定係數
在已知$x_1,x_2$的情況下，引入$x_3$，其判定係數的定義是
$$R^2_{x_3|x_1,x_2}=\frac{\text{SSR}(x_3|x_1,x_2)}{\text{SSE}(x_1,x_2)} $$
分子可以想像為因為引入$x_3$而造成殘差增加量，分母就是只有$x_1,x_2$的殘差。
這個比就是增加量和原本相比，它增加的幅度。

## 回歸系數的顯著性檢驗
$$H^{(i)}_0:\beta_i=0 \quad (i=1,2,\cdots,m)$$
在$H_0$下，

$$
\begin{aligned}
F_i &=\frac{P_i}{Q/n-m-1} \sim F(1,n-m-1), \\
T_i &=\frac{ \sqrt{P_i} }{\sqrt{Q/(n-m-1)}} \sim t(n-m-1)
\end{aligned}
$$

如果 $
F >F_\alpha \quad \text{ or } \quad p=\{F>F_\alpha\} <\alpha
$，則否定$H_0$。