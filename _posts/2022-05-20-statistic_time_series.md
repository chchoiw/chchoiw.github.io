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

## 平移
- 向後平移k步
  
$$
\hat x_t=\frac{1}{k}\sum_{i=0}^{k-1} x_{t-i}
$$

- 中心平移k步
  - k是奇數

$$
\hat x_t=\frac{1}{k} \{ \sum_{i=1}^{ \frac{k-1}{2}} x_{t-i} \sum_{i=-\frac{k-1}{2}}^{-1 } x_{t-i} +x_t\}
$$

  - k是偶數,例如k=4

$$
\hat x_t=\frac{1}{2}\frac{x_t+x_{t+1}+x_{t-1}+x_{t-2}}{4}+\frac{1}{2}\frac{x_t+x_{t+1}+x_{t+2}+x_{t-1}}{4}
$$

## 指數
