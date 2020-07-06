---
title: '澳門通訊博物館網頁的一些錯處'
date: 2020-06-23
permalink: /posts/2020/07/museum_error/
tags:
  - Museum Error
category:
  - Museum
---

- [運算放大器展區](http://www.cmm.gov.mo/chi/exhibition/secondfloor/MoreInfo/2_17_1_OpAmpLab.html)

* 在這個減法放大器, 需要$\frac{R_1}{R_3}=\frac{R_2}{R_4}$,才能有減法的特性([Reference](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-002-circuits-and-electronics-spring-2007/video-lectures/6002_l20.pdf))

<div style="text-align:center" id="image2"><img src="/images/meseum/error/2.png" /></div>

$$
V_\text{out}=k(V_2-V_1), \quad \text{here } k=\frac{R_3}{R_1}=\frac{R_4}{R_2}
$$


* 在這個加法放在器的電路中 
<div style="text-align:center" id="image1"><img src="/images/meseum/error/1.png" /></div>
  * 正負兩極相反了,原因請參考[Op Amps Positive Feedback](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-002-circuits-and-electronics-spring-2007/video-lectures/6002_l21.pdf)  
  * 並且電阻需要有一定的關係$R_5=R_6$才會有

$$
V_\text{out}=-k(V_1+V_2), \quad \text{here } k=\frac{R_7}{R_5}=\frac{R_6}{R_5}
$$

-  [模/數轉換器和數/模轉換器展區](http://www.cmm.gov.mo/chi/exhibition/secondfloor/MoreInfo/ADConverter.html)

<div style="text-align:center" id="image2"><img src="/images/meseum/error/5.png" /></div>

上圖$2n,216$應分別是$2^n,2^{16}$。因為第一次看時, 本身沒有基礎會真的認為此處的$2n$就是$2\times n$,會引致誤會。

-  [解像](http://www.cmm.gov.mo/chi/exhibition/secondfloor/MoreInfo/2_7_5_Resolution.html)
<div style="text-align:center" id="image6"><img src="/images/meseum/error/6.png" /></div>

上圖中, 前半段是用<span style="color:red">ppi</span>,後半段是用<span style="color:red">dpi</span>。雖然查閱資料,dpi與ppi是普遍可互通, 但對於初接觸這些概念的人, 會很容易混淆。


