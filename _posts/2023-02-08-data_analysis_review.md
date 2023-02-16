---
title: 'Python maplotlib 例子'
date: 2023-01-13
permalink: /posts/2023/02/data_analysis_review
tags:
  - python,mathplotlib
category:
  - computer science
---


# 缺失值与异常值

- [知乎](https://zhuanlan.zhihu.com/p/434532885)
- [PPT](http://staff.ustc.edu.cn/~jbs/chapt3.pdf)



##　python 

```
data.drop_duplicates(keep="first",inplace=True)
data.dropna(axis=0,how='any',inplance=True)
```

