---
title: '其他統計分析'
date: 2022-05-19
permalink: /posts/2022/05/statistic_anova/
tags:
  - ANOVA
category:
  - Statistic
---

# 估計與檢驗

- 總體:研究對象的全體組成的集合為總體
- 樣本:在總體中選取部分有代表性的成員組成的子集稱為(隨機)樣本
- 參數:總體的數字特徵,$\mu,\sigma^2$
- 利用樣本對總體進行統計推斷,主要有兩類問題:估計和檢驗
- 估計:
  - 總體參數估計,分布函數、密度函數
  - 方法:最大似然,矩估計法,最小二乘法
  - $\mu \in [\bar x -u_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}},\bar x +u_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}]$
  - $\mu \in [\bar x -t_{1-\frac{\alpha}{2}}\frac{s}{\sqrt{n}},\bar x +t_{1-\frac{\alpha}{2}}\frac{s}{\sqrt{n}}]$
  - $\sigma^2 \in [\frac{(n-1)s^2}{\chi_{1-\frac{\alpha}{2}} (n-1)},\frac{(n-1)s^2}{\chi_{1-\frac{\alpha}{2}} (n-1)}]$
- 檢驗:它是從樣本值出發去判斷關於總體分布的某種看法是否成立

## 成對比較

|   X數據類型   |  X組別     |   Y    | 分析方法      |
|  ---  |  ---  |  ---  |  ---  |
|  定類     |  2組或多組     | 定量      |   方差 (ANOVA)   |
|  定類     |   僅僅2組    |   定量    |   T檢驗    |
|  定類    |    2組或多組   |  定類     |   卡方$\chi$    |

- 觀測兩組均獨立,即A組成員的值與B組成員的值無關
- $\sigma_1=sigma_2$
  
$$
t=\frac{(\bar x_1- \bar x_2)}{\sqrt{s^2(\frac{1}{n_1}+\frac{1}{n_2})}}
$$

where 

$$ 
s^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}
$$

- $\sigma_1\neq sigma_2$
$$
t=\frac{(\bar x_1- \bar x_2)}{\sqrt{(\frac{s_1^2}{n_1}+\frac{s^2_2}{n_2})}}
$$



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