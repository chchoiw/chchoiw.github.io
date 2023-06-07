---
title: 'Track Probability'
date: 2023-06-07
permalink: /posts/2023/06/track_probability
tags:
  - track probability
category:
  - 工作成果
---



<!-- <select name="strIndicatorDescription" id="strIndicatorDescription">
    <option value="2023052012">2023052012</option>
    <option value="2023052100">2023052100</option>
    <option value="2023052112">2023052112</option>
    <option value="2023052200">2023052200</option>
    <option value="2023052212">2023052212</option>
    <option value="2023052300">2023052300</option>
    <option value="2023052312">2023052312</option>
    <option value="2023052400">2023052400</option>
    <option value="2023052412">2023052412</option>
    <option value="2023052500">2023052500</option>
</select> -->

## 介紹

- 以下的圖片是由很多條颱風路徑而生成的機率圖, 因為看見此圖, 感覺是很直觀的結果, 所以我試圖在網絡上尋找資料去計算在地圖每格點的機率計算方法, 幸運的是我找到[香港天文台的科普視頻](https://youtu.be/OS0RVNajhto)並以它為起點, 並且使用EC的ensemble的多路徑預測作為數據而生成的颱風機率圖, 以下為比較圖。
- 這個與香港天文台的圖片有些許不一樣, [香港天文台的結果(只有最新颱風的機率圖)](https://www.hko.gov.hk/tc/probfcst/tc_spm.htm)較圓滑(比較如下表),估計是將EC的路徑數據經圓滑變曲線, 再進行機率計算, 這個猜測有機會再檢證。
<table style="width:50%">

  <tr><div style="text-align:center" id="image1"><img src="/images/track_probability/ec/2023052100.png" /></div></tr>
  <tr><div style="text-align:center" id="image1"><img src="/images/track_probability/result/prob_2023052100_MAWAR.png" /></div></tr>
  <tr><div style="text-align:center" id="image1"><img src="/images/track_probability/hko/2023052100.png" /></div></tr>

</table>
- 雖然這個問題並不是困難的,但是計算方法和參考資料也是上述所列舉的,也是本人獨立完成, 沒有任何除上述的提及的資料或前人基礎下完成, 若有雷同, 請諒解本人並不是抄襲。
  




## 圖片比較

- 以下為我用python生成的圖片與[EC的圖片](https://charts.ecmwf.int/products/cyclone?base_time=202305200120&product=tc_strike_probability&unique_id=04W_MAWAR_2023)以2023年瑪娃颱風為例子的比較

<!-- _MAWAR2023052412_MAWAR -->
<table>
  <tr>
    <th>EC</th>
    <th>Result</th>
  </tr>
  <tr>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/ec/2023052012.png" /></div></td>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/result/prob_2023052012_MAWAR.png" /></div></td>
  </tr>
  <tr>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/ec/2023052100.png" /></div></td>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/result/prob_2023052100_MAWAR.png" /></div></td>
  </tr>
  <tr>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/ec/2023052112.png" /></div></td>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/result/prob_2023052112_MAWAR.png" /></div></td>
  </tr>
    <tr>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/ec/2023052200.png" /></div></td>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/result/prob_2023052200_MAWAR.png" /></div></td>
  </tr>


<tr>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/ec/2023052300.png" /></div></td>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/result/prob_2023052300_MAWAR.png" /></div></td>
  </tr>

<tr>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/ec/2023052312.png" /></div></td>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/result/prob_2023052312_MAWAR.png" /></div></td>
  </tr>

<tr>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/ec/2023052400.png" /></div></td>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/result/prob_2023052400_MAWAR.png" /></div></td>
  </tr>

<tr>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/ec/2023052412.png" /></div></td>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/result/prob_2023052412_MAWAR.png" /></div></td>
  </tr>

  <tr>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/ec/2023052500.png" /></div></td>
    <td><div style="text-align:center" id="image1"><img src="/images/track_probability/result/prob_2023052500_MAWAR.png" /></div></td>
  </tr>

</table>
