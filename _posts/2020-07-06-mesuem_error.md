---
title: '澳門通訊博物館網頁理論描述的一些疑惑'
date: 2020-06-23
permalink: /posts/2020/07/museum_error/
tags:
  - Museum Error
category:
  - Museum
---

- [運算放大器展區](#運算放大器展區)
- [模/數轉換器和數/模轉換器展區](#模數轉換器和數模轉換器展區)
- [解像](#解像)
- [直流電路中的電感](#直流電路中的電感)




因為準備澳門[通訊博物館](http://www.cmm.gov.mo/chi/main.html)的考試，瀏覽了它的網頁並嘗試了解它的內容，當中在查找中發現一些不確定的地方。


## 運算放大器展區
[運算放大器展區](http://www.cmm.gov.mo/chi/exhibition/secondfloor/MoreInfo/2_17_1_OpAmpLab.html)
  - 在這個減法放大器， 需要$\frac{R_1}{R_3}=\frac{R_2}{R_4}$，才能有減法的特性，原因請參考[Operational Amplifier Circuits](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-002-circuits-and-electronics-spring-2007/video-lectures/6002_l20.pdf)

  $$
  V_\text{out}=k(V_2-V_1)， \quad \text{here }\quad k=\frac{R_3}{R_1}=\frac{R_4}{R_2}
  $$

  <div style="text-align:center ; width:350px;margin:auto;" id="image2"><img src="/images/meseum/error/2.png" /></div>

  - 在這個加法放在器的電路中 
    1. 正負兩極相反了，原因請參考[Op Amps Positive Feedback](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-002-circuits-and-electronics-spring-2007/video-lectures/6002_l21.pdf)，或者類同的[數/模轉換器](http://www.cmm.gov.mo/chi/Exhibition/secondfloor/moreinfo/ADConverter.html)中的圖2。 
    2. 並且電阻需要有一定的關係$R_5=R_6$才會有

    $$
    V_\text{out}=-k(V_1+V_2)， \quad \text{here } \quad k=\frac{R_7}{R_5}=\frac{R_7}{R_6}
    $$

  <div style="text-align:center; width:350px;margin:auto;" id="image1"><img src="/images/meseum/error/1.png" /></div>



## 模/數轉換器和數/模轉換器展區
-  [模/數轉換器和數/模轉換器展區](http://www.cmm.gov.mo/chi/exhibition/secondfloor/MoreInfo/ADConverter.html)

    <div style="text-align:center; width:350px;margin:auto;"  id="image2"><img style="border: 1px solid grey;" src="/images/meseum/error/5.png" /></div>
    <hr>
    上圖$2n，216$應分別是$2^n，2^{16}$。當初第一次看時，本身沒有基礎概念認為此處的$2n$就是$2\times n$，實際上應是$2^n$。

## 解像
-  [解像](http://www.cmm.gov.mo/chi/exhibition/secondfloor/MoreInfo/2_7_5_Resolution.html)
    <div style="text-align:center; width:350px;margin:auto;" id="image6"><img style="border: 1px solid grey;padding-left:15px;" src="/images/meseum/error/6.png" /></div>
    <hr>
    上圖中，前半段是用<span style="color:red">ppi</span>，後半段是用<span style="color:red">dpi</span>。特意翻查資料，發現通俗來說，dpi與ppi是普遍可互通。當初第一次看時，會想這個dpi前文沒有提起過，是指ppi，還是dpi就是ppi？

## 直流電路中的電感
-  [直流電路中的電感](http://www.cmm.gov.mo/chi/exhibition/secondfloor/MoreInfo/2_3_6_ResistanceInductance.html)
    <div style="text-align:center ; width:350px;margin:auto;" id="image7"><img src="/images/meseum/error/7.png" /></div>
    如上圖所示，當電感與電源斷開後，$V_L$的正負號會相反。某一方面，圖三和圖四的$V_L$方向是同向的，但這一個是放能，一個是儲能，理應是不同方向的。

