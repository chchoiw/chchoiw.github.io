---
title: '統計2-分析方法'
date: 2022-05-19
permalink: /posts/2022/05/statistic_analysis/
tags:
  - statistic analysis
category:
  - Statistic
---

- [統計分析方法](#統計分析方法)
  - [統計分析方法步驟和流程](#統計分析方法步驟和流程)
- [估計與檢驗](#估計與檢驗)
  - [成對比較](#成對比較)
    - [兩樣本獨立T檢驗](#兩樣本獨立t檢驗)
    - [兩樣成組對差值的T檢驗](#兩樣成組對差值的t檢驗)
  - [正態性檢驗](#正態性檢驗)
- [方差分析](#方差分析)
- [屬性數據分析(列聯表)](#屬性數據分析列聯表)
  - [無序變量](#無序變量)
    - [$\\chi$檢驗](#chi檢驗)
    - [Fisher exact test](#fisher-exact-test)
  - [有序變量關聯性](#有序變量關聯性)
  - [Mentel-Haenszel](#mentel-haenszel)
- [相關分析](#相關分析)
  - [過程](#過程)
- [因子分析](#因子分析)
  - [過程](#過程-1)
- [聚類](#聚類)
  - [系統聚類](#系統聚類)
- [問卷](#問卷)


# 統計分析方法
  1. 分類分析方法

  2. 結構簡化方法

  3. 相關分析方法

  4. 預測決策方法

## 統計分析方法步驟和流程

```mermaid
graph TB
iid0[統計分析目的]
iid1[確定母體範圍]
iid2[量表,如何量測量表]
iid3[抽樣]
iid4[統計數據整理,樣本統計量]
iid5[選擇統計方法,構造理論模型]
iid6[參數估計]
iid7[統計檢驗]
iid8[統計應用]
iid0-->iid1
iid1-->iid2
iid2-->iid3
iid3-->iid4
iid4-->iid5
iid5-->iid6
iid6-->iid7
iid7-->|yes|iid8
iid7-->|no|iid5
```

1. 提煉具體問題，確定欲達的目標
2. 確定定性理論，設置指標變量
	- 確定相關學科理論。如氣象學的理論
	- 確定各因素之間的因果關係
	- 確定內生變量(被解釋變量Y)
	- 確定外生變量(解釋變量X)
	- 選擇變量時需注意
  	- 變量之間的相關性
  	- 實際統計數據的局限性
  	- 不是涉及解釋變量越多越好
  	- 需經過反複試算，找尋適合的變量
3. 收集整理統計數據
   - 收集注意
     - 時間序列數據
       - 數據可比性
       - 統計口徑
       - 隨機誤差項的序列相關問題
     - 橫截面數據
       - 異方差性問題
     - 樣本容量問題

   - 統計數據整理
     - 折算
     - 差分
     - 對數化
     - 標準化
     - 剔除
     - 插值法

4. 選擇統計方法，構造理論模型
   - 繪製變量的樣本散點圖
   - 統計模型的建立
   - 采用不同模式進行計算機模擬

5. 進行統計計算，估計模型參數
   - 選擇合適的統計計算
     - 均值
     - 方法
     - 相關矩陣
     - 距離距陣
     - 特徵值
     - 特徵向量
   - 根據數據樣本估計模型參數
     - 最小二乘法
     - 極大似然法
     - 特徵根估計
     - 主成份估計

6. 模型的檢驗與修改
   - 統計檢驗
     - 回歸方程和回歸係數顯著性檢驗和擬合度檢驗
     - 隨機誤差項的序列相關檢驗和異方法性驗檢
     - 解釋變量的多重共線性檢驗
   - 模型實際意義檢驗
   - 對模型進行修改

7. 統計模型的應用
   - 分類研究
   - 簡化數據結構
   - 變量的相關分析
   - 進行經濟預測


 8. Ref
- [web link](https://wenku.baidu.com/view/908c908f998fcc22bdd10d16.html)
- [web link2](http://www.reea.agri.cn/sttzgg/201608/P020160831597768501898.pdf)
- [web link3](https://blog.csdn.net/nxcjh321/article/details/89095564)
- [web link4](http://epaper.gotop.com.tw/PDFSample/AEM002100.pdf)






# 估計與檢驗

- 總體:研究對象的全體組成的集合為總體
- 樣本:在總體中選取部分有代表性的成員組成的子集稱為(隨機)樣本
- 參數:總體的數字特徵,$\mu,\sigma^2$
- 利用樣本對總體進行統計推斷,主要有兩類問題:估計和檢驗
- 估計:
  - 總體參數估計,分布函數、密度函數
  - 方法:最大似然,矩估計法,最小二乘法
  - $\mu \in \Bigg[\bar x -u_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}},\bar x +u_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}\Bigg]$
  - $\mu \in \Bigg[\bar x -t_{1-\frac{\alpha}{2}}\frac{s}{\sqrt{n}},\bar x +t_{1-\frac{\alpha}{2}}\frac{s}{\sqrt{n}}\Bigg]$
  - $\sigma^2 \in \Bigg[\frac{(n-1)s^2}{\chi_{1-\frac{\alpha}{2}} (n-1)},\frac{(n-1)s^2}{\chi_{\frac{\alpha}{2}} (n-1)}\Bigg]$
- 檢驗:它是從樣本值出發去判斷關於總體分布的某種看法是否成立

## 成對比較

|   X數據類型   |  X組別     |   Y    | 分析方法      |
|  ---  |  ---  |  ---  |  ---  |
|  定類     |  2組或多組     | 定量      |   方差 (ANOVA)   |
|  定類     |   僅僅2組    |   定量    |   T檢驗    |
|  定類    |    2組或多組   |  定類     |   卡方$\chi$    |

###  兩樣本獨立T檢驗
- 觀測兩組均獨立,即A組成員的值與B組成員的值無關
- 需滿三個假定
  - 觀測是獨立
  - 每組觀測是來自正態總體
  - 兩個獨立方差相等
  - $H_0: \mu_1=\mu_2$
- $\sigma_1=\sigma_2$
  
$$
t=\frac{(\bar x_1- \bar x_2)}{\sqrt{s^2(\frac{1}{n_1}+\frac{1}{n_2})}}
$$

where 

$$ 
s^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}
$$

- $\sigma_1\neq \sigma_2$
  
$$
t=\frac{(\bar x_1- \bar x_2)}{\sqrt{(\frac{s_1^2}{n_1}+\frac{s^2_2}{n_2})}}
$$

### 兩樣成組對差值的T檢驗
- 需滿兩個假定 
  - 每對觀測的差值是來自正態總體
  - 每對觀測與其他對觀測是獨立
  - $H_0$:兩次測驗沒有顯著性差別

## 正態性檢驗
- Shapiro-Wilk
- Kolmogorov-Smirnov
- Cramer-von Mises
- Anderson-Darling
- 若p value <0.05, 拒絕分佈是正態

# 方差分析
- [REF 1](https://zhuanlan.zhihu.com/p/92787523)
- 方差分析是分析試驗數據的一種統計方法, 分析各種因素及因素間交互作用對研究對象某些指標值的影響
- 把實驗數據的總波動分解為由所考察因素引起的波動和隨機因素等引起的波動

- 方差分析要求數據滿足以下假定：
  - 觀測性是獨立的
  - 可比性：
    - 若資料中各組均數本身不具可比性則不適用方差分析。
  - 正態性：
    - y是連續
    - 即偏態分布資料不適用方差分析。對偏態分布的資料應考慮用對數變換、平方根變換、倒數變換、平方根反正弦變換等變量變換方法變為正態或接近正態後再進行方差分析。
  - 方差齊性：
    - 即若組間方差不齊則不適用方差分析。多個方差的齊性檢驗可用Bartlett法，它用卡方值作為檢驗統計量， 結果判斷需查閱卡方界值表。
  - 殘差：
    - 正態分佈
  - 檢證各種因素及因素間交互作用對研究對象某些指標值的影響:F檢驗


# 屬性數據分析(列聯表)

## 無序變量
### $\chi$檢驗
- X,Y 是屬性變量
- 數據量大時使用$\chi$檢驗,自由度為$(r-1)(c-1)$
- $H_0:\text{column and row data are not related}$
  

$$
\sum \sum 
\frac{ 
  (n_{i,j}- \frac{n_{ i \cdot}n_{\cdot j} }{n})^2
  } 
  {
     \frac{n_{i \cdot }n_{\cdot j}}{n}
  }
$$


### Fisher exact test
- 適合抽查數量少
- 計算方法為超幾何分布
- $H_0:\text{column and row data are not related}$

## 有序變量關聯性

## Mentel-Haenszel
- 有序相關:即隨著一個變量取值的增加,另一變量的取值是否也有變大
- Mentel-Haenszel Test $H_0:\text{column and row data are not order related}$
- 關聯程度可用$-1 \leq \gamma,\tau_b,\tau_a \leq 1$,越接近-1 或1就有序關聯越大
- $\tau_b$的95%置信區間是$[\tau_b-2\text{ASE},\tau_b+2\text{ASE}]$
- $\tau_b$全名叫Kendall的Tau-b 


# 相關分析

- 典型相關之基本假設
  - 線性關係:兩組變數的相關係數是基於線性關係，若不是線性關係，則變數需要 轉換，以達成線性關係。
  - 常態性(normality):雖然，典型相關並無最嚴格要求常態性，但常態性會使分配標 準化以允許變數間擁有較高的相關，因此，符合常態性是較好的作法，由於多變 量的常態難以判讀，所以大多都是針對單一變量要求是常態性。
  - 變異數相等(Homoscedasticity):若不相等，會降低變數間的相關，因此，需要符 合變異數相等。
  - 複共線性問題:若是變數間有複共線性問題，則無法說明任何一個變數的影響， 導致解釋的結果並不可靠，因此，需要變數無複共線性問題。
  - 樣本數:想對第一典型變量的負荷得到可靠估計，則樣本數至少是分析內變數個數的20倍(即n>20)
  - 異常點:異常點對相關係數的大小會產生很大的影響，而典型相關也是以相關係數為基礎，所以也會受異常點很嚴重的影響
- [REF 1](http://120.118.226.200/member/hunght/%E6%B4%AA%E5%83%96%E9%BB%9B%E8%80%81%E5%B8%AB%E6%95%99%E6%9D%90(IEM)/Canonical%20Analysis.pdf)
- [REF 2](http://epaper.gotop.com.tw/PDFSample/AEM002600.pdf)
- [REF 3](https://dasanlin888.pixnet.net/blog/post/34469087)
- [REF 4](https://dasanlin888.pixnet.net/blog/post/34469093)
- [ANOVA 與 MANOVA分別](/images/A97038118.pdf)



##  過程

- 均值、標準差和兩組變量間的相關系數
- 與主成分分析類似, 找出VAR($V_i$)最大,$\lambda_1$為它的最大的eigenvalue,稱$\sqrt{\lambda_1}$為第一典型相闗係數
- $H_0:\Sigma_{12}=0$,
  - Wilks' Lambda
  - Pillai's Trace
  - Hotelling-Lawley Trace
  - Roy's Greatest Root
  - p<0.05 ,即$\Sigma_{12}\neq 0$
- $H_0:\lambda_i=0 \quad \forall j>=i$
  - F test 
  - p<0.05 ,即$\lambda_i\neq 0$
- $(v_{ti},w_{ti})$為第t個觀測值在第i對典型向量,也是第i對樣本典型變量的得分值
  - 繪制散點圖$(v_{ti},w_{ti})$, 應在同一直線上,因為差個$\lambda_i$,
  - 若有異常值, 應分析原因

# 因子分析

- [REF 1](http://www.woshipm.com/data-analysis/4545137.html)
- [REF 2](https://zhuanlan.zhihu.com/p/150330786)


- 因子分析:將存在某些相關性的變量提煉爲較少的幾個因子，用這幾個因子去表示原本的變量，也可以根據因子對變量進行分類
- 因子分析的前題:
  - 要求因子的數量$m$小於原始變量的數量$p$，即$m\leq p$
  - 因子$F$之間是相互獨立且方差爲1；
  - 因子$F$和$\epsilon$之間的相關性爲0，$\epsilon$之間相關性爲0。


- 因子分析主要實現以下目的
  - 求解方程中的因子$F$的係數$a_{ij}$,因子載荷矩陣$[a_{ij}]$；
  - 給予因子$F$實際的解釋:名命分類
  - 展示原始特徵和公共因子之間的關係，從而實現降維和特徵分類等目的。

  $$F_i=\sum_{j} b_{ij}x_j$$

## 過程



```mermaid
graph LR
id0[充份性檢驗]
id1[選擇因子個數]
id2[提取公共因子並做旋轉]
id3[判斷因子與題項對應關係]
id4[計算因子得分]

id0-->id1
id1-->id2
id2-->id3
id3-->id4
```


- 充份性檢驗: 檢驗變量之間是否存在相關性，從而判斷是否適合做因子分析；
  - KMO>0.7,和Bartlett's Test的p-value<0.01
- 選擇因子個數:通過數據定義最合適的潛在公共因子個數，這個決定後面的因子分析效果
  - Kaiser”s準則 :choose $F_i$ where var($F_i$)>1
  - 累積貢獻率原則
- 提取公共因子並做因子旋轉:求解函數的過程,即求$a_{ij}$
  - 主要方法有:主成分法、最大似然法、殘差最小法
- 判斷因子與題項對應關係:解釋和命名其實是對潛在因子理解的過程
  - 根據因子載荷矩陣發現因子的特點,
  - 看因子載荷系數和共同度,$h_i^2$是變量$x_i$的共同度, $q_j^2$是$F_j$對$X_i \quad \forall i$的總影響
  
  $$
  h_i^2=\sum_{j} a_{ij}^2
  $$

  $$
  q_j^2=\sum_{t}a_{tj}^2
  $$

- 計算因子得分:對每一樣本數據，得到它們在不同因子上的具體數據值，這些數值就是因子得分。
  -  驗檢,降維和分類







# 聚類

## 系統聚類
- 根據統計量決定分類個數
  - $R^2$越大說明NCL個類分得越開
  - 偽$F$越大說明樣品可明顯分為NCL個
  - 偽$t^2$越大說明上次合併結果最好

# 問卷

```mermaid
graph LR
id0[研究目的]
id1[編擬及修訂量表初稿]
id2[選取受試者預試]
id3[項目分析]
id4[因素分析]
id5[正式量表]

id0-->id1
id1-->id2
id2-->id3
id3-->id4
id4-->id5
```


- [REF 1](https://www.mercy.org.tw/public/ufile/ufile/2ce058b96885f861a7e7f1f7a14a4fe6.pdf)
- [REF 2](http://web.thu.edu.tw/s974836/www/%E4%BF%A1%E5%BA%A6%E6%95%88%E5%BA%A6.pdf)
- 項目分析(信度):確認量表題目的堪用程度
  - 刪除鑑別力不夠的題目
  - 所謂效度是指衡量的工具是否能真正衡量到研究者想要衡量的問題。
- 因素分析(效度):
  - 進行建構效度,刪除解釋力不夠項目,保留最後構面與項目
  - 所謂效標關聯效度是指使用中的衡量工具和其他的衡量工具來比較兩者是否具有關聯性。

