
---
title: 'Radar ingest into LAPS'
date: 2017-07-26
permalink: /posts/2017/07/lap_radar_ingest/
tags:
  - LAPS
  - RADAR
category:
  - Numerical weather model
---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

* [A. Revise $TEMPLATE/remap.nl](#a-revise-templateremapnl)
* [B.  run remap_polar_netcdf.exe](#b-run-remap_polar_netcdfexe)
	* [1. Run systime.pl](#1-run-systimepl)
	* [2.  run remap_polar_netcdf.exe](#2-run-remap_polar_netcdfexe)
	* [3.  check](#3-check)
		* [a. log files:](#a-log-files)
		* [b.  output files for running remap_polar_netcdf.exe](#b-output-files-for-running-remap_polar_netcdfexe)
	* [4. run shced.pl which includes "mosaic_radar.x"](#4-run-shcedpl-which-includes-mosaic_radarx)
		* [a. run sched.pl](#a-run-schedpl)
		* [b. check](#b-check)
	* [5. remark :](#5-remark)
		* [a. run remap_polar_netcdf.exe again](#a-run-remap_polar_netcdfexe-again)
		* [b.  v01 is not netcdf file](#b-v01-is-not-netcdf-file)

<!-- /code_chunk_output -->


Assume having suitable netcdf format radar files, that is **"Polar netcdf File"** in the following figure, then we can run **remap_polar_netcdf.exe** to get "VXX" files.



After that, we run shced.pl which includes **"mosaic_radar.x"** to complete the analysis progress.


<div class="separator" style="clear: both; text-align: center;"><a href="https://1.bp.blogspot.com/-EjATYE-EuzI/XMF8Dg9ElmI/AAAAAAAAABA/Z6wtTKtxrm0kSj1akDtBgoN8VCR1w6FmACPcBGAYYCw/s1600/laps_radar.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://1.bp.blogspot.com/-EjATYE-EuzI/XMF8Dg9ElmI/AAAAAAAAABA/Z6wtTKtxrm0kSj1akDtBgoN8VCR1w6FmACPcBGAYYCw/s640/laps_radar.jpg" width="640" height="564" data-original-width="613" data-original-height="540" /></a></div>


### A. Revise $TEMPLATE/remap.nl


set path to where you placed radar nimbus netcdf files
```bash 
path_to_radar_a='/home/chchoi/raw_data/radar/ZA'
```


### B.  run remap_polar_netcdf.exe

#### 1. Run systime.pl


In order to run "remap_polar_netcdf.exe", we have to revise time file in \$LAPS_ROOT_DATA/time/ via \$LAPSINSTALLROOT/etc/systime.pl
```bash
perl $LAPSINSTALLROOT/etc/systime.pl 16 08 01 19 00 > $LAPS_DATA_ROOT/time/systime.dat
```



#### 2.  run remap_polar_netcdf.exe

```bash
perl $LAPSINSTALLROOT/etc/laps_driver.pl remap_polar_netcdf.exe $LAPSINSTALLROOT $LAPS_DATA_ROOT
```







#### 3.  check


##### a. log files:


there will be log file in $LAPS_ROOT_DATA/log/remap_polar_netcdf.log.XXXX

##### b.  output files for running remap_polar_netcdf.exe


if there are data in the folder $LAPS_ROOT_DATA/lapsprd/v01-vXXX, that means you are successful







#### 4. run shced.pl which includes "mosaic_radar.x"


##### a. run sched.pl

```bash
perl $LAPSINSTALLROOT/etc/sched.pl -A 01-Aug-2016-1900 $LAPSINSTALLROOT $LAPS_DATA_ROOT
```

##### b. check


if there are data in the folder $LAPS_ROOT_DATA/lapsprd/vrz, that means you are successful







#### 5. remark :


##### a. run remap_polar_netcdf.exe again

If having already the file in v01-vXXX, we cannot run "remap_polar_netcdf.exe" again.

Hence, if one wants to run "remap_polar_netcdf.exe" again, please delete them.

##### b.  v01 is not netcdf file


if we would like to have v01 is netcdf format, please revise nest7grid.parms
```bash
l_compress_radar=.true.,
```

to get netcdf version V01 files.







 



 



 