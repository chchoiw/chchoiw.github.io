---
title: 'k-Nearest Neighbor Algorithm'
date: 2019-09-23
permalink: /posts/2019/09/k_nearest_neighbor_alg/
tags:
  - k-Nearest Neighbor Algorithm
category:
  - Machine Learning
---

---
- [k-Nearest Neighbor Algorithm](#k-Nearest-Neighbor-Algorithm)

# k-Nearest Neighbor Algorithm
- Basically, this is my studying from [NTCU open course](http://ocw.nctu.edu.tw/index.php) - [Machine Learning](http://ocw.nctu.edu.tw/course_detail.php?bgid=1&gid=1&nid=563&page=1). I will take the key points for my references.

1. define distance
    * if values are real number, 

    $$d(x,x_0)=\left\Vert (x-x_0)\right\Vert^2$$

    * if values are ordinal,

    $$d(x,x_0)=\sum_{i=1}^n \mathbb{1}(x_i \neq x_0) $$

2. Given q query point $x_0$, find k-nearest neighbors and count which type is majority. 

3. Classify $x_0$ to the same class with the majority within k-nearest neighbors.

4. Be careful with scale with different attributes. We might need to normalize
5. 
$$
\hat x_j=\frac{x_j-\mu_j}{\sigma_j}
$$

4. Condensed Nearest Neighbors

- $Z$ is empty set for start
Repeat 
&nbsp;&nbsp;&nbsp;&nbsp;for all $x \in X$ (in random order)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;find $x' \in Z$ s.t.
        $$\left\Vert x-x' \right\Vert=\text{min}_{x_j \in Z} \left\Vert x-x_j \right\Vert$$
Until $Z$ does not change

5. python 



* The folling codes came from [website](https://stackabuse.com/k-nearest-neighbors-algorithm-in-python-and-scikit-learn/)

- Importing the Dataset

```python 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Assign colum names to the dataset
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Read dataset to pandas dataframe
dataset = pd.read_csv(url, names=names)
```

```python
dataset.head()
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
```

- Train Test Split

```python 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
```
- Feature Scaling
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
```
- Training and Predictions

```python
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
```
- Evaluating the Algorithm
```python 
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```