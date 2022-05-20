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
