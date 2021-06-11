---
title: '綜合機器學習複習'
date: 2021-05-21
permalink: /posts/2021/06/ml_review/
tags:
  - regression
category:
  - Machine Learning
---


# 前提

- 這是根據[CDA](https://edu.cda.cn/my/course/2783)機器學習卷的問題和書本"統計學習方法"的一些基礎複習而記錄的一些點。
- [簡單概念](https://buzzorange.com/techorange/2019/08/13/machine-learning-algorithm-collection/)

# 決策樹
## ID3
- "統計學習方法"書中第76頁中有詳細介紹
- 基本上就是使用**信息增益**來決定那一個特徵是根和根的分支是根特徵分類，再計算熵增益如此類推。
- 不可處理空值和數值形態字段

## C4.5
- "統計學習方法"書中第78頁中有詳細介紹
- 基本上就是使用**信息增益比**來決定那一個特徵是根和根的分支是根特徵分類，再計算熵增益如此類推。
- 可處理空值和數值形態字段


## 隨機森林
- [參考網頁](https://easyai.tech/ai-definition/random-forest/)
- 隨機森林是從樣本抽取N組數據，每組數據形成一𢒙決策樹，再從這N個決策樹中取特徵眾數
- 在机器学习中，随机森林是一个包含多个决策树的分类器， 并且其输出的类别是由个别树输出的类别的众数而定。 Leo Breiman和Adele Cutler发展出推论出随机森林的算法。
- 预测样本分类、用于样本排序、用于特征选择和用于回归预测

## 频繁闭项集
- [知乎解釋](https://www.zhihu.com/question/20177381)
- 閉項：它的直接超集的支持度计数都不等于它本身的支持度计数
- 闭项集同时是频繁: 也就是它的支持度大于等于最小支持度阈值，那它就称为闭频繁项集

##  防止決策樹OVERFITTING
- [防止決策樹OVERFITTING](https://www.cnblogs.com/shayue/p/jue-ce-shu-fang-zhi-guo-ni-he.html)
- 剪枝
- 提前停止:限制樣樹的高度，分類指標決定要不要再走下一支線


# 分類
- [ROC和AUC](https://easyai.tech/ai-definition/accuracy-precision-recall-f1-roc-auc/)
- [ROC,KS曲線,Lift曲線和PR曲線](https://zhuanlan.zhihu.com/p/39435695)


# SVM


- [Regularization](https://www.cnblogs.com/jianxinzhou/p/4083921.html):減少OVERFITTING，即減少變量的重要性。 
- [Regularization 2](https://allen108108.github.io/blog/2019/10/22/L1%20,%20L2%20Regularization%20%E5%88%B0%E5%BA%95%E6%AD%A3%E5%89%87%E5%8C%96%E4%BA%86%E4%BB%80%E9%BA%BC%20_/)

# 数据挖掘
- 分类
- 回归

## 線性回歸和邏輯回歸的相同和分別
- [線性回歸和邏輯回歸分別](https://tw.ec-europe.org/669098-what-is-the-difference-between-XGLTXI)
  - 線性回歸假設因變量的高斯（或正態）分佈。 Logistic回歸假設因變量的二項式分佈。
  - 線性回歸是關於在數據中擬合直線，而邏輯回歸是關於在數據中擬合曲線。
  - 線性回歸是機器學習的回歸算法，而邏輯回歸是機器學習的分類算法。
#  岭回归和lasso回归

- [講得很好的網頁](https://www.cnblogs.com/wuliytTaotao/p/10837533.html)


# 聚類
 
## 轮廓系数
- $s_i$接近1，则说明样本$i$聚类合理；
- $s_i$接近-1，则说明样本$i$更应该分类到另外的簇；
- 若$s_i$近似为0，则说明样本$i$在两个簇的边界上。

# SMOTE过采样算法

- [參考](https://www.cnblogs.com/Determined22/p/5772538.html)

# Machine Learning 和 Deep Learning 分別
- [知乎很好的解答](https://www.zhihu.com/question/41268372)


#  路徑BFS 與 DFS

- [解釋很好的網站](https://zhuanlan.zhihu.com/p/346666812)

# 數據取LOG

- [知乎解答](https://www.zhihu.com/question/22012482)
  - 1.We might want to see the data structure a little differently
  - 2.We might want to reduce skew to assist in modeling 
  - 3.We might want to straighten a nonlinear relationship in a scatterplot, so that we can model the relationship with simpler methods
