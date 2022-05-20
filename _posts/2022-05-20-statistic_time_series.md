---
title: '時間序列'
date: 2022-05-19
permalink: /posts/2022/05/statistic_time_series/
tags:
  - 數據結構
category:
  - Statistic
---


# 時間序列

- 橫截面數據：橫截面數據是在同一時間，不同統計單位相同統計指標組成的數據列。橫截面數據是按照統計單位排列的。因此，橫截面數據不要求統計對象及其範圍相同，但要求統計的時間相同。也就是說必須是同一時間截面上的數據。
- 橫截面數據要注意異方差問題
- 時間序列數據：在不同時間點上收集到的數據，這類數據反映了某一事物、現象等
- 隨時間的變化狀態或程度。
- 面板數據：是截面數據與時間序列數據綜合起來的一種數據類型。其有時間序列和截面兩個維度，當這類數據按兩個維度排列時，是排在一個平面上，與只有一個維度的數據排在一條線上有著明顯的不同，整個表格像是一個面板,所以把panel data譯作“面板數據”。



- 可以用於分析時間序列數據：差分法、移動平均值法(MA)和自迴歸法(AR)

- 序列本身是非平穩的，通常我們有兩種處理方式，一是進行差分，二是進行對數變換。

## 季節指數提取
- 加法: $\bar y$全部平均, $\bar y_s$季節平均


$$
I=\bar y_s - \bar y
$$

- 乘法: $\bar y$全部平均, $\bar y_s$季節平均

$$
I=\frac{ \bar y_s} {\bar y}
$$


## 移動平均
- 向後移動平均k步



$$
\hat x_t=\frac{1}{k}\sum_{i=0}^{k-1} x_{t-i}
$$

- 中心移動平均k步
  - k是奇數

$$
\hat x_t=\frac{1}{k} \{ \sum_{i=1}^{ \frac{k-1}{2}} x_{t-i} \sum_{i=-\frac{k-1}{2}}^{-1 } x_{t-i} +x_t\}
$$

  - k是偶數,例如k=4

$$
\hat x_t=\frac{1}{2}\frac{x_t+x_{t+1}+x_{t-1}+x_{t-2}}{4}+\frac{1}{2}\frac{x_t+x_{t+1}+x_{t+2}+x_{t-1}}{4}
$$

## 指數

  |       |  大趨勢     | 季節效應      |
| :---: | :---: | :---: |
|    1參數   |  無     |  無     |
|    2參數  |   有    |  無     |
|    3參數   |    有   |   有    |


- 1參數:$x_t$實測, $\hat x_t$預測
  
$$
\hat x_{t+1}=\alpha  x_{t}+(1-\alpha) \hat x_{t}
$$


# ARMA
- [vedio link 1](https://www.bilibili.com/video/BV1Ev411h7nT/?spm_id_from=333.788.recommend_more_video.-1)
- [vedio link 2](https://www.bilibili.com/video/BV18g411u7ms/?spm_id_from=333.788.recommend_more_video.-1)
- 有空再補
  
## 時間序列預測步驟
- [REF 1](https://www.zhihu.com/question/52866306)