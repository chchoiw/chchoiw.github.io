---
title: 'Markov Chain'
date: 2023-06-07
permalink: /posts/2024/09/markov_chain
tags:
  - Markov Chain, 
category:
  - Statistic
---

## Markov Chain

$$
P(X_n=x_n|X_{n-1}=x_{n-1},\dots,X_{1}=x_1)=P(X_n=x_n|X_{n-1}=x_{n-1})
$$


## C-K formular



## Reachable
- when $i,j$ is reachable, there exists $n$ such that $P_{i,j}(n)>0$, i.e.  $i \leftarrow j$


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
\begin{equation}
P_{i,j}(z)&=\delta_{i,j}+f_{i,j}(z)P_{j,j}(z)
\end{equation}

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

$$\sum_{n}n f_{j,j}(n) \le \infty
$$

- null recurrent:

$$\sum_{n}n f_{j,j}(n) = \infty
$$

$$d_i=gcd{k|P_{i,i}(k)>0}$$


## stable converage
- if finite state Diagram D is irreducible and non-perodic, then 
$$
P_{i,j}(n) \rightarrow \pi{i,j}
$$

- if finite states Diagram D is irreducibe and recurrent, then 

$$
lim_{n\rightarrow \infity}\sum_{k=1}^n\frac{1}{k}P_{i,j}(k) \rightarrow \hat \pi_{i,j}
$$






