---
title: '02331-數據結構'
date: 2021-09-28
permalink: /posts/2021/09/02331/
tags:
  - 數據結構
category:
  - Computer Science
---


# 第三章

## 隊列

### 數組隊列
- 空隊列時
  - font=0, rear=0
- 非空隊列時
  - font是出隊,非空隊列font是有內容
  - rear是入隊,非空隊列rear是最後有內容的後一個位置,沒有內容
- 元素個數:
  
  $$
  n+\text{rear}-\text{font} \quad \text{(mod n)}
  $$
  
  $n$為隊列長度
### 鏈隊列

- 空隊列時
  
```
Q->font=head=Q->rear
head->next=Null
```

- 非空隊列時
  - font的指針指向head,但head沒有內容
  - rear的指針指向隊尾,p->rear->data是有內容的


## 中綴表達和后綴表達

| 中綴表達式       | 運算付棧OS      | 后綴表達式      |
|  ---  |  ---  |  ---  |
|9-(2+4*7)/5+3 #      | #      |    空   |
|  )/5+3            | #-(+*      |9347
|    /5+3   |    #-   |   9347*+    |
|    5+3   |    #-/   |   9347*+    |
|    +3   |    #-/   |   9347*+5    |
|    3   |    #+   |   9347*+5/-    |
|    空  |    #   |   9347*+5/-3+    |

- 總結兩個規則
- ()集齊了,()內的符號退棧, 進棧到后綴中
- 若下一個運算符號優先次序低於棧中, 先將運算棧中的全部運算符號退棧, 再將低優先次序的符號進棧




# 第四章

## 矩陣

$$
A_{m\times n}=
\left[
\begin{matrix}
a_{00} &\dots &a_{0,n-1} \\
\vdots &\ddots &\vdots \\
a_{m-1,0}&\dots &a_{m-1,n-1}
\end{matrix}
\right]
$$

寫成

$$
A=
[[a_{00},...,a{1,n-1}],...[a_{m-1,0},...,a_{m-1,n-1}]]
$$


- 按行(橫)存:
  
  $$
    a_{00},a_{01},\dots,a_{m-1,n-1}
  $$

- 按列(縱)存:
  
  $$
    a_{00},a_{1,0},\dots,a_{m-1,n-1}
  $$

- 對稱

$$  
\{
\begin{array}{cccc}
\frac{i(i+1)}{2}+j \quad & i\geq j  \\
\frac{j(j+1)}{2}+i \quad & i<j
\end{array}
$$


# 第五章

## 二叉樹

- 在$i$層,最多有$2^{i-1}$個結點
- 深度為$k$的二叉樹,最多有$2^{k}-1$結點
- 終端結點$n_0$,度數為2的結點數為$n_2$,

$$
n_0=n_2+1
$$

- 完全二叉樹:深度為$k$的二叉樹, 在前$k-1$層是滿樹,第$k$層的結點都在左邊。則有$n$結點的深度$k$

$$
k=\lfloor\log n\rfloor +1  \quad \text{or} \quad k=\lceil \log (n+1) \rceil
$$ 

- 前序歷遍:根左右
- 中序歷遍:左根右
- 後序歷遍:左右根
- 已知前序中序或中序後序確定二叉樹

- 線二叉樹

  |lchild       |  ltag     |   Data    | rtag      |rchild       |

$$
\text{ltag}=
\{
\begin{array}{cccc}
0 \quad & \text{lchild指向左孩子}\\
1 \quad & \text{lchild指向前趨}
\end{array}
$$

$$
\text{rtag}=
\{
\begin{array}{cccc}
0 \quad & \text{lchild指向右孩子}\\
1 \quad & \text{lchild指向后繼}
\end{array}
$$