---
title: 'Temperature and specific humidity'
date: 2017-07-26
permalink: /posts/2017/07/temp_sp/
tags:
  - Temperature
  - Specific humidity
---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->


This is mainly talking about the relation between temperature, relative humidity and specific humidity.



We first clarify some notations:



(a). $q$ specific humidity or the mass mixing ratio of water vapor to total air (dimensionless)



(b). $ w$ mass mixing ratio of water vapor to dry air (dimensionless)



(c). $ e_s(t)$ saturation vapor pressure (hPa)



(d). $ e_{s0}=6.111$ saturation vapor pressure at $ T_0$  (hPa)



(e). $ R_d=287$ specific gas constant for dry air $ (J\cdot  kg^{-1}\cdot  K^{-1})$



(f). $ R_v=461$ specific gas constant for water vapor $ (J \cdot kg^{-1}\cdot  K^{-1})$



(g). $ p$ pressure (hPa)



(h). $ L_v(T)=2.26\cdot 10^6$ specific enthalpy of vaporization $ (J \cdot kg^{-1})$



(i). $ T$ temperature (K)



(j). $ T_0$ reference temperature  (K)







From definition of RH, one knows

$$ \displaystyle RH = \dfrac{e}{e_s}. \ \ \ \ \ (1) $$











From Clausius-Clapeyron, using T with unit K,



$$ \displaystyle e_s(T) = e_{s0}\exp\left[\left(\dfrac{L_v(T)}{R_v}\right)\left(\dfrac{1}{T_0} -\dfrac{1}{T} \right)\right] \approx 6.11\exp\left(\dfrac{17.67(T-T_0)}{T-29.65}\right). \  \ \ \ \ (2) $$



As if one uses T with unit C,

$$ \displaystyle e_s(T) \approx 6.11\exp\left(\dfrac{17.67T}{T-237.3}\right). \ \ \ \ \ (2a)$$



If one applies (2a) to (1),

$$ \displaystyle RH=\frac{\exp\left(\dfrac{17.67Td}{Td-237.3}\right) }{\exp\left(\dfrac{17.67T}{T-237.3}\right) }. $$



where $ Td$ is dewpoint. Given $ RH$ and $ T$, one can also use above formula to get $ Td$.







Applying

$$ \displaystyle P=\rho RT,  \ \ \ \ \ (3) $$



one gets

$$ \displaystyle w = \dfrac{m_v}{m_d}=\dfrac{\rho_v}{\rho_d}=\dfrac{e\ R_d}{R_v(p-e)}. \ \ \ \ \ (4) $$











By (a), (b) ,  specific humidity is defined as.

$$ \displaystyle q = \dfrac{w}{w+1}. \ \ \ \ \ (5) $$



Substitute (4) to (5) , one gets

$$ \displaystyle  q=\frac{\frac{R_d}{R_v}e}{\frac{R_d}{R_v}e+(p-e)}\approx \frac{0.622e}{p-(1-0.622)e}.$$



Given $ RH$, $ T$ and $ P$, one can apply (1) and (2) to get $ e$. Finally, put the calculated $ e$ to above formula, one gets $ q$.







Ref: [link](https://earthscience.stackexchange.com/questions/5076/how-to-calculate-specific-humidity-with-relative-humidity-temperature-and-pres), [link2](https://earthscience.stackexchange.com/questions/2360/how-do-i-convert-specific-humidity-to-relative-humidity)