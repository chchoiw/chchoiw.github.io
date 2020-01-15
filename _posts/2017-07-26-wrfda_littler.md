---
title: 'WRFDA little r'
date: 2017-07-26
permalink: /posts/2017/07/wrfda_littler/
tags:
  - WRFDA
  - little r
category:
  - Numerical weather model
---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [little_r](#little_r)
  - [head recorder](#head-recorder)
  - [data record](#data-record)
  - [ending record](#ending-record)

<!-- /code_chunk_output -->

# little_r
For WRFDA, we need to transfer observations to little_r format. What is [little_r](http://www2.mmm.ucar.edu/wrf/users/wrfda/OnlineTutorial/Help/littler.html)?



There are three parts of little_r code.







## head recorder

Basically, there are 44 fields, please see the following graph.



<div class="separator" style="clear: both; text-align: center;"><a href="https://3.bp.blogspot.com/-VVJt_zSO2Ms/XMFbpSCfB7I/AAAAAAAAAAo/xSzeZNyx3W4AGnEb_Uo1_OoYaO_xCI8mgCPcBGAYYCw/s1600/wrfda_obs_22.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://3.bp.blogspot.com/-VVJt_zSO2Ms/XMFbpSCfB7I/AAAAAAAAAAo/xSzeZNyx3W4AGnEb_Uo1_OoYaO_xCI8mgCPcBGAYYCw/s640/wrfda_obs_22.jpg" width="640" height="480" data-original-width="1600" data-original-height="1200" /></a></div>











The fortran code of this format is
```fortran
 a=-888888.0 !(array of dim=13)
 b=0         !(array of dim=13)

 WRITE(101,'(2f20.5,4A40,f20.5,5I10,3L10,2I10,A20,13(f13.5,I7))')&
 lat(r),lon(r),&
 '                                        ',&
 '                                        ',&
 'FM-12 SYNOP                             ',&
 '                                        ',&
 elev(r),-888888,-888888,-888888,&
 i,-888888,is_sound,bogus,discard, & ! 3 logic is False
 -888888,-888888,date(r),& 
 slp(r),0,((a(k),b(k)),k=1,12)
```



## data record




There are 20 fields required. 


From little_r format, if we want to make litter_r format for FM-12 SYNOP, only needed is pressure, height, speed, wind direction, temperature and relative humidity.




| Code       | Obs Type          | Mandatory variables | Optional variables | Unused variables | Notes | 
|------------|-------------------|---------------------|--------------------|------------------|-------| 
| FM‑12<br>FM-14 | SYNOP<br>SYNOP MOBIL | /P and/or H         | Sp,Dr,T,RH†        | Td,U,V,Th        |       | 






<div class="separator" style="clear: both; text-align: center;"><a href="https://4.bp.blogspot.com/-0RU9X3ryPbQ/XMFbpSaUMYI/AAAAAAAAAA0/hYk5v5CPQnE0FRmXahHhOnBDbRIpe1iZgCPcBGAYYCw/s1600/wrfda_obs_24.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://4.bp.blogspot.com/-0RU9X3ryPbQ/XMFbpSaUMYI/AAAAAAAAAA0/hYk5v5CPQnE0FRmXahHhOnBDbRIpe1iZgCPcBGAYYCw/s640/wrfda_obs_24.jpg" width="640" height="480" data-original-width="1600" data-original-height="1200" /></a></div>







The fortran code is
```fortran
 WRITE(101,'(10(F13.5,I7))') p(r),qc,ht(r),qc,temp(r),qc,dp(r),qc,&
 sp(r),qc,dr(r),qc,((a(k),b(k)),k=1,2),rh(r),b(1),a(1),b(1)
```


















## ending record









<div class="separator" style="clear: both; text-align: center;"><a href="https://4.bp.blogspot.com/-OlMRskoYH_0/XMFbpVrR6hI/AAAAAAAAAA0/sQ_7ZocKVk4KB-gAcRRazgVshGPxAj4TACPcBGAYYCw/s1600/wrfda_obs_25.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://4.bp.blogspot.com/-OlMRskoYH_0/XMFbpVrR6hI/AAAAAAAAAA0/sQ_7ZocKVk4KB-gAcRRazgVshGPxAj4TACPcBGAYYCw/s640/wrfda_obs_25.jpg" width="640" height="480" data-original-width="1600" data-original-height="1200" /></a></div>






The fortran code is
```fortran
 WRITE(101,'(10(F13.5,I7))') -777777.,0,-777777.,0,((a(k),b(k)),k=1,8)
 WRITE(101,'(3I7)') 50,0,0
```

Ref: the graphs are from [WRFDA_obs][(https://chchoiw.files.wordpress.com/2017/08/wrfda_obs.pdf](https://drive.google.com/file/d/1-Ji8-LeyFY1tHxOmnskWdma5lTM4Hlql/view?usp=sharing)), which can be [downloaded](http://www2.mmm.ucar.edu/wrf/users/wrfda/Tutorials/2017_July/docs/WRFDA_obs.pdf).







My observation data is xml2 format, so the FORTRAN code for transformation can be [downloaded](https://www.dropbox.com/s/73pnb5kv1w9bh9s/awp2wrf.f90?dl=0) for your reference.









