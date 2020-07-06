---
title: '澳門通訊博物館網頁的一些錯處'
date: 2020-06-23
permalink: /posts/2020/07/museum_error/
tags:
  - Museum Error
category:
  - Museum
---

1. [運算放大器展區](http://www.cmm.gov.mo/chi/exhibition/secondfloor/MoreInfo/2_17_1_OpAmpLab.html)

* 在這個減法放大器, 需要$\frac{R_1}{R_3}=\frac{R_2}{R_4}$,才能有減法的特性([Reference](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-002-circuits-and-electronics-spring-2007/video-lectures/6002_l20.pdf))

<div style="text-align:center" id="image2"><img src="/images/meseum/error/2.png" /><br>圖 1</div>

$$
V_\text{out}=k(V_2-V_1), \quad \text{here } k=\frac{R_3}{R_1}=\frac{R_4}{R_2}
$$


* 在這個加法放在器的電路中, 正負兩極相反了, 並且電阻需要有一定的關係$R_5=R_6$才會有
<div style="text-align:center" id="image1"><img src="/images/meseum/error/1.png" /><br>圖 1</div>
  
$$
V_\text{out}=-k(V_1+V_2), \quad \text{here } k=\frac{R_7}{R_5}=\frac{R_6}{R_5}
$$

