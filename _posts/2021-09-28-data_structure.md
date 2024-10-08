---
title: '02331-數據結構'
date: 2021-09-28
permalink: /posts/2021/09/02331/
tags:
  - 數據結構
category:
  - Computer Science
---


- [第一章](#第一章)
- [第三章 棧和隊列](#第三章-棧和隊列)
  - [棧](#棧)
  - [隊列](#隊列)
    - [數組隊列](#數組隊列)
    - [鏈隊列](#鏈隊列)
  - [中綴表達和后綴表達](#中綴表達和后綴表達)
- [第四章 多維數組和廣義表](#第四章-多維數組和廣義表)
  - [矩陣](#矩陣)
  - [廣義表](#廣義表)
- [第五章](#第五章)
  - [二叉樹](#二叉樹)
  - [樹和森林](#樹和森林)
  - [哈夫曼樹](#哈夫曼樹)
- [第六章 圖](#第六章-圖)
  - [搜索遍歷](#搜索遍歷)
  - [最小生成樹](#最小生成樹)
    - [Prim算法](#prim算法)
    - [Kruskal算法](#kruskal算法)
  - [最短路徑](#最短路徑)
    - [Dijkstra](#dijkstra)
  - [拓扑排序](#拓扑排序)
- [第七章 排序](#第七章-排序)
  - [插入排序](#插入排序)
  - [交換排序](#交換排序)
  - [選擇排序](#選擇排序)
  - [歸並排序](#歸並排序)
  - [分配排序](#分配排序)
  - [內部排序比較](#內部排序比較)
- [第八章 查找](#第八章-查找)
  - [順序查找](#順序查找)
  - [樹表查找](#樹表查找)
    - [B樹](#b樹)
    - [B+樹](#b樹-1)
  - [散列表查找](#散列表查找)
- [考試常見名詞](#考試常見名詞)


# 第一章

- 算法滿足輸入、輸出、有窮性、確定性和可行性
- 評價算法優劣
  - 時間複雜性
  - 空間複雜性
  - 可讀性和可操作性



# 第三章 棧和隊列
## 棧
- 先進後出
- $a_1$,$a_2,\dots,a_n$
- 棧頂TOP:$a_n$
- 棧底BOTTOM:$a_1$
- 入出的也在棧頂
- 出的元素順序$a_n,\dots,a_1$
- 進棧: S.top+1
- 退棧: S.top-1
- 棧空: S.top=-1
- 棧滿: S.top==stackSize-1


## 隊列
- 先進先出

### 數組隊列
- 空隊列時
  - font=0, rear=0
- 非空隊列時
  - font是出隊,非空隊列font是有內容
  - rear是入隊,非空隊列rear是最後有內容的後一個位置,沒有內容
  
  ```
  Q-->data[Q-->rear]=x;
  Q-->rear=(Q-->rear+1) %n
  ```

  - 測滿: ```(Q-->rear+1) %n==(Q-->font)```
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


| 中綴表達式       | 運算付棧OS (棧)     | 后綴表達式(隊列)      |
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




# 第四章 多維數組和廣義表

## 矩陣
- $m$行,$n$列

$$
A_{m\times n}=
\left[
\begin{matrix}
a_{0,0} &\dots &a_{0,n-1} \\
\vdots &\ddots &\vdots \\
a_{m-1,0}&\dots &a_{m-1,n-1}
\end{matrix}
\right]
$$

寫成

$$
A=
[[a_{0,0},...,a_{1,n-1}],...[a_{m-1,0},...,a_{m-1,n-1}]]
$$


- 按行(橫)存:
  
  $$
    a_{00},a_{01},\dots,a_{m-1,n-1}
  $$

  $$
  a_{i,j}=a_{00}+(n*i+j)*d
  $$

- 按列(縱)存:
  
  $$
    a_{00},a_{1,0},\dots,a_{m-1,n-1}
  $$


  
  $$
  a_{i,j}=a_{00}+(m*j+i)*d
  $$

- 對稱(存,$n=m$), 只存$\frac{n*(n+1)}{2}$,在$a_{i,j}$順序來存, 它在$k$的位置

$$  
k=\Bigg\{
\begin{array}{cccc}
\frac{i(i+1)}{2}+j \quad & i\geq j  &\quad (\text{lower triangle})\\
\frac{j(j+1)}{2}+i \quad & i<j &\quad (\text{upper triangle})
\end{array}
$$

- 下三角矩陣, 即上三角(不包括對角綫)為常數

$$  
k=\Bigg\{
\begin{array}{cccc}
\frac{i(i+1)}{2}+j \quad & i\geq j  \\
\frac{n(n+1)}{2} \quad & i<j 
\end{array}
$$

- 上三角矩陣, 即下三角(不包括對角綫)為常數

$$  
k=\Bigg\{
\begin{array}{cccc}
\frac{i(2n-i+1)}{2}+j-i \quad & i\leq j  \\
\frac{n(n+1)}{2} \quad & i>j 
\end{array}
$$

- 稀疏矩陣


|index| i (行號)      | j(列號)     | v(value)      |
|---|  ---  |  ---  |  ---  |
|0|  0 |  1  |  3  |
|1|  0 |  3  |  5  |
|2|  1 |  2  |  -2  |
|3|  2 |  0  |  1  |
|4|  2 |  4  |  6  |
|5|  3 |  2  |  8  |

|i (行號)| 第i行第一個非零的index      | 第i行之前非零元素總數     | 第i行上非零元素個數      |
|---|  ---  |  ---  |  ---  |
|0|  0 |  0  |  2  |
|1|  2 |  2  |  1  |
|2|  3 |  3  |  2  |
|3|  5 |  5  |  1  |


## 廣義表
- P.98
- 空表: (),長度為0
- (()),長度為1
- C=(a,(b,c)),長度為2
- (e,(e,(e,...)))為無限廣義表,深度為$\infty$,長度為2
- A=(a,(b,c,d),e,(f,g))
  - A的第一個元素,head(A)=a
  - A刪除第一個元素的廣義表,tail(A)=((b,c,d),e,(f,g))
- 通常采用鏈式存儲結構, 可用一個結點表示
  - tag=0,表示為子表,用slink
  - tag=1,表示為結點,用data
  - link為下一個元素的指針

  |tag|data/slink     | link     |


# 第五章

## 二叉樹

- 在$i$層,最多有$2^{i-1}$個結點
- 深度為$k$的二叉樹,最多有$2^{k}-1$結點
- 終端結點$n_0$,度數為2的結點數為$n_2$,

$$
n_0=n_2+1
$$

- 完全二叉樹:深度為$k$的二叉樹, 在前$k-1$層是滿樹,第$k$層的結點都在左邊。則有$n$結點的深度$k$
- 分支結點即度不為0的結點。


$$
k=\lfloor\log n\rfloor +1  \quad \text{or} \quad k=\lceil \log (n+1) \rceil
$$

- P.113:從data[], 轉換成樹

```c
void create (int* Data, int n)
{
  BinTNode *Q[100],*Bt=NULL,*p;
  int font=0;rear=0,k;
  for (k=0;k<n;k++)
  {
    p=NULL;
    if (data[k]!=0)
    {
      p=(BinTree)malloc(sizeof (BinTNode));
      p->data=data[k];
      p->lchild=p->rchild=NULL;
    }
    Q[rear++]=p;
    if (rear==1) Bt=p;
    else 
    {
      if (p!=NULL && Q[font]!=NULL)
      {
        if (rear%2==0) Q[font]->lchild=p;
        else Q[font]->rchild=p;
        if (rear%2==1) font++;

      }
    }
  }
}
```


- 前序歷遍:根左右
- 中序歷遍:左根右
- 後序歷遍:左右根
- 已知前序中序或中序後序確定二叉樹

- 線二叉樹

  |lchild       |  ltag     |   Data    | rtag      |rchild       |

$$
\text{ltag}=
\Bigg\{
\begin{array}{cccc}
&0 \quad &\text{lchild指向左孩子}\\
&1 \quad &\text{lchild指向前趨}
\end{array}
$$

$$
\text{rtag}=
\Bigg\{
\begin{array}{cccc}
&0 \quad &\text{rchild指向右孩子}\\
&1 \quad &\text{rchild指向后繼}
\end{array}
$$

這裏前趨後繼是根據前,中和後序其中一㮔排序算法,沒有特別指出,就假設是中序。

## 樹和森林

- 樹變二叉樹:
  - 兄弟連成線, 只保留長子
- 二叉樹變樹:a右結點與a父母連, 並斷與a連, 即與祖父母連, 但與父母斷關係
- 樹前序:根，前序遍歷子樹(左子樹才到右)。變二叉樹後等價前序
- 樹后序:后序遍歷子樹(右子樹才到左)，根。變二叉樹後等價中序

  
## 哈夫曼樹
- 最小兩個的比重做成一個, 代表原本的放入數列
- 同复上術步驟
- 比重大的一側為1,小的一則為0
- 則可由經過的路徑組成編碼
- $n$個字符的哈夫曼樹有結點$2n-1$個
  


# 第六章 圖


- 無向圖邊數:$e\leq\frac{n(n-1)}{2}$
- 無向圖邊數:$e\leq\ n(n-1)$
- 連通圖:任意兩點都有連接
- 任何$n$個頂點,任何情況下都是連通的, 則至少需多少邊?

$$
\frac{(n-1)(n-2)}{2}*\frac{2}{3}+1
$$

## 搜索遍歷
- 深度搜索遍歷(DFS):
  - 矩陣$O(n^2)$,鄰接表$O(n+e)$
  - 深度, 找深, 沒有更深時, 找最晚,但有支線是沒有歷遍
- 廣度搜索遍歷(BFS):
  - 矩陣$O(n^2)$,鄰接表$O(n+e)$
  - 廣度,第一層已遍歷,跟第一層頂點次序遍歷第二層,如此類推


## 最小生成樹
- 樹是無回路的連通圖
- 極小連通子圖:若在圖中去掉一邊,會變成非連通。若加一邊，則有回路



### Prim算法
- 先選一點$U=\{x\}$
- 再從已歸納的點集$U$中可伸展的邊,選出來, 並將這邊頂點歸納在$U$中，並重覆，直至$U$包括了所有的頂點
- $O(n^2)$
- 圖G有$n$的頂點, 生出來的樹$T$的邊數是$n-1$

### Kruskal算法
- 所有頂點在原處,選最小權的邊,直至成為連通圖

## 最短路徑

### Dijkstra
- 尋找某一點$V_0$到其他點的最短路徑
- 無路徑通往的頂點設為$\infty$
- 選連通權數最少又不在集合$U$中的頂點加入$U$,更新加入$U$後的有限路徑中選取權數最少的路徑
- 重覆上述步驟, 直至$U$包括所有的頂點, 這時$V_0$到其他頂點的最短路徑產生
  

## 拓扑排序
- 入度為0的頂點, 輸出它,並刪除它與它的出線
- 重覆以上動作,就找到排序
- 排序不唯一


# 第七章 排序

相同紀錄，若排序時相對位置持保持，則稱為穩定

## 插入排序

- 直接排序
  - $A=\{a_1\}$ 為以排序的，$B=\{a_2,\dots,a_n\}$ 為未排序
  - 將$B$中與$A$最後的元素比較，比$A$小的才向前移動，直至不再比較小，將元素直接插入$A$,並向後移動比它大的，如此類推
  - 在$i$中，最多向後移動$i+1$次，最多比較$i$次
  - 最好的情況$O(n)$，最壞的情況$O(n^2)$,平均$O(n^2)$
  - 空間$O(1)$
  - 穩定的
- 希爾排序
  - $d$為增量序列
  - $a_1$為數列第一項，不是$a_0$,z設$d_1$為間距，將數列分成
    
    $$
    \{a_1,a_1+d_1,a_1+2d_1\} \quad \{a_2,a_2+d_1,a_2+2d_1\} \quad \dots
    $$

  - 在上述集合中進行**直接排序**

  - 取$d_2<d_1$,重覆上述
    
    $$
    \{a_1,a_1+d_2,a_1+2d_2\} \quad \{a_2,a_2+d_2,a_2+2d_2\} \quad \dots
    $$

  - 最後隔距$d_l=1$
  - $n$很大時，比直接排序時間和移動少很多,
  - 移動和比較次數約為$n^{1.25}-1.6n^{1.25}$
  - 不穩定的，因為$d$會令相同數值的後面的元素向前移動
  
## 交換排序
- 冒泡排序
  - 從後到前，有後比前小的交換，第一個出來的一定是最少
  - 如此類推，直至排序完成
  - 若第一趟沒有置換，則排序完成
  - 最好的情況$O(n)$，最壞的情況$O(n^2)$,平均$O(n^2)$
  - 穩定的
- 快速排序
  - $B=a_1$為基準
  - $i=1,j=n$
  - for some biggest $j_b$ $a_{j_b}<B$ for some biggest $j$, 
    
    $$a_i=a_{j_b} \quad j=j_{b} \quad i=i+1$$

  - for some smallest $i_s$ $a_{i_s}>B$ for some smallest $i$, 
    
    $$a_j=a_{i_s} \quad i=i_{s} \quad j=j+1$$

  - 不穩定的，因為$i,j$互換數值
  - 平均時間$O(n \log_2 n)$,排序已為有序時，第一趟只固定$a_1$的位置，但還有$a_2,\dots a_{n-1}$,所以時間$O(n^2)$
  - 空間時間$O(n \log_2 n)$，棧最大深度為$\lceil n \log_2 n \rceil+1$

## 選擇排序
- 直接選擇：
  - 從中選出最小的與$a_1$交換，如此類推
  - 平均時間$O(n^2)$
  - 不穩定
- 堆排序
  - 數列變二叉樹，根->左->右->左左->左右
  - 從最底開始置換，最大堆，即倒序，孩子必須小於父母，不然就置換
  - 從第一棵樹中選出根，其餘再組成最大堆，再取根
  - 樹的排序的時間$O(n \log_2 n)$，並$n-1$棵樹，所以時間$O(n \log_2 n)$
  - 不穩定
  - 小根堆 $k_{2i+1},k_{2i+2}\geq k_i \quad i\leq \lceil \frac{n}{2} \rceil$,降序
  - 大根堆，升序


## 歸並排序
  - 每一個元素為一組，相鄰的合並，並排序，
  - 第一趟後，有$\lceil \frac{n}{2} \rceil$的組別，如此類推
  - 每一趟的排序的時間$O(n)$，並需要$ \log_2 n$趟，所以時間$O(n \log_2 n)$
  - 穩定

## 分配排序
- 箱排序/基數排序
  - 先將數字用個位數排序
  - 排序後再十位數排序
  - 如此類推
  - $r$為箱數，上例為10，$d$為趟數，上例為2
  - 初始化和分配$n$個鏈表為$O(n)$,清空和收集箱子時間為 $O(rd)$,共$d$趟
  - 時間為$O(d(rd+n))$

## 內部排序比較
- 時間複雜
  1. 直接插入、直接選擇、冒泡為$O(n^2)$
  2. 快速、歸並、堆排為$O(n \log_2 n)$
  3. 希爾$O(n \log_2 n)$ 或$n^{1.25}$
  4. 基數$O(d(rd+n))$
   
- 穩定
  - 直接插入、冒泡、歸並和基數為穩定
  - 直接選擇、希爾、堆排和快速為不穩定
- 空間複雜
  - 快速$O(\log_2 n)$
  - 歸並$O(n)$
  - 直接插入、直接選擇、冒泡、希爾和堆排$O(1)$

- [link](https://www.runoob.com/w3cnote/ten-sorting-algorithm.html)

# 第八章 查找

## 順序查找
- 平均查找長度,$P_i$概率,$C_i$列表中第$i$個元素


$$
\text{ASL}=\sum P_iC_i
$$

- 順序查找
- 二分查找: 要順序排序
- 索引順序查找:又稱分塊查找;塊間有序,塊內無序

## 樹表查找
### B樹

- $m\geq 3$階樹
  
$$
(m,p_0,k_1,p_1,k_2,\dots,k_m,p_m)
$$


- 每棵樹至多有$m$棵子樹
- 若樹為非空,根結點至少有1個關鍵字,至多有$m-1$個關鍵字。
- 所有葉結點都在同一層上,並且不帶信息
- 關鍵字個數 $\lceil \frac{m}{2} \rceil-1 \leq n \leq m-1$
- 除結點外, 結點有子樹$\lceil \frac{m}{2} \rceil \leq n \leq m$
- 注意,通常關鍵字的數量為$m$時, 因為包頭尾,子樹數量為$m+1$
- P.209:生成、插入和刪除過程需要了解

### B+樹

- 是B樹的變型樹
- 有$k$個孩子就有$k$個關鍵字
- 葉結點中包含了關鍵字的信息及指向相應的指針,且葉子結點本身依照關鍵字的大小自小到大順序鏈接
- 所有非終結點可看成索引部分, 結點中僅含其子樹中最大或最小的關鍵字

$$
(m,k_1,p_1,k_2,\dots,k_m,p_m)
$$

- 如$k_1$的子樹

$$
( (k_1-1,p_1) , (k_1,p_2) ) 
$$

- 沒有子樹的最大值比根的最大值大




## 散列表查找

- P.215
- 處理沖突的方法
  - 開放定址法:線性探插法、二次探查法和雙重散列法,
    - 沿著序列逐個單元進行查找,直到空為止
  - 拉鏈法:鏈表
- 上面的要計算平均查找長度ASL

# 考試常見名詞
- 數據項是具有獨立含義的<span style="color:red">最小</span>標識單位
- 算法滿足輸入、輸出、有窮性、確定性和<span style="color:red">可行性</span>
- 數據的四種基本存儲方法是<span style="color:red">順序,鏈接,索引和散列存儲</span>
- 數據結構是數據的<span style="color:red">邏輯結構和儲存結構</span>
- <span style="color:red">遞歸函數</span>
- 遞歸的最小子問題稱<span style="color:red">遞歸終止條件</span>
- <span style="color:red">有向無環圖</span>
- <span style="color:red">父結點或兄弟</span>
- <span style="color:red">裝填因子</span>,大則發生沖突機率大
- <span style="color:red">儲存地址</span>
- <span style="color:red">帶權路徑長度</span>
- 最小<span style="color:red">生成樹</span>
- 極小<span style="color:red">連通圖</span>
- <span style="color:red">順序存儲</span>結構
- <span style="color:red">基數大小</span>
- 分塊查找<span style="color:red">索引查找</span>
- 數據的運算,即對數據元素施加的操作, 是定義在數據的<span style="color:red">邏輯</span>結構
- <span style="color:red">三元組表</span>
- <span style="color:red">索引查找</span>
- 線索取代<span style="color:red">空指針</span>
- 無序數組用<span style="color:red">順序查找</span>
- 數據邏輯結構是從邏輯關係上描述數據,它與數據的存儲<span style="color:red">無關</span>
- 散列存儲,解決沖突方法有<span style="color:red">開放地址法</span>和<span style="color:red">拉鏈法</span>
- 頂點表示活動,邊表示活動間的先後關係,稱<span style="color:red">頂點活動網(AOV)</span>
- 借助一個棧來實現圖的遍歷遍算法是<span style="color:red">深度遍歷</span>
- 若有向圖中存在排序序列,則一定不存在<span style="color:red">回路</span>
- 最短路徑<span style="color:red">Dijkstria</span>,最小生成樹<span style="color:red">Prim,Kruskal</span>
- 在<span style="color:red">隊尾</span>加元素,在<span style="color:red">隊頭</span>減元素
- 二分查找是<span style="color:red">順序查找結構, 按關鍵字有序</span>
- 分塊查找, 先查<span style="color:red">索引表</span>,再找相應的<span style="color:red">塊</span>
- 平均查找長度與結點無關的查找方法是<span style="color:red">散列查找</span>
- 三種查找方法: <span style="color:red">樹表, 順序和散列</span>
- Dijkstra 算法是按照路徑: <span style="color:red">長度</span>不減的次序求出各條路徑的
- 一個連通圖的<span style="color:red">生成樹</span>是包含圖中所有頂點的極小連通子圖
- 箱排序的改進和推廣的算法是<span style="color:red">基數排序</span>
- 長度為1的廣義表,若有Head(A)=Tail(A),則A=<span style="color:red">(())</span>