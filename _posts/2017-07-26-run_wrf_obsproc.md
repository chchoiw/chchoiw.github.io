---
title: 'Run WRF obsproc'
date: 2017-07-26
permalink: /posts/2017/07/run_wrf_obsproc/
tags:
  - WRF
  - RUN
  - obsproc
category:
  - Numerical weather model
---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [install madis-4.3 and MADIS2LITTLER](#install-madis-43-and-madis2littler)
  - [prerequisite: export PATH](#prerequisite-export-path)
  - [1. install madis-4.3, needed netcdf3](#1-install-madis-43-needed-netcdf3)
  - [a. vim $madis-4.3/src/makefile](#a-vim-madis-43srcmakefile)
  - [2. install MADIS2LITTLER](#2-install-madis2littler)
  - [a. vim compile.ksh](#a-vim-compileksh)
  - [b. compile](#b-compile)
  - [3. run MADIS2LITTLER](#3-run-madis2littler)
  - [a. vim run_madis_to_little_r.ksh](#a-vim-run_madis_to_little_rksh)
  - [b.  running madis_to_little_r.ksh](#b-running-madis_to_little_rksh)
  - [4. combine three files together](#4-combine-three-files-together)
  - [5. running obsproc.exe](#5-running-obsprocexe)
  - [a.  copy and link files](#a-copy-and-link-files)
  - [b. vi namelist.obsproc](#b-vi-namelistobsproc)
  - [c. Run obsproc.exe](#c-run-obsprocexe)

<!-- /code_chunk_output -->





Using MADIS observations


[MADIS obs website](https://madis.ncep.noaa.gov/)
[MADIS obs download](https://madis-data.ncep.noaa.gov/madisPublic1/data/)





#  install madis-4.3 and MADIS2LITTLER

## prerequisite: export PATH

```bash
 export DAT_DIR=/home/chchoi/arw/wrfda_test
 export WRFDA=/home/chchoi/arw/WRFDA
 export WRKDIR=/home/chchoi/arw/wrf_run

```

[MADIS2LITTLER download](http://www2.mmm.ucar.edu/wrf/users/wrfda/download/madis.html)
[MADIS-4.3 download](https://madis.ncep.noaa.gov/madis_api.shtml)

We mainly  transfer MADIS natural netcdf files to LITTLE_R format via MADIS2LITTLER. And installing MADIS2LITTLER needs library madis.











## 1. install madis-4.3, needed netcdf3


## a. vim $madis-4.3/src/makefile
```bash
 NETCDF_INC=/home/chchoi/netcdf3/include/
 NETCDF_LIB=/home/chchoi/netcdf3/lib/libnetcdf.a
 #
 #
 # Linux and Windows-Cygwin or Windows-MinGW (all 3 use g77 compiler)
 # ------------------------------------------------------------------
 #
 #FC=g77
 #FC=gfortran
 FC=pgf90
 #FC=mpif90
 #FFLAGS=-Wno-globals
 FFLAGS=-O
 LDFLAGS=
```



## 2. install MADIS2LITTLER


## a. vim compile.ksh

```bash
MADIS_EXTERNAL=/home/chchoi/x64/madis/lib/
NETCDF_LIB=/home/chchoi/x64/netcdf3/lib/
```

## b. compile
```bash
./compile.ksh pgf90
```


## 3. run MADIS2LITTLER


##  a. vim run_madis_to_little_r.ksh

```bash
 export MADIS_DATA=/home/chchoi/raw_data/madis 
 # where to put madis obs files

 export MADIS_STATIC=/home/chchoi/x64/madis/static/ 
 # where to put madis library

 export METAR=TRUE
 export MARINE=TRUE
 export GPSPW=FALSE
 export ACARS=TRUE
 export RAOB=TRUE
 export NPN=FALSE
 export MAP=FALSE
 export SATWND=TRUE
 #usually meter and marine are enough

 SDATE=2017061200
 EDATE=2017061212
 INTERVAL=12

 CODE_DIR=/home/chchoi/x64/MADIS2LITTLER/
 # where to install MADIS2LITTLER

 MADIS2LITTLE_R_DIR=${MADIS_DATA}/little_r_obs
 # where to put transformed little_r obs files
```







## b.  running madis_to_little_r.ksh

```bash
./madis_to_little_r.ksh
```







## 4. combine three files together

```bash
cat RAOB_LITTLE_R_2017-06-12_16 METAR_LITTLE_R_2017-06-12_16 SHIP_LITTLE_R_2017-06-12_16 >& obs.2017061216
```







 



 







## 5. running obsproc.exe








## a.  copy and link files

```bash
 cp $WRFDA/var/obsproc/namelist.obsproc.3dvar.wrfvar-tut namelist.obsproc
 cp $WRFDA/var/obsproc/obserr.txt .
 cp $WRFDA/var/obsproc/msfc.tbl .
 ln -sf $WRFDA/var/obsproc/obsproc.exe .
```







## b. vi namelist.obsproc

```
&record1
 obs_gts_filename = 'obs.2017061212'
 obs_err_filename = 'obserr.txt',
 fg_format = 'WRF'
 gts_from_mmm_archive = .false.,
 /

&record2
 time_window_min = '2017-06-12_06:00:00',
 time_analysis = '2017-06-12_12:00:00',
 time_window_max = '2017-06-13_00:00:00',
 /

&record3
 max_number_of_obs = 400000,
 fatal_if_exceed_max_obs = .TRUE.,
 /

&record4
 qc_test_vert_consistency = .TRUE.,
 qc_test_convective_adj = .TRUE.,
 qc_test_above_lid = .TRUE.,
 remove_above_lid = .false.,
 domain_check_h = .true.,
 Thining_SATOB = .false.,
 Thining_SSMI = .false.,
 Thining_QSCAT = .false.,
 calc_psfc_from_qnh = .true.,
 /

&record5
 print_gts_read = .TRUE.,
 print_gpspw_read = .TRUE.,
 print_recoverp = .TRUE.,
 print_duplicate_loc = .TRUE.,
 print_duplicate_time = .TRUE.,
 print_recoverh = .TRUE.,
 print_qc_vert = .TRUE.,
 print_qc_conv = .TRUE.,
 print_qc_lid = .TRUE.,
 print_uncomplete = .TRUE.,
 /

&record6
 ptop = 1000.0,
 base_pres = 100000.0,
 base_temp = 290.0,
 base_lapse = 50.0,
 base_strat_temp = 215.0,
 base_tropo_pres = 20000.0
 /

&record7
 IPROJ = 1,
 PHIC = 22.2,
 XLONC = 113.54417,
 TRUELAT1= 30.0,
 TRUELAT2= 60.0,
 MOAD_CEN_LAT = 22.2,
 STANDARD_LON = 120.00,
 /

&record8
 IDD = 1,
 MAXNES = 1,
 NESTIX = 50, 200, 136, 181, 211,
 NESTJX = 50, 200, 181, 196, 211,
 DIS = 16, 10., 3.3, 1.1, 1.1,
 NUMC = 1, 1, 2, 3, 4,
 NESTI = 1, 40, 28, 35, 45,
 NESTJ = 1, 60, 25, 65, 55,
 /
```







## c. Run obsproc.exe

```bash
./obsproc.exe
```

this will get obs_gts_2017-06-12_12:00:00.

