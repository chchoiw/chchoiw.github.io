---
title: 'AM'
date: 2020-06-13
permalink: /posts/2020/06/signals_systems4/
tags:
  - AM
category:
  - Signals and Systems
---

\begin{equation} \label{shift1}
\phi(t)=s(t)cos(2\pi f_ct)
\end{equation}


\begin{equation} \label{ft_shift1}
\phi(f)=\frac{1}{2}(S(f-f_c)+f(f+f_c))
\end{equation}

\begin{equation} \label{am1}
\phi_{AM}(t)=A_c[1+K_a s(t)]cos(2\pi f_c t)\quad \text{where }fc \gg f_m \text{  and  }|K_a s(t)|<1
\end{equation}

$$
\begin{align} 
m &=K_a A_m \quad \text{and by } \eqref{am1} \label{m_index_1}\\
\frac{\phi_{\max}}{\phi_{\min}}&=\frac{A_c(1+m)}{A_c(1-m)} \\
 m=\frac{\phi_{\max}+\phi_{\min}}{\phi_{\max}-\phi_{\min}} \label{m_index_2}
\end{align}
$$