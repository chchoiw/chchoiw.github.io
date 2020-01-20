---
title: 'Bash Code'
date: 2020-01-20
permalink: /posts/notes/bash_code/
---
- [Bash Code](#bash-code)
  - [show update time](#show-update-time)
  - [Post doc via http](#post-doc-via-http)
  - [show job and kill job](#show-job-and-kill-job)
  - [Create a file and change pression of rw](#create-a-file-and-change-pression-of-rw)
  - [ssh technique](#ssh-technique)
  - [zip folder](#zip-folder)
  - [loop file](#loop-file)
  - [date](#date)
  - [vim set utf-8](#vim-set-utf-8)
  - [vim delete all lines](#vim-delete-all-lines)

# Bash Code
## show update time
- ```stat -c "%y %n"```:``` %y``` get the seconds since epoch

```bash
date -r gen_sms.py +"%Y-%m-%d %H:%M"
# or 
stat -c "%y %n" /datacenter/swfdata/sms/* >& $workdir/fileLoc2txt/sms.txt
```
## Post doc via http 
```bash
cat msg.xml | curl -X POST -H 'Content-type: text/xml' -d @- http://smsmgr01.three.com.mo/servlet/_xml
curl -X POST -H 'Content-type: text/xml' -d @msg.xml http://smsmgr01.three.com.mo/servlet/_xml
```

## show job and kill job
```bash
ps -xu | grep check_alert_direct.py
kill PID
# kill by name
pkill -f /home/cptmain/elsa/gen_sms/check_alert_direct.py
```

## Create a file and change pression of rw
- usually when generate a file by webpage need the following code
```
touch myfile
chmod 777 myfile
```

## ssh technique

1. copy the new key to your server:
ref: [link](https://askubuntu.com/questions/46930/how-can-i-set-up-password-less-ssh-login)
```bash
ssh-keygen
ssh-copy-id user@host
ssh user@host
```

2. copy file
ref: [link](https://unix.stackexchange.com/questions/115560/use-scp-to-transfer-a-file-from-local-directory-x-to-remote-directory-y)
```bash
# local to remote
scp -P 2222 file.ext username@domain:~/ 
# remote to local
scp username@domain:/home/xxx/xxx/11.jpeg /Users/username/Desktop/  
```
3. show remote disk
```bash
ssh ecmfuser@172.16.2.149 df -h /pub >& $workdir/fileLoc2txt/ecmwf.txt
```

## zip folder
```bash
tar -czvf archive.tar.gz /usr/local/something
```


## loop file
```bash
shopt -s dotglob nullglob
a=(/datacenter/data/hko_warn.d/*)
num_file=${#a[@]}
if [ $num_file -gt 0 ]
then
# do someting
fi
```

## date
```bash
if [ $# -eq 0 ]
then
  df=(`date +"%Y %m %d %H 00" --date="-3 days" `)
else
  df=($1 $2 $3 $4 $5)
fi
yyyy=${df[0]}
mm=${df[1]}
dd=${df[2]}
hh=${df[3]}
MM=${df[4]}
sched_time="${yyyy}${mm}${dd}"
```

## vim set utf-8
```bash
:e! ++enc=utf8
```

## vim delete all lines
```bash
gg
dG
# or
:1,$d
```
