---
title: 'Run WRF(NMM)'
date: 2017-07-26
permalink: /posts/2017/07/run_wrf_nmm/
tags:
  - WRF
  - NMM
  - RUN
category:
  - Numerical weather model
---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [run geogrid.exe](#run-geogridexe)
    - [My working directory:](#my-working-directory)
    - [vim namelist.wps with geogrid and metgrid parts respectively.](#vim-namelistwps-with-geogrid-and-metgrid-parts-respectively)
    - [Run geogrid.exe](#run-geogridexe-1)
    - [output](#output)
- [Run ungrib.exe](#run-ungribexe)
    - [Locations:](#locations)
    - [link NAM grib files and ungrib Vtable (for nmm)](#link-nam-grib-files-and-ungrib-vtable-for-nmm)
    - [Output:](#output-1)
- [Run metgrid.exe](#run-metgridexe)
    - [Output:](#output-2)

<!-- /code_chunk_output -->





For NMM, I only tried the official test data.



## run geogrid.exe


####  My working directory:

```bash
export WKDIR=/home/chchoi/domains/boston/
ln -sf ~/WPS/*.exe -t $WKDIR/wpsprd
ln -sf ~/WPS/link_grib.csh
cp ~/WPS/namelist.wps $WKDIR/wpsprd
cp ~/WPS/geogrid/GEOGRID.TBL.NMM ~/WPS/geogrid/GEOGRID.TBL
cp ~/WPS/metgrid/METGRID.TBL.NMM ~/WPS/metgrid/METGRID.TBL
```


#### vim namelist.wps with geogrid and metgrid parts respectively.

```bash
opt_geogrid_tbl_path = '/home/chchoi/WPS/geogrid/'
opt_metgrid_tbl_path = '/home/chchoi/WPS/metgrid/'
```

> Remark: METGRIDTBL is for running metgrid.exe section


####  Run geogrid.exe

```bash
./geogrid.exe
```

or
```bash
mpirun -np 4 geogrid.exe
```

####  output

```bash
geo_em.d01.nc, geo_em.d02.nc
```

##  Run ungrib.exe








####  Locations:
The locations I put NAM files is ~/NAM and I installed WPS at ~/WPS. Just revised for your own location.


#### link NAM grib files and ungrib Vtable (for nmm) 
link NAM grib files and ungrib Vtable (for nmm) to $WRKDIR. Then run ungrib.exe

```bash
./link_grib.csh ~/NAM/20050123_i00_f0
 ln -sf ~/WPS/ungrib/Variable_Tables/Vtable.NAM Vtable
./ungrib.exe >& ungrib.log
```



####  Output:

geo_em.d01.nc, geo_em.d02.nc


## Run metgrid.exe

```bash
 cp ~/WPS/metgrid/METGRID.TBL.NMM ~/WPS/metgrid/METGRID.TBL
 ./metgrid.exe
```

#### Output:

met_em.d01.2017-05-21_00:00:00.nc

