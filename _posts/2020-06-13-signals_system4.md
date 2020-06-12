---
title: 'AM'
date: 2020-06-13
permalink: /posts/2020/06/signals_systems4/
tags:
  - AM
category:
  - Signals and Systems
---


# DSB_LC
- 用R-C電壓去檢測載波的包線-> $(1+Ka)s(t)$->$s(t)$
- 以下是載波$\phi_{AM}(t)$

\begin{equation} \label{am1}
\phi_{AM}(t)=A_c[1+K_a s(t)]cos(2\pi f_c t)\quad \text{where }fc \gg f_m \text{  and  }|K_a s(t)|<1
\end{equation}

- $m$是調變百分比

$$
\begin{align} 
m &=K_a A_m \quad \text{and by } \eqref{am1} \label{m_index_1}\\
\frac{\phi_{\max}}{\phi_{\min}}&=\frac{A_c(1+m)}{A_c(1-m)} \\
 m=\frac{\phi_{\max}+\phi_{\min}}{\phi_{\max}-\phi_{\min}} \label{m_index_2}
\end{align}
$$

$$
P=P_0+P_{USB}+P_{LSB}=P_C+frac{m^2}{4} P_C+frac{m^2}{4} P_C=(\1+frac{m^2}{2})P_C
$$

# DSB-SC

- 調變：載波$\phi_{DSB-SC}(t)$

\begin{equation} \label{shift1}
\phi_{DSB-SC}(t)=s(t)\cos(2\pi f_c t)
\end{equation}

- 乘以$cos(2\pi f_ct)$,頻譜會以$f_c,-f_c$為中心, 向左向右平移$f_m$,頻譜強度變為0.5, 表達式為以下
\begin{equation} \label{ft_shift1}
\Phi(f)=\frac{1}{2}(S(f-f_c)+f(f+f_c))
\end{equation}

## 解調

- 乘以$cos(2\pi f_c t)$得以下

$$
\phi_{DSB-SC}(t)\cos(2\pi f_c t)=\frac{1}{2}(s(t)+\cos(4\pi f_c t))
$$
