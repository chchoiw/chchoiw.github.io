---
title: '綜合統計複習'
date: 2021-05-21
permalink: /posts/2021/05/stat_3/
tags:
  - regression
category:
  - Statistic
---

# 一些基本描述統計


- [68–95–99.7原則](https://zh.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7%E5%8E%9F%E5%89%87) :
  - 一個標準差=**0.68**
  - 二個標準差=**0.95**
  - 三個標準差=**0.99**

## 統計特徵量
- 用來表達所有資料中意涵訊息的特徵，以凸顯資料所代表的意義，讓使用該資料之研究者或讀者能夠掌握分析方向
- 分四大類：集中量數、差異量數、偏態與峯度。

## 集中量數/集中趨勢量數
- 指一羣體中之個體的某一特性，有其共同的趨勢存在，此一共同趨勢之量數即稱之集中趨勢量數
- 因其能夠代表該羣體特性的平均水準，故通稱為平均數
- 居有簡化作用、代表作用和比較作用


## 偏度
- [wiki](https://zh.wikipedia.org/zh-hant/%E5%81%8F%E5%BA%A6)


<div style="text-align:center" id="image1"><img src="/images/stat/c1007_3.jpg" /></div>

- 負偏態或左偏態：偏度<0，平均值左側的橫軸更長，分佈的主體集中在右側。平均<中位<眾數，峯的位置在右邊。
- 
- <div style="text-align:center" id="image1"><img src="/images/stat/c1007_2.jpg" /></div>
- 正偏態或右偏態：偏度>0，平均值右側的橫軸更長，分佈的主體集中在左側。眾數<中位<平均，峯的位置在左邊。

$$
g=\frac{m_3}{m_2^\frac{3}{2}}=\frac{\sum\limits_{i=1}^n (x-\bar x)^3}{(\sum\limits_{i=1}^n (x-\bar x)^2)^{\frac{2}{3} } }
$$

## 峯度
- [wiki](https://zh.wikipedia.org/wiki/%E5%B3%B0%E5%BA%A6)
- 如果超值峯度為正，稱為尖峯態（leptokurtic）。如果超值峯度為負，稱為低峯態（platykurtic）。

$$
g=\frac{m_4}{m_2^2}-3=\frac{\sum\limits_{i=1}^n (x-\bar x)^4} {(\sum\limits_{i=1}^n (x-\bar x)^2 )^2}-3
$$

- "減3"是為了讓正態分佈的峯度為0

## 相對分散度
- 若有兩組資料而欲比較其相對分散程度時,會使用相對分散度來對比

$$
\text{CV}=\frac{\sigma}{\mu}
$$

## 	異衆比率
- [百度](https://baike.baidu.com/item/%E5%BC%82%E4%BC%97%E6%AF%94%E7%8E%87#:~:text=%E5%BC%82%E4%BC%97%E6%AF%94%E7%8E%87%EF%BC%88variation%20ratio,%E5%8D%A0%E6%80%BB%E9%A2%91%E6%95%B0%E7%9A%84%E6%AF%94%E4%BE%8B%E3%80%82)

$$
V_r=\frac{ (\sum f_i ) -f_m}{\sum f_i}
$$

- 分子是非眾數的頻數和
- 分母是全部眾數的頻數和尸


## 列联表分析
- [知乎參考](https://zhuanlan.zhihu.com/p/24552283)

$$
\sum \sum 
\frac{ 
  ( n_{i,j}- 
      \frac{ n_{i\dot} n_{\dot j} }{n} )^2 
  } 
  {
     \frac{ n_{i\dot} n_{\dot j} {n}
  }
$$


# 一些基本的分佈
## 二次項分佈
- [wiki](https://zh.wikipedia.org/wiki/%E4%BA%8C%E9%A0%85%E5%88%86%E4%BD%88)
- $n$次伯努利分佈

$$f(k,n,p)= \text{Pr}(X=k)=\tbinom {n}{k}(1-p)^{n-k}p^{k} $$

- 平均值和變異數

$$
\text{E}(X)=np,\quad \text{var}(X)=np(1-p)
$$


## 幾何分佈
- [wiki](https://zh.wikipedia.org/wiki/%E5%B9%BE%E4%BD%95%E5%88%86%E4%BD%88)
- 如果每次試驗的成功概率是$p$，那麼$k$次試驗中，第$k$次纔得到第一次成功的概率是，

$$ \text{Pr}(X=k)= (1-p)^{k-1}p $$

- 平均值和變異數

$$
\text{E}(X)=\frac{1}{p},\quad \text{var}(X)=\frac{1-p}{p^2}
$$


## 超幾何分佈
[wiki](https://zh.wikipedia.org/wiki/%E8%B6%85%E5%87%A0%E4%BD%95%E5%88%86%E5%B8%83)
超幾何分佈是統計學上一種離散概率分佈。它描述了由有限個物件中抽出$n$個物件，成功抽出指定種類的物件的個數（不歸還 （without replacement））。

例如在有$N$個樣本，其中$K$個是不及格的。超幾何分佈描述了在該$N$個樣本中抽出$n$個，其中$k$個是不及格的機率：

$$ f(k;n,K,N)=\frac{\tbinom {K}{k} \tbinom {N-K}{n-k} }{\tbinom {N}{n} }$$


上式可如此理解：$\tbinom {N}{n}$ 表示所有在 $N$個樣本中抽出$n$個的方法數目。$\tbinom {K}{k}$表示在$K$個樣本中，抽出$k$個的方法數目，即組合數，又稱二項式係數。剩下來的樣本都是及格的，而及格的樣本有$N-K$個，剩下的抽法便有$\tbinom {N-K}{n-k}$種。

若$n=1$，超幾何分佈還原為伯努利分佈。其中 $k  = 1, 2, 3, ....$

- 平均值和變異數

$$
\text{E}(X)=n\frac{K}{N},\quad \text{var}(X)=n\frac{K(N-K)(N-n)}{N^2(N-1)}
$$

## poisson分佈
- [wiki](https://zh.wikipedia.org/wiki/%E5%8D%9C%E7%93%A6%E6%9D%BE%E5%88%86%E5%B8%83)

$$
\text{Pr}(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}
$$

卜瓦松分佈的母數$\lambda$是單位時間（或單位面積）內隨機事件的平均發生率。

- 平均值和變異數

$$
\text{E}(X)=\lambda,\quad \text{var}(X)=n\lambda 
$$

- 在一個固定時間間隔，或固定範圍內，觀察某一特定事件發生的次數，會發生幾次是一個隨機變數。
- 在二項隨機試驗中，當$n$很大而$p$很小時，我們可以用卜瓦松分配求得二項分配的近似機率值(Simeon D. Poisson(1837), 1781~1840)，此時取
  
  $$
  \lambda=np
  $$


- 我們想像這樣一個白努利隨機試驗，每此投擲銅板的時間間隔是相同的$h$，所以，當$n$很大時，這個投擲實驗像是在一個綿密的持續時間為$nh$的區間內，做觀察某一個特定事件(成功)出現的次數。二項隨機實驗是這$n$伯努利試驗的和，具有
  1. 每一次試驗彼此相互獨立，
  2. 成功的次數與持續時間$nh$ 成正比，
- 這兩點性質滿足前面提到卜瓦松分配三個性質的(a)與(c)。當$p$很小時，這意謂接連兩次正面的機率非常非常地小，也就滿足(b)的性質。以上說明，當$n$很大而$p$很小時，二項隨機實驗的觀察機制非常類似卜瓦松隨機實驗，這也就是為什麼 Poisson(1837)得出可以用卜瓦松分配求得二項分配的近似機率值。 
  
<hr>

# 抽樣
- [reference](https://zh.wikipedia.org/wiki/%E6%8A%BD%E6%A8%A3)
- 分類:
  - 概率抽樣包括有簡單隨機抽樣、系統抽樣（等距抽樣）、分層抽樣（類型抽樣）、整羣抽樣
<div style="text-align:center ;width:500px;" id="image1"><img src="/images/stat/ns8q7pr6pn3243878n7r4snq41rn0372.jpg" /></div>	

## 簡單隨機抽樣(simple random sampling)
<div style="text-align:center;width:300px;" id="image2"><img src="/images/stat/Simple_random_sampling.png" /></div>

在進行抽樣時不摻入任何人為因素。**母體的每一個體都有同等的機會被選中**，且每次抽選與此次之前的歷次抽選無關。在進行此方法時，通常將所觀察的母體內每一個體，加以編號$1-N$，接著隨機地從這$N$個號碼中抽出我們想要的$n$個號碼(即預定的樣本數)。其次找出母體號碼中與這$n$個隨機號碼相同的個體, 這就是選出的樣本。

## 分層抽樣(stratified sampling)
<div style="text-align:center;width:300px;" id="image3"><img src="/images/stat/Stratified_sampling.png" /></div>	

調查的母體，可依某衡量標準，區分成若干個不重複的子母體，我們稱之為『層』，且**層與層之間有很大的變異性，層內的變異性較小**。在區分不同層後，再從每一層中利用簡單隨機抽樣抽出所須比例的樣本數，將所得各層樣本合起來即為樣本。此處的比例就是該層的個體總數佔母體的比例。

## 系統抽樣(systematic sampling)
<div style="text-align:center;width:500px;" id="image4"><img src="/images/stat/Systematic_sampling.png" /></div>	

系統抽樣基本上是隻做一次簡單隨機抽樣後，就採取依固定間隔數抽出一樣本。一般而言，若母體為有限，可將母體依序編號$1,2,\cdots,N$，假設欲選取$n$個樣本，先決定區間間隔$k$，然後以簡單隨機抽樣從$1,2,\cdots,k$中選取一數，此數做為起點，依序每$k$個單位選取一樣本。通常k取為最接近$N/n$的整數。

## 羣集抽樣(cluster sampling)
<div style="text-align:center;width:300px;" id="image5"><img src="/images/stat/muestreo_por_conglomerados.webp" /></div>	

當母體的底冊的蒐集及編造極為困難或龐大，而在調查時又希望節省成本時，可採用此種抽樣。羣集抽樣的方法就是將母體分成幾個羣集(或部落、區域)，而**羣集間的變異小，羣集內的變異大**。再從這幾個羣集中抽出數個羣集進行抽樣或普查。有時羣集抽樣又稱部落抽樣、叢聚抽樣。



## 最大似然  
- 估計算
  - 無偏性、有效性、一致性
邏輯迴歸中常用的篩選變量的方法有
- **Wald test** : 	共線性時Wald檢驗不再有效
- **一個似然比檢驗**


## 數據清理和檢查

- 隨機森林填充缺失值
對於一個有n個特徵的數據來說，其中特徵T有缺失值，我們就把特徵T當作標籤，其他的n-1個特徵和原本的標籤組成新的特徵矩陣。那對於T來說，它沒有缺失的部分，就是我們的Y_test，這部分數據既有標籤也有特徵，而它缺失的部 分，只有特徵沒有標籤，就是我們需要預測的部分。
  - 特徵T不缺失的值對應的其他n-1個特徵 + 本來的標籤：X_train
  - 特徵T不缺失的值：Y_train
  - 特徵T缺失的值對應的其他n-1個特徵 + 本來的標籤：X_test
  - 特徵T缺失的值：未知，我們需要預測的Y_test、
  
- 識別異常值
- 數據標準化
- 聚類法


- 錯誤值（Wrong Value）的處理是在知識發掘處理的**數據清洗**階段。
- 連續變量的缺失值佔比在85%左右時，根據是否缺失，生成指示變量，僅使用指示變量作爲解釋變量

## 統計顯著性

- $H_0$ VS $H_1$採用反證法的邏輯，假設$H_0$是對的，再看有沒有證據反對這個小概率的$H_0$
- 應用了小概率原理
- 不同的問題需要使用不同的檢驗統計量
- 定義拒絕域$\bar W$，通常與$H_1$的$\leq,\geq$ 方向相同，暫時假設 $H_1 : x < 110  $，下面沿用這個$H_1$。
- 顯著水平$\alpha$是一個概率值，
  
  $$ \text{Pr} \{x \in \bar W \}=\alpha ，此時$\bar W=\{ x<x_\alpha \} $$
  
- $\alpha$亦表示原假設爲真時，拒絕原假設的概率。
- p-value:落在與樣本計算出來的參數界限值$x_p$與$\bar W$的同方向的一邊的概率。用數學式表示則是
  
  $$
    p=\text{Pr}\{x<x_p \}
  $$

- 所以當$p\leq\alpha$，即拒絕域
  
  $$\{x<x_p\} \subseteq\bar W$$
  
- **置信水平**$1-\alpha$提高，根據下式，**置信距間變大**

$$\text{Pr}(\text{置信距間})=1-\alpha$$


- 樣本減少，$p$值增大

# 線性迴歸和邏輯迴歸
- [百度百科](https://baike.baidu.com/item/logistic%E5%9B%9E%E5%BD%92)
- [知乎參考](https://zhuanlan.zhihu.com/p/28408516)

- 多重線性識別方法：VIF、散點圖和相關係數矩陣
- 多元線性迴歸中容易出現的問題是 正態分佈問題、異方差問題、異常值問題和共線性問題 

- DW檢測：誤差項自相關或(序列相關)  
  

# 卡方、F、T、正態和ANOVA等檢測

- [T、ANOVA、卡方檢驗和迴歸分別](https://www1.cgmh.org.tw/intr/intr2/ebmlink/doc/%E7%B5%B1%E8%A8%88%E6%95%99%E5%AD%B89411.pdf)

## 卡方

- 卡方：名義測量類型的數據
- 卡方：單個總體的方差檢驗
- 卡方圖形在$y$軸右側
- 總體方差服從卡方分佈

## t驗檢

- 正態性、連續變量、獨立性和方差齊性


## 檢驗正態分佈
- 繪製頻數分佈圖
- 繪製P-P圖
- 進行KS檢驗
- 繪製Q-Q圖

In linear least squares multiple regression with an estimated intercept term,   equals the square of the Pearson correlation coefficient between the observed  and modeled (predicted)  data values of the dependent variable.”在帶有截距項的線性最小二乘多元迴歸中，  等於實測值  和擬合值  的相關係數的平方。注意前面有一串限定條件。



# 主成分分析、因子分析、對應分析等
## 主成份分析(PCA)

-	變化過後的新的特徵，兩兩之間完全獨立
- 新的特徵的方差就是其所對應的特徵值
- 做PCA最好需要做標準化
- 主成分分析關注變量之間的相關關係
- 因子分析關注維度的含義
- 對應分析關注行變量和列變量兩者的相關性。
- 多維尺度分析關注行變量之間的相似性

## 對應分析
- **對應分析**用於兩個**離散型變量**之間的分析
- 能夠分析變量（列）與樣本（行）之間的關係
- 夠分析樣本（行）與樣本（行）之間的關係## 時間序列
- 兩個向量的長度越長，且夾角越小，那麼對應性越強

## 相關分析

- 數據間相互獨立，包括觀測間相互獨立與變量間相互獨立
- 兩列變量均服從正態分佈
- 變量爲連續變量
- 兩變量間的關係是線性的


# 時間序列
- 橫截面數據：橫截面數據是在同一時間，不同統計單位相同統計指標組成的數據列。橫截面數據是按照統計單位排列的。因此，橫截面數據不要求統計對象及其範圍相同，但要求統計的時間相同。也就是說必須是同一時間截面上的數據。
- 橫截面數據要注意異方差問題
- 時間序列數據：在不同時間點上收集到的數據，這類數據反映了某一事物、現象等
- 隨時間的變化狀態或程度。
- 面板數據：是截面數據與時間序列數據綜合起來的一種數據類型。其有時間序列和截面兩個維度，當這類數據按兩個維度排列時，是排在一個平面上，與只有一個維度的數據排在一條線上有着明顯的不同，整個表格像是一個面板,所以把panel data譯作“面板數據”。



- 可以用於分析時間序列數據：差分法、移動平均值法(MA)和自迴歸法(AR)

- 序列本身是非平穩的，通常我們有兩種處理方式，一是進行差分，二是進行對數變換。

ARMA(p,q) 模型
-	時間序列的自相關係數是拖尾的
- 時間序列的偏相關係數是拖尾的