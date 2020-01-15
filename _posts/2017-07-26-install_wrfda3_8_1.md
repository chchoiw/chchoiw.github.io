---
title: 'Install WRFDA3_8_1'
date: 2017-07-26
permalink: /posts/2017/07/install_wrfda3_8_1/
tags:
  - WRF
  - WRFDA
---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

* [a. vim ~/.bashrc](#a-vim-~bashrc)
* [b.  cd $WRFDA](#b-cd-wrfda)
* [c.  vim your configure.wrf](#c-vim-your-configurewrf)
* [d.  compile](#d-compile)
* [e.  check](#e-check)

<!-- /code_chunk_output -->


### a. vim ~/.bashrc
```bash
export BUFR=1
export CRTM=1
export WRFDA=/home/chchoi/arw/WRFDA
```



### b.  cd $WRFDA
```bash
cd $WRFDA
./configure wrfda
```




### c.  vim your configure.wrf

if your lib path of hdf5 is $HDF5/lib64, please vim your configure.wrf
 /home/chchoi/hdf5/lib64 -lhdf5

### d.  compile
```bash
./compile all_wrfvar >& compile.out &
tail -f compile.out
```



### e.  check
```bash
ls $WRFDA/var/build/*.exe
ls $WRFDA/var/obsproc.exe
```
if there are <span style="color:green">43</span> files in $WRFDA/var/*.exe and <span style="color:green">1</span> file in \$WRFDA/var/obsproc.exe, then WRFDA is installed successfully.

