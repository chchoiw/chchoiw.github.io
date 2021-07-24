---
title: '正態分佈、獨立性和方差齊次性檢驗'
date: 2019-06-19
permalink: /posts/2019/06/normal_independ_cvar/
tags:
  - 正態分佈檢驗
  - 獨立性檢驗
  - 方差齊次性檢驗
category:
  - Statistic
---

- [正態分佈檢驗](#%e6%ad%a3%e6%85%8b%e5%88%86%e4%bd%88%e6%aa%a2%e9%a9%97)
  - [經驗分布函數](#%e7%b6%93%e9%a9%97%e5%88%86%e5%b8%83%e5%87%bd%e6%95%b8)
  - [Shapiro-Wilk](#shapiro-wilk)
  - [Kolmogorov-Smirnov](#kolmogorov-smirnov)
  - [Cramer-von Mises](#cramer-von-mises)
  - [Anderson-Darling](#anderson-darling)
  - [Q-Q圖](#q-q%e5%9c%96)
- [獨立性檢驗](#%e7%8d%a8%e7%ab%8b%e6%80%a7%e6%aa%a2%e9%a9%97)
  - [Durbin -Watson Test](#durbin--watson-test)
- [方差齊次性檢驗](#%e6%96%b9%e5%b7%ae%e9%bd%8a%e6%ac%a1%e6%80%a7%e6%aa%a2%e9%a9%97)
  - [Bartlett檢驗](#bartlett%e6%aa%a2%e9%a9%97)

# 正態分佈檢驗

## 經驗分布函數

$$
\begin{aligned}
\hat F_n(t) &=\frac{\text{number of elements in the sample}<t}{n} \\
&= \frac{1}{n} \sum_{i=1}^n 1_{x_i<t}
\end{aligned}
$$

## Shapiro-Wilk
Reference:
* Wiki: [link](https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test)
* Another academic pdf [link](https://math.mit.edu/~rmd/465/shapiro.pdf)

$$
W=\frac{(\sum a_i x_{(i)})^2}{\sum(x_i-\bar x)^2}
$$

其中，
- $x_{(i)}$是從小到大排序後第$i$項
-  ${Z_1, \cdots, Z_n}$ be i.i.d. $N(0, 1)$ and also take their order statistics $Z_{(1)}<\cdots<Z_{(n)} $
- $m_i$是$E(Z_{(i)})$
- $V$ 是 covariance of $Z_{(i)},Z_{(j)}$,即$V_{ij} = E[(Z_{(i)} −m_i)(Z_{(j)} − m_j )]$
-  $C := (m'V^{−1}V^{−1}m)^{1/2}$
- $a=\frac{m'V^{-1}}{C}$

通常$W$越大，越接近正態分布
$H_0: X \text{ is normal distribution}$
當 $W<W_\alpha$ 或者 $p < 1-\alpha $ 時，否定$H_0$

## Kolmogorov-Smirnov

$$
D=\text{Sup}| F_n(x)-F_0(x)|
$$

## Cramer-von Mises

$$
W^2=n \int_{-\infty}^{+\infty}(F_n(x)-F_0(x))^2dF_0(x)
$$

## Anderson-Darling

$$
A^2=n \int_{-\infty}^{+\infty}(F_n(x)-F_0(x))^2[F_0(x)(1-F_0(x))]^{-1}dF_0(x)
$$

## Q-Q圖
繪制散點$(q_i,x^*_{(i)})$的散布圖，其中

$$
\begin{aligned}
q_i &=\Phi^{-1}(p_i) \\
p_i &=\frac{i-0.5}{n}
\end{aligned}
$$

為正態總體的$p_i$分位數。
> 這些點應散布在一條$y=x$附近上。


# 獨立性檢驗
## Durbin -Watson Test
- [simple example](https://www.investopedia.com/terms/d/durbin-watson-statistic.asp)
- [wiki]()

$$
d=\frac{\sum_{t=2}^T (e_t-e_{t-1})^2}{\sum_{t=1}^T e^2_t}
$$

$$H_0  :e_t= ae_{t-1}+v_t, a=0$$

Since $d$ is approximately equal to

$$ 2(1 −  \hat {\rho }),$$

where $\hat {\rho }$  is the sample autocorrelation of the residuals, $d = 2$ indicates no autocorrelation.

A rule of thumb is that test statistic values in the **range of 1.5 to 2.5** are relatively normal.

# 方差齊次性檢驗
## Bartlett檢驗

$$
\begin{aligned}
s_i^2 &=\frac{1}{m_i-1} \sum_{j=1}^{m_i} (y_{ij}- \bar y_i)^2=\frac{Q_i}{f_i} \\
f_e&=f_1+f_2+\cdots+f_r=\sum_{i=1}^r(m_i-1) \\
\text{MS}_e &=\frac{1}{f_e}\sum_{i=1}^r Q_i=\sum_{i=1}^r \frac{f_i}{f_e}s_i^2\\
\text{GMS}_e &=[(s_1^2)^{f_1} (s_2^2)^{f_2} \cdots (s_r^2)^{f_r}]^{\frac{1}{f_e}}\\
\text{MS}_e &\geq\text{GMS}_e \\
C&=1+\frac{1}{3(r-1)}[\sum_{i=1}^r \frac{1}{f_i}-\frac{1}{f_e}]\\
B &=\frac{f_e}{C}( \text{ln MS}_e - \text{ln GMS}_e)
\end{aligned}
$$

拒絕域為: 

$$W=\{B \geq \chi_{(1-\alpha)}^2(r-1)\}$$