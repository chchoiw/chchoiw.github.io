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

$$
A_{m\times n}=
\left[
\begin{matrix}
a_{00},\dots,a_{0,n-1} //
\vdots,\ddots,\vdots //
a_{m-1,0},\dots,a_{m-1,n-1}
\end{matrix}
\right]
$$