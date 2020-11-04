---
title: 'Ring Ration'
date: 2019-04-26
permalink: /posts/2019/04/ring_ration/
tags:
  - ring ration
category:
  - Statistic
---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [簡介](#簡介)
- [價格指數](#價格指數)
- [總價](#總價)
- [計算短物量](#計算短物量)
- [計算短期物量指數](#計算短期物量指數)
- [環比物量指數](#環比物量指數)
- [環比物量](#環比物量)
- [總結：](#總結)

<!-- /code_chunk_output -->


## 簡介

- 這是透過澳門統計局對環比的介紹，規範寫出數學關係式，以便自己的理解。


- ref:[澳門統計局](https://www.dsec.gov.mo/elearning/knowledge/123)

- 以下$P$是指價格，$Q$是指數量。

## 價格指數

$$PI_{n,k}=\frac{P_{n,k}}{P_{n-1,k}} $$

其中$k$是類型,$n$是時期
<!-- \frac{\sum P_{n-2}Q_{n-1}}{\sum P_{n-2}Q_{n-2}} -->
## 總價

$$V_{n,k}=P_{n,k}Q_{n,k}$$


## 計算短物量

$$SQ_{n}=\sum_{k} SQ_{n,k}= \sum_{k} P_{n-1,k}Q_{n,k}=\sum_{k} \frac{V_{n,k}}{PI_{n,k}}$$

其中，

$$SQ_{n,k}=P_{n-1,k}Q_{n,k}$$

是某一 $k$ 類在 $n$ 時期的短期物量。

## 計算短期物量指數

$$SQI_{n,k}= \frac{ P_{n-1,k}Q_{n,k}}
{P_{n-1,k}Q_{n-1,k}}
 =\frac{\frac{V_{n,k}}{PI_{n,k}} }
 { P_{n-1,k}Q_{n-1,k}}
 = \frac{\frac{V_{n,k}}{PI_{n,k}} }
 { V_{n-1,k}}
 $$

$$SQI_{n}= \frac{\sum\limits_{k} P_{n-1,k}Q_{n,k}}
{\sum\limits_{k} P_{n-1,k}Q_{n-1,k}}
 =\frac{\sum\limits_{k} \frac{V_{n,k}}{PI_{n,k}} }
 {\sum\limits_{k} P_{n-1,k}Q_{n-1,k}} 
 $$

## 環比物量指數

$$ RI_{n,k}=\frac{ P_{n-1,k}Q_{n,k}}{ P_{n-1,k}Q_{n-1,k}}   \frac{P_{n-2,k}Q_{n-1,k}}{ P_{n-2,k}Q_{n-2,k}} ...\frac{ P_{0,k}Q_{1,k}}{ P_{0,k}Q_{0,k}}
= \frac{\frac{V_{n,k}}{PI_{n,k}} }{ V_{n-1,k}}
\frac{\frac{V_{n-1,k}}{PI_{n-1,k}} }{ V_{n-2,k}}
\frac{\frac{V_{1,k}}{PI_{1,k}} }{ V_{0,k}}
=\frac{Q_{1,k}}{Q_{0,k}}
$$

$$ RI_{n}=\frac{\sum\limits_{k} P_{n-1}Q_{n}}{\sum\limits_{k} P_{n-1}Q_{n-1}}   \frac{\sum\limits_{k} P_{n-2}Q_{n-1}}{\sum\limits_{k} P_{n-2}Q_{n-2}} ...\frac{\sum\limits_{k} P_{0}Q_{1}}{\sum\limits_{k} P_{0}Q_{0}}$$

值得注意的是

$$ RI_{n}=SQI_{n}\times SQI_{n-1}\times... \times SQI_{0}$$

## 環比物量

$$ RQ_{n,k}=RI_{n,k} \times P_{0,k} \times Q_{0,k}$$

$$ RQ_{n}=\sum\limits_{k} RI_{n,k} \times P_{0,k} \times Q_{0,k}$$

## 總結：

- 在統計表中，基本上不會給出數量$Q$,也不會給出價格指標$PI$,所以在**環比物量**統計表中是無法自己計算的。
- 另外,通常**實際GDP增長**是
  
  $$
  \text{實際GDP增長}=\frac{\sum P_0Q_1}{\sum P_0Q0}
  $$


----
例子:
香港統計局:2018第4季GDP

- [web link](https://www.statistics.gov.hk/pub/B10300012018QQ04B0100.pdf),
- [local link](pdf/hk_gdp_2018_4.pdf)

1. 表 3 各組成部分在本地生產總值的按年實質變動百分率中所佔的比率:
根據解釋38中,表中數據是: 

  $$實際年增長率_{n,k} \times (n-1) 時期 k 類所佔百分比$$

   - 即是**表4(乙)數據**乘以**表4(丙)** 所計算的上一年的百分表。

   以2018年第一季私人開支為例:
   - 表4(乙)數據=8.9
   - 表4(丙)的上一年百分比=415294/622549=0.667
   - 所以表3=8.9%*0.667=5.9%

2. 表2 瀏覽解釋34-37,期中37說明了
- 表4(丙)經過[X-12自迴歸-求和-移動平均]剔除季節性效應
- 計算對上季度比較的變動百分率

# 拉氏指數
- [百度百科](https://baike.baidu.com/item/%E6%8B%89%E6%B0%8F%E6%8C%87%E6%95%B0)
- 拉氏物量指数

$$\text{L_I}=\frac{\sum P_0Q_1}{\sum P_0Q_0}$$

- 拉氏物價指数

$$\text{L_p}=\frac{\sum P_1Q_0}{\sum P_0Q_0}$$

- 拉氏指數通常指**拉氏物價指数**

# 帕氏指數
- [百度百科](https://baike.baidu.com/item/%E5%B8%95%E6%B0%8F%E6%8C%87%E6%95%B0)
- 帕氏物量指数

$$\text{P_I}=\frac{\sum P_1Q_1}{\sum P_1Q_0}$$

- 帕氏物價指数
   
$$\text{P_I}=\frac{\sum P_1Q_1}{\sum P_0Q_1}$$

# 拉氏與帕氏的差別
- 拉氏的權數(物價權數:Q; 物量權數:P)固定在基期。
- 帕氏的權數(物價權數:Q; 物量權數:P)固定在報告期
- 拉氏與帕氏指數多指價格指數

# 指標
- 指标归纳起来有数量指标和质量指标
- 
## 質量指數
反映质量指(價格)标综合变动，则指标化指标是质量(價格)指标  

  $$\text{P_1}=\frac{\sum P_1Q_X}{\sum P_0Q_X} $$
  
- 當$X=0$(即權數在基期)時,它是拉氏
- 當$X=1$(即權數在報告期)時,它是帕氏

## 數量指數
反映数量指标综合变动，则指标化指标是数量指标  
  $$\text{P_2}=\frac{\sum P_XQ_1}{\sum P_XQ_0} $$

- 當$X=0$(即權數在基期)時,它是拉氏
- 當$X=1$(即權數在報告期)時,它是帕氏