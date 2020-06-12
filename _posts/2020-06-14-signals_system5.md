---
title: '脈波調變'
date: 2020-06-14
permalink: /posts/2020/06/signals_systems5/
tags:
  - PAM
  - PCM
category:
  - Signals and Systems
---


# 參考
- 這是閱讀書本<[通訊原理與應用](http://findbook.tw/book/9789572122990/basic)>,作者藍國桐。

# 定義

- 在以下的過程當中，假設調變信號$s(t)$是

\begin{equation} \label{signal}
s(t)=A_m \cos(2\pi f_m t),
\end{equation} 

雖然是這樣定義，但經Fourier Series，任何週期波都可以表達成$\eqref{signal}$的和。它的[Fourier Transform](/posts/2020/06/signals_systems2/), 稱為頻譜或$S(t)=\mathcal{F}(s(t))$

- 在調變後的結果會以$\phi(t)$表示, 它的[Fourier Transform](/posts/2020/06/signals_systems2/), 稱為頻譜或$\Phi(t)=\mathcal{F}(\phi(t))$
- 解調後的信號會以$s_0(t)$表示
<hr>

# 取樣程序

## 理論上可利用$\delta (t-nT_s)$
\begin{equation}\label{ins_sampling}
s_{\text(int)}=\sum_{n=-\infty}^{\infty}s(t)\delta(t-nT_s)
\end{equation}

- 它的頻譜
  
\begin{equation}\label{ins_sampling_ft}
S_{\text(int)}(f)=\mathcal{F}(s_{\text(int)})=f_s\sum_{n=-\infty}^{\infty}S(f-nf_s)
\end{equation}

## 實際上可利用$p_T (t-nT_s)$

\begin{equation} \label{pT_fs}
p_T(t)=\sum_{n=-\infty}^{\infty}P_n \e^{jn2\p f_s t}
\end{equation}

其中 

$$
P_n=\frac{1}{T}\int_{\frac{-T_s}{2}}^{\frac{T_s}{2}}e^{-jn2\pi f_s t}dt=\frac{1}{n\pi}\sin(n\pi f_s\tau)=f_s\tau \frac{\sin(n\pi f_s \tau)}{n\pi f_s \tau}
$$

- 原信號$s(t)$取樣後$s_s(t)$為

$$
s_s(t)=s(t)p_{T}(t)=\sum_{n=-\infty}^{\infty}s(t)P_n e^{jn2\pi f_s t}
$$

- $s_s(t)$的頻譜$S_s(f)$

$$
S_s(f)=P_0 S(f)+\sum_{n=-\infty,n\neq 0 }^{\infty}P_n S(f-nf_s)
$$

其中$P_0=\frac{\tau}{T_s}$

# 取樣定理
以$s(t)$代表一頻寬有限的信號，並以$f_m$代表頻寬。如果隔$T_s$移取樣一次,只要

$$
f_s>2f_m
$$

就能從$s(nT_s)$取回原來的信號而不失真。


## PAM