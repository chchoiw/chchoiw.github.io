---
title: 'Python Code'
date: 2020-01-20
permalink: /posts/notes/python_code/
---

- [Useful import](#useful-import)
- [Useful python code](#useful-python-code)
  - [Basic](#basic)
  - [Read and write xml](#read-and-write-xml)
  - [Json](#json)
  - [Datetime and seconds since ecoph](#datetime-and-seconds-since-ecoph)
  - [Change output from print screen to terminal](#change-output-from-print-screen-to-terminal)
  - [Read DB to df](#read-db-to-df)
  - [Update or append df to DB](#update-or-append-df-to-db)
  - [Dictionary Skills](#dictionary-skills)
  - [DataFrame Skills](#dataframe-skills)
  - [encode and decode](#encode-and-decode)
  - [Send Email](#send-email)
  - [Try and Except Error:](#try-and-except-error)
  - [Subprocess-Run Command and get responds](#subprocess-run-command-and-get-responds)
  - [Matplotlib](#matplotlib)

# Useful import

1. common
```python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# sysmtem command
import os
import subprocess
from glob import glob
import traceback
import pandas as pd
import numpy as np
import datetime
import time
# timezone
import pytz 
# SQL
import MySQLdb as db
# df insert/append to db
import sqlalchemy
# XML
from lxml import etree
import untangle
# json
import json
# write txt with different encoding
import codecs
from tabulate import tabulate
# math
from math import sin, cos, sqrt, atan2, radians
```
2. matplotlib
```python
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import MaxNLocator
import matplotlib.dates as dates
import matplotlib.ticker as ticker
````


# Useful python code
## Basic
1. Path,base and suffice
ref:
- [link1](https://stackoverflow.com/questions/22272003/what-is-the-difference-between-os-path-basename-and-os-path-dirname)
- [link2](https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python#s)
```python
import os
path='/foo/bar/item.txt'
dirname=os.path.dirname(path)
# dirname='foo/bar'
base_with_suff=os.path.basename(path)
# base_with_suff='item.txt'
base=os.path.splitext(base_suff)[0]
# base='item'
suff=os.path.splitext(base_suff)[1]
# suff='txt'
```
2. list files on the directory
```python
# if directioy=/home/cptmain/
# then filename=*.xml
for filename in os.listdir(directory):
    if filename.endswith(".xml"):
```

3. wirte a file
```python
with open(directory+base+"_respond.txt","w+") as f:
    f.write(output)
f.close()
# write a file with utf8
# display traditional chinese which NOT includes '氹'
with codecs.open(wt_sms_path, 'wb',encoding='utf8') as f:
    f.write(output)
f.close()
# write a file with anscii
# display traditional chinese which includes '氹'
with codecs.open(wt_sms_path, 'wb',encoding='big5hkscs') as f:
    f.write(output)
f.close()
# write a file with anscii
# display traditional chinese which NOT includes '氹'
with codecs.open(wt_sms_path, 'wb',encoding='Big5') as f:
    f.write(output)
f.close()
```
4. write two files
```python
with open('a', 'w') as a, open('b', 'w') as b:
    do_something()
with codecs.open(path, 'wb',encoding='big5hkscs') as f, codecs.open(path2, 'wb',encoding='big5hkscs') as f2:
    f.write(output)
f.close()
```
5. get max and skip null
```python
import numpy as np
ary=[np.nan,1]
np.max(ary)
```


## Read and write xml
ref:[lxm](https://lxml.de/tutorial.html)
String read as xml
```python
respond_xml=etree.fromstring(respond_xml_str)
```

Generate Simple xml
```python
from lxml import etree
root= etree.Element('jds')
account= etree.SubElement(root,'account')
'''
this is set for attribute
'''
account.set("acid", "hutchison"  )
root.append(account)
```
Output:
```xml
<jds>
    <account acid="hutchison">
</jds>
```
Moreover, adding subelement "msg_send" under "account"

```python
msg_send = etree.SubElement(account,'msg_send')
account.append(msg_send)
```


Adding Text in tag:
```python
language=etree.SubElement(msg_send,'language')
language.text='C'
msg_send.append(language)
```

XML to string
```python
xml_str = etree.tostring(root,encoding="UTF-8", \
                        pretty_print=True,\
                        doctype='<!DOCTYPE jds SYSTEM "/home/httpd/html/dtd/jds2.dtd">',\
                        xml_declaration=True)
```
Wite to file with coding utf8
```python
import codecs
with codecs.open(name_file, 'wb',encoding='utf8') as xml:
    xml.write("%s" %xml_str)
xml.close()  
```
Output:
```xml
<?xml version='1.0' encoding='UTF-8'?>
<!DOCTYPE jds SYSTEM "/home/httpd/html/dtd/jds2.dtd">
<jds>
	<account acid="hutchison">
		<msg_send>
			<language>C</language>
		</msg_send>
	</account>
</jds>
```
Read xml as obj
```python
import untangle
# pip install untangle
path="/datacenter/data/zhuhai_warn/publish_440404000000_2019524430_11B03_YELLOW.xml"
obj = untangle.parse(path)
b=obj.ZHwarning.Custom.Warning.Message.cdata
c= b.encode(encoding='UTF-8',errors='strict')
# if you want use var instead of concreat text
key=Message
d=getattr(obj.ZHwarning.Custom.Warning, key)
# d=obj.ZHwarning.Custom.Warning.Message
```

## Json
1. json to dict
ref:[link](https://www.w3schools.com/python/python_json.asp)
```python
import json
    with open(filename, 'r') as f:
        config_dict = json.load(f)
```


2. dict(ary) to json 
```python
json_str=json.dumps(json_obj, indent=4, ensure_ascii=False).encode('utf8')
```
3. json to dict(ary)
```python
respond_ary=json.loads(a) 
```

## Datetime and seconds since ecoph
1. get file updated time: seconds since epoch 
```python
import os
import datetime
import time
file_uptime_epoch=int(os.path.getmtime(file_name))
now_second_epoch=(datetime.datetime.utcnow()- \
    datetime.datetime(1970,1,1)).total_seconds()
# or 
# round to n min
now_second_epoch=(now_second_epoch//(n*60))*n*60
now_second_epoch=time.time()
``` 
2. timestamp transfer to datetime
```python
dt=datetime.datetime.utcfromtimestamp(file_uptime_epoch)
dt=dt+ datetime.timedelta( hours=8)
```
3. common code:
```python 
now_dt=datetime.datetime.utcnow()+ datetime.timedelta( hours=8)
now_dt=now_dt.replace(second=0,microsecond=0)
dt_str=datetime.datetime.strftime(datetime.datetime.utcnow()+ \
                                    datetime.timedelta( hours=8),"%Y-%m-%d %H:%M:00")
```
4. get year/monthe/day/hour/minutes from datetime 
```python
now_dt=datetime.datetime.utcnow()+ datetime.timedelta( hours=8)
now_dt=now_dt.replace(second=0,microsecond=0)
# Year ,type int
yy=now_dt.year
mth=now_dt.month
dd=now_dt.day
hh=now_dt.hour
mn=now_dt.minute
ss=now_dt.second
mirss=now_dt.microsecond
diff_mins=(now_dt-last_check_time).total_seconds()/60
```
5. datetime with utc timezone
```python
import datetime
import pytz
mth="07"
# this is not ok
mth=7
# only integer are possible
nuc_dt=datetime.datetime(yy, mth,dd,hh,mm,0,0,tzinfo=pytz.utc)
```

6. datetime range
```python
idx=pd.date_range(dt, periods=1441,freq='min')
# return DatetimeIndex
```
7. 
```python
date_array= [datetime.datetime.strftime(i, "%Y-%m-%d %H:%M:%S") for i in table_sub.index]
```


## Change output from print screen to terminal
```python
old_stdout = sys.stdout
log_dt=now_dt.strftime('%Y%m%d%H%M')
log_path="%s/log_test/check_alert_%s.txt" %(workdir,log_dt)
log_file = open(log_path,"w+")
sys.stdout = log_file
# at the end of file , back to origion setting
sys.stdout = old_stdout
log_file.close()
```

## Read DB to df
1. read db to df
```python
import MySQLdb as db
import sqlalchemy
def connect_db(config_dict,sql):
    try:
        db_connection = db.connect(host=config_dict["host"], \
                                    db=config_dict["db"], \
                                    user=config_dict["user"] ,\
                                    passwd=config_dict["passwd"] ,\
                                    charset='utf8')
        awsMon_db = pd.read_sql(sql, con=db_connection )
        logic=True
        if awsMon_db.shape[0]==0:
            logic=False
    except :
        logic=False
        awsMon_db=pd.DataFrame()
    return logic,awsMon_db
```

2. read max() form db
```python
def get_max_id(testing_mode):
    db_connection = db.connect(host='mssv08', db='CPTMAIN', user='cptmain' ,passwd='cpt123' ,charset='utf8')
    if testing_mode:
        auto_sms_sql="select max(ID) FROM auto_sms_test"
        return_status_sql="select max(MESSAGE_ID) FROM sms_return_status_test where type='SMARTONE'"
    else:
        auto_sms_sql="select max(ID) FROM auto_sms"
        return_status_sql="select max(MESSAGE_ID) FROM sms_return_status where type='SMARTONE'"
    max_id_df = pd.read_sql(auto_sms_sql, con=db_connection )
    max_msg_id_df = pd.read_sql(return_status_sql, con=db_connection )
    max_id=max_id_df.loc[0,'max(ID)']
    max_msg_id=max_msg_id_df.loc[0,'max(MESSAGE_ID)']
    if  pd.isnull(max_id):    
        max_id=1
    if  pd.isnull(max_msg_id):
        max_msg_id=1000000001
    # print smartone_max_id_df
    max_id =int(max_id )
    return {"max_id":max_id,"max_st_msg_id":max_msg_id}
```



## Update or append df to DB
```python
def insert_db(insert_db,alert_df):
    database_connection = sqlalchemy.create_engine( \
            "mysql://{0}:{1}@{2}/{3}?charset=utf8".format(\
                insert_db["username"], \
                insert_db["passwd"], \
                insert_db["host"], \
                insert_db["db"]) )
    if alert_df.shape[0]>0:
        alert_df.to_sql(con=database_connection,\
             name=insert_db["table"], \
             if_exists=insert_db['if_exists'], \
             index=False )
```
## Dictionary Skills

1. Copy Dictionary
```python
type_dic=dict(filename_msg_dic)
```

2. Get Value
```python
your_dict.values()
all(value == 0 for value in your_dict.values())
```

3. Get Key
```python
your_dict.keys()
```
4. any(all) value is true 
ref:[link](https://stackoverflow.com/questions/35253971/how-to-check-if-all-values-of-a-dictionary-are-0-in-python)
```python
any(value for value in your_dict.values())
all(value for value in your_dict.values())
```

5. loop for dict
```python
for key, value in d.iteritems()
```

6. print dict
```python
import json
cars = {'A':{'speed':70, 'color':2},
        'B':{'speed':60, 'color':3}}
print(json.dumps(cars, indent = 4,ensure_ascii=False, encoding='utf8'))
```


## DataFrame Skills
1. Create Empty DateaFrame
```python
df = pd.DataFrame()
df = pd.DataFrame(columns=['datetime','filename','message'])
```

2. Drop Column of DataFrame
```python
merge_df=merge_df.drop(['INSERT_TIME_GAP_x', 'CHECK_FLAG_x','UPDATE_DATETIME',"ID"], axis=1)   
```

3. Rename Column of DataFrame
```python
station_df.rename(columns={'gps_z': 'BaseLevel'}, inplace=True)
# or
config_df=merge_df.rename(columns={"INSERT_TIME_GAP_y":"INSERT_TIME_GAP",\
                    "CHECK_FLAG_y":"CHECK_FLAG"})
```

4.  Append dict to dataframe
```python
df=df.append({'datetime' : now , \
                'filename' : filename, \
                'message':message} , \
                ignore_index=True)
```
5. Select from dataframe with isin
```python
config_dict=config_df.loc[config_df['TYPE'].isin(['AWS_POWER'])]
```

6. A row of df converts to dict
```python
config_dict=config_df.loc[config_df['TYPE'].isin(['AWS_POWER'])].to_dict('records')[0]
```

7. Set index
```python
wl_info=wl_info.set_index(keys='SiteID')
```
8. Drop the row of which cell includes NAN
```python
st_msgid_recp_df=st_msgid_recp_df.dropna()
```
9. read csv as df
```python
data = pd.read_csv("filename.csv") 
```
10. read db/table as df
```python
try:
    db_connection = db.connect(host='mssv08', db='CPTMAIN', user='cptmain' ,passwd='cpt123' ,charset='utf8')
    last_check_alert_db = pd.read_sql(check_alert_sql, con=db_connection )
    db_connection.close()
except:
    print error_str()
```
11. index drop some elements
```python
#index drop some column
col=col.drop(['a','b'])
```

12. fill nan in col y with value in col x 
```python
merge_df.CHECK_FLAG_y.fillna(merge_df.CHECK_FLAG_x, inplace=True)
```
13. print df with tabulate
```python
#pip install tabulate
from tabulate import tabulate
print tabulate(sms_df, headers='keys', tablefmt='psql',floatfmt=(".0f",".0f",".0f",".0f",".0f"))
```
14. check None and np.nan value
```python
import pandas as pd
thre2=None # (np.nan)
pd.notnull(thre2) #False
pd.isnull(thre2) #True
```

15. DatetimeIndex to an array of native Python datetime objects.
```python
#string to time objects != DatetimeIndex
dt_x =table_sub.index.to_pydatetime()
```
16. Concat two dataframes
```python
pd.concat([table_nan, table_sub2])
```
17. pd reindex
```python
df.reindex(idx,fill_value=np.nan)
```

## encode and decode
```python
audio_path = audio_path.decode("utf8", "strict").encode("ascii", "strict")
file_str = str(file).decode("big5", "strict").encode("utf8", "strict")
```
Try to transfer string to utf-8
```python
try:
    string=unicode(string, "utf-8")
except TypeError:
    pass
```

Writing output as utf8
```python
import codecs
with codecs.open(name_file, 'wb',encoding='utf8') as xml:
xml.close()
```

Writing output as utf8 or ansii
```python
with codecs.open(name_file, 'wb',encoding='big5') as xml:
xml.close()
```

Cannot count the length of uft-8, have to covert unicode
```python
# utf8 to unicode and then count length
msg_unicode=msg.decode("utf8", "strict")
if len(msg_unicode)>=70:
    msg_unicode=msg_unicode[0:65]+"..."
    # convert unicode to utf8
    msg=msg_unicode.encode("utf8", "strict")
```

## Send Email
```python 
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from glob import glob
import datetime
import requests
# send email lib
import smtplib, os, sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from HTMLParser import HTMLParser
import re
from tabulate import tabulate
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
def sd_email(email_dict,receivers_ary):  
    htmlmsgtext=email_dict['htmlmsgtext']
    receivers=receivers_ary
    fromaddr=email_dict['fromaddr']
    host=email_dict['host']
    msgsubject=email_dict['msgsubject']
    replyto = email_dict['fromaddr']
    try:
        msgtext = htmlmsgtext.replace('</br>',"\r").replace('<br />',"\r").replace('</p>',"\r")
        msgtext = strip_tags(msgtext)
        msg = MIMEMultipart()
        msg.preamble = 'This is a multi-part message in MIME format.\n'
        msg.epilogue = ''
        body = MIMEMultipart('alternative')
        body.attach(MIMEText(msgtext))
        body.attach(MIMEText(htmlmsgtext, 'html', 'utf-8'))
        msg.attach(body)
        if 'attachments' in globals() and len('attachments') > 0:
            for filename in attachments:
                f = filename
                part = MIMEBase('application', "octet-stream")
                part.set_payload( open(f,"rb").read() )
                Encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
                msg.attach(part)

        msg.add_header('From', fromaddr)
        msg.add_header('To', "")
    #    msg.add_header('To', toaddr)
        msg.add_header('Subject', msgsubject)
        msg.add_header('Reply-To', replyto)
        msg.add_header('Accept-Language', 'zh-TW')
        msg.add_header('Accept-Language', 'ISO-8859-1,utf-8')
        server = smtplib.SMTP(host)
    #    server = smtplib.SMTP()
    #    server.connect(host)
    #    server.login(user,password)
        server.set_debuglevel(False)
        try:
            server.sendmail(msg['From'], receivers, msg.as_string())
    #        server.sendmail(msg['From'], [msg['To']], msg.as_string())
            print 'Email successfully sent!!'
            server.quit()
        except:
            print 'ERROR: email NOT sent'
    except:
        print ('Email NOT sent to %s successfully. %s ERR: %s %s %s ', 'one of the receivers', 'tete', str(sys.exc_info()[0]), str(sys.exc_info()[1]), str(sys.exc_info()[2]) )
```


## Try and Except Error:
0. define a function call ```error_str()```
```python
import traceback
def error_str():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    error_str="\n"
    for item in traceback.format_exception(exc_type, exc_value,exc_traceback):
        error_str=error_str+item
    return error_str
```
1. send email your error msg
```python
try:
    # your code
except :
    exc_type, exc_value, exc_traceback = sys.exc_info()
    error_str="\n"
    for item in traceback.format_exception(exc_type, exc_value,exc_traceback):
        error_str=error_str+item

    print error_str
    # if not testing_mode:
    if True:
        email_dict={
        'host'        : 'smtp.macau.ctm.net',
        #host       = 'smtp.mtel.net.mo',
        'fromaddr'    : 'cptmain@smg.gov.mo',
        #toaddr     = 'mfleong@smg.gov.mo,tklai@smg.gov.mo',
        #receivers  = ["tklai@smg.gov.mo","mfleong@smg.gov.mo"],

        # receivers = receivers_df["email"].tolist(),
        # print receivers
        # replyto   = fromaddr
        'msgsubject'  : u'(Auto-Mail) rss_policetxt_error',
        }
        receivers_ary=["chchoiw@gmail.com"],
        email_dict['htmlmsgtext']=error_str +"\r\n Location:pwsv04:/home/cptmain/schjobs1/rss_policetxt"
        email.sd_email(email_dict,receivers_ary)
```

## Subprocess-Run Command and get responds
ref:
- [link](https://www.pythonforbeginners.com/os/subprocess-for-system-administrators)
- [link2](https://pythonspot.com/python-subprocess/)
- [link3](https://docs.python.org/2/library/subprocess.html)
>Popen.communicate(input=None)
Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached. Wait for process to terminate. The optional input argument should be a string to be sent to the child process, or None, if no data should be sent to the child.
communicate() returns a tuple (stdoutdata, stderrdata).

```python
import subprocess
cmd=['curl', '-X', 'POST' ,'-H', "'Content-type: text/xml'", '-d', '@%s/three_xml/980__20190605_1227.xml' %ct.workdir, 'http://smsmgr01.three.com.mo/servlet/_xml']
p1 = subprocess.Popen( cmd, stdout=subprocess.PIPE, stdout=subprocess.PIPE )
output=p1.communicate()[0]
err=p1.communicate()[1]
# write output to file
with open(ct.workdir+"/three_xml/980__respond.xml","w+") as f:
    f.write(output)
f.close()
```

or 

```python

with open(path1,"w+") as f, open(path2,"w+") as f2:
    proc = subprocess.Popen(cmd, stdout=f,sterr=f2)
    proc.wait()
    f.seek(0)
    f2.seek(0)
f.close()
f2.close()
```

## Matplotlib
ref: pws04
```bash
/home/cptmain/elsa/slosh_track/draw_track.py
```
1. draw map
```python
from mpl_toolkits.basemap import Basemap
lat_0=22.16
lon_0=113.57
llcrnrlon, llcrnrlat, urcrnrlon, urcrnrlat=106,16,121,24
map = Basemap(projection='merc', \
            lon_0=lon_0, \
            lat_0=lat_0, \
            llcrnrlat=llcrnrlat-0.5,\
            urcrnrlat=urcrnrlat-0.5,\
            llcrnrlon=llcrnrlon+0.5,\
            urcrnrlon=urcrnrlon+0.5,resolution='i')
x_0,y_0=map(lon_0,lat_0)
```

2. draw outline of continents and coastlines:
```python
map.drawcoastlines(linewidth=0.55)
map.fillcontinents(color='coral',lake_color='#e0f8f7')
map.drawmapboundary(fill_color='#e0f8f7')
```


3. draw circle of distance into map
```python
radius_deg=i*1./(111.0*math.cos(math.radians(lat_0)))
map.tissot(lon_0,lat_0,radius_deg,50,facecolor='white',alpha=0.2,linewidth=1.55, linestyle='-',zorder=1) 
```



4. draw data point into map
```python
map.plot(x,y,marker='o',markersize=10,\
        color=track_color,linewidth=2,\
        markeredgewidth=0,zorder=10)
```

5. draw arrow
```python
# arrow located at x_c, y_c
plt.annotate("", xy=(x_c, y_c), xytext=(x[i], y[i]),arrowprops=dict(arrowstyle='-> ,head_length=0.4,head_width=0.2', color=track_color,linewidth=2),fontsize=10,zorder=10)
```

6.draw meridians and parallels
```python
map.drawmeridians(lon, labels=[1, 1, 0, 1],
                    fontsize=10, linewidth=1, fmt=custom_ticks.lon2str)
map.drawparallels(lat, labels=[1, 0, 0, 0],
                    fontsize=10, linewidth=1, fmt=custom_ticks.lat2str)
```
7. draw table data
- rowLabels:column name array
- colWidths:column width array
- cellText: array includes column data
- bbox:[left, bottom, width, height]
```python
rowLabels = ['time','lat', 'lon','central\npressure','storm\nsize']
colWidths=[1./len_sort]*len_sort
cellText = [time_str_ary,lat_sort,lon_sort,c_p_sort,s_s_sort]
the_table = plt.table(cellText=cellText,\
                        rowLoc='center',\
                        rowColours=None, \
                        rowLabels=rowLabels,\
                        colWidths=colWidths,\
                        colLabels=None,loc='bottom',\
                        bbox=[0.0, -0.52, 0.99, 0.45])
```