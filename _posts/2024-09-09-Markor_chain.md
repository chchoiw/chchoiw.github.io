---
title: 'Stochastic Processs'
date: 2024-09-09
permalink: /posts/2024/09/stochastic_process
tags:
  - Stochastic Process, Markov Chain, Possion Process
category:
  - Statistic
---





# Possion Process

The stochastic countng satifies the following conditions is defined as Possion Process
- $N(0) = 0$
- $N(t)$ is indepentent increment process


$$ (X_{t_1}-_{t_0}),\dots,(X_{t_{n+1}}-_{t_n})$$ are indepentent


- $N(t)$ is statoinary increment process

$$(X_{t_1}-_{t_0}) \sim \text{Pission}(\lambda)$$



Using Generating function $G(z,t)=E(z^(N(t)))=sum_k z^k P(N(t)=k)$ to find that possion process is 

$$P(N(t) = k) = \frac{(\lambda t)^k}{k!} \exp{-\lambda t}$$



# Markov Process

- [interveiw questions 1](https://www.robots.ox.ac.uk/~lsgs/posts/2020-12-13-recursion-markov.html)
- [interview questions 2](https://analyticsarora.com/9-unique-machine-learning-interview-questions-on-markov-chains/)
- [Markov notes](https://blog.csdn.net/weixin_45768147/article/details/131738269?spm=1001.2014.3001.5502)
- [Markov videos](https://www.bilibili.com/video/BV11b421E7nh/?spm_id_from=333.999.0.0&vd_source=1e739a4b8bd8d83d5b7daf376a61bdf3)
- [Markov videos(easier)](https://www.bilibili.com/video/BV1Kt4y1C7Z7/?spm_id_from=333.337.search-card.all.click)

$$
P(X_n=x_n|X_{n-1}=x_{n-1},\dots,X_{1}=x_1)=P(X_n=x_n|X_{n-1}=x_{n-1})
$$


## Chapman–Kolmogorov equation

$$
P_{i,j}(n)=\sum_k P_{i,k}(n) P_{k,j}(n) 
$$



## Reachable
- when $i,j$ is reachable, there exists $n$ such that $P_{i,j}(n)>0$, i.e.  $i \rightarrow j$


## Commutative
- $i \leftrightarrow j$ that means $i \rightarrow j$ and $j \rightarrow i$

## Closed
- a set $S$ is defined as closed if a subset $C$ of $S$, $a \in C$, $b \notin C$ , which imples $a \not\to b$

## Irreducible
- a set $S$ is irreducible if $S$ do not include closed true subset $C$ 
- iff $S$ is closed and all elements in S is commutative


## First passaege Proability

$$ f_{i,j}(n)=P(X_n=j,X_{n-1}\not= j,\dots, X_1\not=j|X_{n-1}=i)$$

$$ 0\le \sum_{n} f_{i,j}(n) \le 1$$

## Recurrent
$$\sum_{n} f_{i,j}(n) =1$$

or

$$\sum_{n} P_{i,j}(n)=\infty$$


- the proof is using 

$$ 
P_{i,j}(z)=\delta_{i,j}+f_{i,j}(z)P_{j,j}(z)
$$

$$
P_{i,i}(z)=\frac{1}{1-F_{i,j}(z)} 
$$

where 


$$P_{i,j}(z)=\sum_{n}P_{i,j}(n)z^n$$

- finite state has an elemnent which is recurrent
- irreducibe with finite state implies all states are recurrent

## Periodic

- irreducible and recurrent, the following holds.

$$
\frac{1}{n}\sum_{k=1}^n P_{i,j}(k)=\frac{1}{\sum_{n}n f_{j,j}(n)}
$$

- positive recurrent:

$$\sum_{n}n f_{j,j}(n) < \infty
$$

- null recurrent:

$$\sum_{n}n f_{j,j}(n) = \infty
$$

- when $d_i=1$, the diagram is non-periodic

$$d_i=gcd\{k|P_{i,i}(k)>0\}$$



## stable converage
- if finite state Diagram D is irreducible and non-perodic, then 
$$
P_{i,j}(n) \rightarrow \pi_{i,j}
$$

- if finite states Diagram D is irreducibe and recurrent, then 

$$
lim_{n\rightarrow \infty}\sum_{k=1}^n\frac{1}{k}P_{i,j}(k) \rightarrow \hat \pi_{i,j}
$$






