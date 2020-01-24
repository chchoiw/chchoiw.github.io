---
title: 'Perceptron Algorithm'
date: 2019-09-24
permalink: /posts/2019/09/perceptron_alg/
tags:
  - Perceptron Algorithm
category:
  - Machine Learning
---
- [Perceptron Algorithm](#Perceptron-Algorithm)
- [Binary Classification Problem](#Binary-Classification-Problem)
- [Perceptron Algorithm (Primal From)](#Perceptron-Algorithm-Primal-From)
- [Stop in Finite steps](#Stop-in-Finite-steps)
- [Perceptron Algorithm(Dual Form)](#Perceptron-AlgorithmDual-Form)
- [Python Code](#Python-Code)

# Perceptron Algorithm
- Basically, this is my studying from [NTCU open course](http://ocw.nctu.edu.tw/index.php) - [Machine Learning](http://ocw.nctu.edu.tw/course_detail.php?bgid=1&gid=1&nid=563&page=1). I will take the key points for my references.


# Binary Classification Problem

Given a training dataset

$$
S=\{(x_i,y_i) | x_i \in \mathbb{R}^n,  y_i \in {-1,1,i=1,2,\dots,l} \}
$$

$$
\begin{aligned}
x_i  \in A_{+} & \Longleftrightarrow y_i=1 \\
x_i  \in A_{-} & \Longleftrightarrow y_i=-1
\end{aligned}
$$

Main Goal
- Predit the unseen class label for new data
- Find a function $f:\mathbb{R}_n \rightarrow \mathbb{R}$ by learning from data such that

$$
\begin{aligned}
f(x) \geq 0  & \Longleftrightarrow x  \in A_{+} \\
f(x) \geq 0  & \Longleftrightarrow x  \in A_{-}
\end{aligned}
$$

Here the simplest function is linear 

$$
f(x)=w^{T}x+b
$$

# Perceptron Algorithm (Primal From)
An on-line and mistake-driven produce 

***Repeat***
<br>
***for*** i =1 to l 
<br>
***if*** $y_i(\langle w_{k},x_i \rangle +b_k) \leq 0$, then 

$$
\begin{aligned}
w_{k+1}  &\leftarrow  w_{k} +\eta y_ix_i\\
b_{k+1}  &\leftarrow  b_{k}  +\eta y_iR^2 \\
k & \leftarrow k+1
\end{aligned}
$$

***end if***
<br>
***Until*** no mistakes made within the for loop 
<br>
***return***: $k,(w_k,b_k)$

***Remark***:

$$
y_i(\langle w_{k+1},x_i \rangle +b_{k+1})=
y_i(\langle w_{k},x_i \rangle +b_{k})+\eta(\langle x_{i},x_i \rangle +R^2)
$$

# Stop in Finite steps
Theorem(Novikoff)
Let $S$ be a non-trival training set, and let

$$
R=\max\limits_{1\leq i \leq l} \Vert x_i\Vert
$$

Suppose that there exists a vector $\omega_{opt}$ such that $\Vert \omega_{opt} \Vert =1 $ and 

$$
y_i(\langle w_{opt},x_i \rangle +b_{opt}) \geq r \quad \text{for} \quad 1\leq i \leq l 
$$

The number of mistakes made by the on-line perceptron algorithm on $S$ is almost $\left(\frac{2R}{r}\right)^2$


Remark:
- the value of $\eta$ is irreverent.

# Perceptron Algorithm(Dual Form)

$$ 
w_i=\sum\limits_{i=1}^l \alpha_i y_i x_i
$$

Given a linearly seperable training set $S$ and $\alpha=0$, $\alpha \in \mathbb{R}^l$, $b=0$ and $R=\max\limits_{1\leq i \leq l }\Vert x_i \Vert$

$$
y_i(\langle w_{k},x_i \rangle +b_{k})=y_i\left(\sum\limits_{i=1}^l \alpha_i y_i \langle w_i,x_i \rangle +b_k \right)
$$

***Repeat***
<br>
***for*** i= 1 to l
<br> 
***if*** $y_i\left(\sum\limits_{i=1}^l \alpha_i y_i \langle w_i,x_i \rangle +b_k \right) \leq 0$, then

$$
\begin{aligned}
\alpha_{i}  &\leftarrow  \alpha_{i}+1\\
b_{i}  &\leftarrow  b_{i}  + y_iR^2 \\
\end{aligned}
$$

***end if***
<br>
***Until*** no mistakes made within the for loop 
<br>
Return :$(\alpha, b)$
Remark:
- The number of updates: 
- 
$$
\sum\limits_{i=1}^l \alpha_i=\Vert \alpha \Vert \leq \left( \frac{2R}{r} \right)^2
$$

which $\alpha_i >0$ means that $\langle x_i,y_i \rangle$ has been misclassified.
 - Training data only appear in the algorithm through the entries of the Gram matrix

$$
G_{ij}=\langle x_i, x_j \rangle
$$

# Python Code
The following code are from [website](https://towardsdatascience.com/an-introduction-to-perceptron-algorithm-40f2ab4e2099)
- Import data
```python
from sklearn import datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
np.random.seed(10)
# Load data
iris=datasets.load_iris()
X = iris.data[0:99,:2]
y = iris.target[0:99]
```

- Plot figure
```python 
# Plot figure
plt.plot(X[:50, 0], X[:50, 1], 'bo', color='blue', label='0')
plt.plot(X[50:99, 0], X[50:99, 1], 'bo', color='orange', label='1')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend()
```
```python
# Update y into -1 and 1
y=np.array([1 if i==1 else -1 for i in y])
```
- Perceptron Algorithm (Primal From)
```python
#########
# Gradient Descent
#########
# Initialize parameters
w=np.ones((X.shape[1],1));
b=1;
learning_rate=0.1;
Round=0;
All_Correct=False;
# Start Gradient Descent
while not All_Correct:
    misclassified_count=0
    for i in range(X.shape[0]):
        XX=X[i,]
        yy=y[i]
        if yy * (np.dot(w.T,XX.T)+b)<0:
            w+=learning_rate * np.dot(XX,yy).reshape(2,1)
            b+=learning_rate * yy
            misclassified_count +=1
    if misclassified_count==0:
        All_Correct=True
    else:
        All_Correct=False
    Round += 1
    print(Round)
print(w)
print(b)
```
- Plot result hyperplane
```python 
x_points = np.linspace(4,7,10)
y_ = -(w[0]*x_points + b)/w[1]
plt.plot(x_points, y_)
plt.plot(X[:50, 0], X[:50, 1], 'bo', color='blue', label='0')
plt.plot(X[50:99, 0], X[50:99, 1], 'bo', color='orange', label='1')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend()
```