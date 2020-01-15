---
title: 'Run WRF(ARW)'
date: 2017-07-26
permalink: /posts/2017/08/Run_WRF_ARW/
tags:
  - WRF
  - RUN
  - ARW
---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

* [1.  Run real.exe](#1-run-realexe)
	* [a.  Link needed files to my working directory:](#a-link-needed-files-to-my-working-directory)
		* [i. export my working directory](#i-export-my-working-directory)
		* [ii. link neededs files](#ii-link-neededs-files)
	* [b. vim namelist.input](#b-vim-namelistinput)
	* [c . Run geogrid.exe](#c-run-geogridexe)
	* [d.  output](#d-output)
* [2.  Run wrf.exe](#2-run-wrfexe)
	* [a.  for core dump:](#a-for-core-dump)
		* [i set unlimited ram](#i-set-unlimited-ram)
		* [ii vim namelist.input](#ii-vim-namelistinput)
		* [iii. reinstall wrf by vim configure.wrf](#iii-reinstall-wrf-by-vim-configurewrf)
	* [b.  disable cuda](#b-disable-cuda)
	* [c.  Output:](#c-output)

<!-- /code_chunk_output -->




### 1.  Run real.exe

#### a.  Link needed files to my working directory:
##### i. export my working directory
```bash
export WKDIR=/home/chchoi/run_wrf/
export WRF=/home/chchoi/WRFV3
export WPS=/home/chchoi/WPS
```
##### ii. link neededs files
```bash
cd $WRKDIR/wrf
ln -sf $WRF/run/*_DATA -t $WKDIR/wrf
ln -sf $WRF/run/*.TBL -t $WKDIR/wrf
ln -sf $WRF/run/tr* -t $WKDIR/wrf
ln -sf $WRF/run/*.txt -t $WKDIR/wrf
ln -sf $WRF/run/*.tbl -t $WKDIR/wrf
ln -sf $WRF/run/co2* -t $WKDIR/wrf
ln -sf $WRF/main/*.exe -t $WKDIR/wrf
ln -sf $WRF/run/*.formatted -t $WKDIR/wrf
ln -sf $WRF/run/ETAMPNEW_DATA.expanded_rain

cp $WRF/run/namelist.input $WKDIR/wrf
cp $WRF/run/namelist.input $WKDIR/wrf
cp namelist.input namelist.input.org

ln -sf $WRKDIR/wps/met_em.* -t $WKDIR/wrf
```




#### b. vim namelist.input
```bash
num_metgrid_levels = 32, 
num_metgrid_soil_levels = 4, 
num_land_cat = 24, 
sf_surface_physics = 2, 2, 2,
frames_per_outfile = 1000, 1000, 1000,
```



####c . Run geogrid.exe
```bash
./real.exe
```
or
```bash
mpirun -np 4 real.exe
```



#### d.  output
```bash
wrfbdy_d01
wrfinput_d01
wrfinput_d02
```


----


### 2.  Run wrf.exe




#### a.  for core dump:

##### i set unlimited ram
```bash
 ulimit -s unlimited
```
##### ii vim namelist.input
```bash
timestep= 6*$(how many km for dx and dy)
```
##### iii. reinstall wrf by vim configure.wrf
```bash
FCOPTIM = -O2 -fastsse -Mvect=noaltcode -Msmartalloc -Mprefetch=distance:8 -Mfprelaxed # -Minfo=all =Mneginfo=all
FCDEBUG = -g $(FCNOOPT) -C -Ktrap=fp -traceback
```

Ref: for more details, please go to  [Compile WRFV3 via mpif90](https://chchoiw.blogspot.com/2017/07/compile-wrfv3-via-mpif90.html)



#### b.  disable cuda
```bash
mpirun -np 8 --mca mpi_cuda_support 0 wrf.exe
```



#### c.  Output:
```
wrfout_d01_2017-05-21_00:00:00
wrfout_d02_2017-05-21_00:00:00
```
