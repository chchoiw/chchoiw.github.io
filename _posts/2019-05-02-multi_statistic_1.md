---
title: 'Likelihood'
date: 2019-05-02
permalink: /posts/2019/05/likelihood/
tags:
  - Likelihood
category:
  - Statistic
---
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

* [應用多元統計分析-1:Likelihood](#應用多元統計分析-1likelihood)
	* [似然的含義](#似然的含義)
	* [定義 $Vec(X')$](#定義-vecx)
	* [似然函數的最大值估計](#似然函數的最大值估計)
	* [無偏性](#無偏性)

<!-- /code_chunk_output -->



# 應用多元統計分析-1:Likelihood

> 主要是跟著書本<<應用多元統計分析>> 高惠璇 編著
<div class="separator" style="clear: both; text-align: center;">
<a href="https://4.bp.blogspot.com/-0c3BIEOjlJs/XMpxGqrHK7I/AAAAAAAAABY/-wCerGKfJrIKsGipLpfSjp-cYVXiigL2ACLcBGAs/s1600/51irGh3KldL._SX344_BO1%252C204%252C203%252C200_.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="499" data-original-width="346" height="320" src="https://4.bp.blogspot.com/-0c3BIEOjlJs/XMpxGqrHK7I/AAAAAAAAABY/-wCerGKfJrIKsGipLpfSjp-cYVXiigL2ACLcBGAs/s320/51irGh3KldL._SX344_BO1%252C204%252C203%252C200_.jpg" width="221" /></a></div>

## 似然的含義
因為經常在處理數據時，我們不知道它的平均值和方差，似然就是利用數據樣本去估計它的平均值和方差，使得**得出樣本數據的機率最大**。

另外，有關似然的更多解釋請到 [link](https://wangcc.me/LSHTMlearningnote/likelihood-definition.html)。

假設 $X_{(i)}'$是 $p$ 元正態總$N(\mu,\Sigma )$，
令 

$$
 X=\left[ \begin{matrix}
   X_{(1)}' \\
   X_{(2)}' \\
   \vdots  \\
   X_{(n)}'
  \end{matrix} \right]\tag{1}
$$

為樣本矩陣。


## 定義 $Vec(X')$
若定義

$$
Vec(X')=
\left[ \begin{matrix}
   X_{(1)} \\
   X_{(2)} \\
   \vdots  \\
   X_{(n)}
  \end{matrix} \right]      \tag{2}
 $$

那麽

$$
Vec(X') =
N_{np}(1_n \otimes \mu, I_n \otimes \Sigma)
$$

- $Vec(X')$ 其實就是將每一橫列拉直為一個 $np$向量
- 為什麽要定義 $Vec(X')$ 使其複雜？
    因為$X'$本來就是一個樣本矩陣，在求似然的最大值時，本能地將矩陣看向為$np$維的向量，再去微分求最大值。

- 因為定義了 $Vec(X')$，所以才有以下等式
    令$f$為聯合密度函數，$L$為似然函數 

    $$L(\mu,\Sigma|X')=f(Vec(X')|1_n \otimes \mu,I_n \otimes \Sigma)=\prod_{i=1}^nf(x_i| \mu)$$

    即不同的$f(x_i\vert\theta)$能獨立地相乘，都是因為定義了$Vec(X')$，使得相對應的 $ 1_n \otimes \mu$ 和 $I_n \otimes \Sigma$，然後運算過程中能拆成 $\prod_{i=1}^nf(x_i\vert \mu)$

## 似然函數的最大值估計

$$\hat{\mu}=\bar{X},\hat{\Sigma}=\frac{1}{n}A $$

其中

$$
A=\sum_{i=1}^n (X_i-\bar{X})(X_i-\bar{X})'
$$


## 無偏性

$$E(\bar{X})=\mu$$

$$E(A)=(n-1)\Sigma$$