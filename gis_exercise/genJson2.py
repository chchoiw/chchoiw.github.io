
# coding: utf8
import pandas as pd
import numpy as np
import json
from scipy import signal
import operator
import math
import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging
import matplotlib.pyplot as plt
import mysql.connector as connection
import pandas as pd
import datetime
import traceback
import os
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)
workdir="/srv/www/htdocs/gis_exercise/"
# https://www.giserdqy.com/secdev/leaflet/18166/
# https://www.zhihu.com/question/41690082
# https://github.com/sknightq/sknight-gis

longlatData={
    "CC": [113.5786111111111, 22.13722222222222],
    "DC": [113.55111111111111,22.11722222222222],
    "DP": [113.54333333333334,22.21527777777778],
    "EM": [113.56,22.20722222222222],
    "FM": [113.54222222222222,22.197222222222223],
    "JA": [113.5425,22.154999999999998],
    "KV": [113.58027777777778,22.134722222222223],
    "MM": [113.53055555555555,22.185833333333335],
    "PE": [113.55833333333334,22.196666666666665],
    "PG": [113.54166666666667,22.180833333333336],
    "PN": [113.56,22.191666666666666],
    "PS": [113.56,2.1816666666666666],
    "PV": [113.534722222222221,22.175555555555558],
    "TG": [113.56861111111111,22.159444444444443],
    "ZM":[113.58031944444444,22.199275],
    "UM":[113.54694444444445,22.131666666666668],
    "CG":[113.55101111111111,22.197644444444446]
    
}

longlatGridDict={
        "lo1": 113.5090,
        "la1": 22.2235,
        "lo2": 113.5947,
        "la2": 22.1034,
        "nx":20,
        "ny":32,
}
longlatGridDict["dx"]=(longlatGridDict["lo2"]-longlatGridDict["lo1"])/longlatGridDict["nx"]
longlatGridDict["dy"]=(longlatGridDict["la1"]-longlatGridDict["la2"])/longlatGridDict["ny"]
# example.geojson


wlLongLatData={
    "LPM":[ 113.5344444, 22.18944444],
    "LHK":[ 113.5377778, 22.19694444],
    "LMF":[ 113.5466667, 22.21138889],
    "LAO":[ 113.5486111,22.1575],
    'LCH':[ 113.5505556,  22.15777778,],
    'LIL':[ 113.5594444,  22.15583333,],
    'LCS':[ 113.5575000,  22.15472222,],
    'LSP':[ 113.5627778,  22.13166667,],
    "LPI":[ 113.5363889,  22.19805556,],
    'LSI':[ 113.5369444,  22.19972222,],
    
    'LRR':[113.5447222,   22.20250000],
    'LIV':[113.5352778,   22.21222222],
    'LCL':[113.5511111,   22.11722222],
    'LLM':[113.5377778,   22.20333333],
    'LTA':[113.5430556,   22.20194444],
    'LPH':[113.5350000,   22.19333333],
    'LPN':[113.5563889,   22.15444444],
    'LMM':[113.5448000,   22.20530000],
    'LPF':[113.5327230,   22.19049000],
    "LP1":[113.5368280,   22.19905200],
    
    'LPS':[22.190490, 113.532723], 
}
id2Sation={
    "01":"LPM",
    "02":"LHK",
    "03":"LMF",
    "04":"LAO",
    "05":"LCH",
    "06":"LIL",
    "07":"LCS",
    "08":"LSP",
    "09":"LPI",
    "10":"LSI",
    "11":"LRR",
    "12":"LIV",
    "13":"LCL",
    "14":"LLM",
    "15":"LTA",
    "16":"LPH",
    "17":"LPN",
    "18":"LMM",
    "19":"LPF",
    "20":"LP1",
    "99":"LPS",
    
}


nowdt=(datetime.datetime.now()+datetime.timedelta(hours=8,minutes=-1))
nowdtStr=nowdt.strftime("%Y-%m-%d %H:%M:00")
nowdt24hoursAgo=nowdt+datetime.timedelta(hours=-24)
nowdt24hoursAgoStr=nowdt24hoursAgo.strftime("%Y-%m-%d %H:%M:00")
# try:
#     mydb = connection.connect(host="mssv01.smg.net", database = 'AWS',user="", passwd="")
#     query = "SELECT OBS_DATETIME,STATIONCODE,TEMP,HUMI,WSPD,WDIR,WSPD_10, WDIR_10 FROM AWS.min_tab1 where obs_datetime=%s order by obs_datetime desc limit 50;" %nowdt
#     awsData= pd.read_sql(query,mydb)
#     print(awsData)   
#     mydb.close() #close the connection
# except Exception as e:
#     # mydb.close()
#     print(str(e))
# "refTime": "2014-11-30T06:00:00.000Z",
####################################
# aws station time series for each location
#####################################
mydb = connection.connect(host="mssv01.smg.net", database = 'AWS',user="cptmain", passwd="",use_pure=True,charset='utf8')
for stationcode in longlatData.keys():
    queryTimeSeries = "SELECT OBS_DATETIME,STATIONCODE,TEMP,HUMI,WSPD_10, WDIR_10 FROM AWS.min_tab1 where obs_datetime>='%s' and obs_datetime< '%s'  and STATIONCODE='%s';" %(nowdt24hoursAgoStr,nowdtStr,stationcode)
    awsTimeSeriesData= pd.read_sql(queryTimeSeries,mydb)  
    awsTimeSeriesData["OBS_DATETIME"] = awsTimeSeriesData["OBS_DATETIME"].dt.strftime('%Y-%m-%d %H:%M:%S')
# .apply(lambda x: x.timestamp.dt.strftime('%Y-%m-%d %H:%M:%S'))


    awsJson=awsTimeSeriesData.to_dict(orient='records')
    awsString2 = json.dumps({0:awsJson}, cls=NpEncoder)

    with open(workdir+"awsData/stationTimeSeries/"+stationcode+".json", "w") as awsJsonFile:
        awsJsonFile.write(awsString2)
    # awsTimeSeriesData.to_csv("TG.csv",index=False)
    awsJsonFile.close()






    #close the connection
# print(awsTimeSeriesData)
# awsData=pd.read_csv("aws.csv",index_col="STATIONCODE")




####################################
# wl station newest data
#####################################
nowdtWL=(nowdt-datetime.timedelta(minutes=1))
nowdtStrWL=nowdtWL.strftime("%Y-%m-%d %H:%M:00")
mydb = connection.connect(host="mss004.smg.net", database = 'ftgms',user="cptmain", passwd="Idced@11ic",use_pure=True,charset='utf8')
# query = "SELECT OBS_DATETIME,STATIONCODE,TEMP,HUMI,WSPD,WDIR,WSPD_10, WDIR_10 FROM AWS.min_tab1 where obs_datetime='%s' order by obs_datetime desc limit 50;" %nowdtStr

# nowdtStrWL="2023-07-17 10:00:00"
# nowdtStr="2023-07-17 10:01:00"
# query="SELECT * FROM ftgms.sitedata where datetime>='"+nowdtStrWL+"' and datetime< '"+nowdtStr+"';"
query="select row.OBS_DATETIME as datetime, round((row.reference_water_level - station.gps_z)/1000.0,2) as level,row.station_id from NO_WATER_LEVEL_VFTGMS_RAW as row left join station on row.station_id = station.serial_no where row.OBS_DATETIME between '"+nowdtStrWL+"' and  '"+nowdtStr+"' order by OBS_DATETIME desc;"

wlData= pd.read_sql(query,mydb)

stationAryWL=[]
for i in wlData.index:
    statCode=id2Sation[wlData.loc[i,"station_id"]]
    wlData.loc[i,"STATIONCODE"]=statCode
    wlData.loc[i,"long"]=wlLongLatData[statCode][0]
    wlData.loc[i,"lat"]=wlLongLatData[statCode][1]
    wlData.loc[i,"FloodingLevel"]=wlData.loc[i,"level"]*100
    tmpDict={
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [wlData.loc[i,"long"],wlData.loc[i,"lat"]],
        },
        "properties": {
            "wl":wlData.loc[i,"FloodingLevel"],
            "name":statCode
        }
        }
    stationAryWL.append(tmpDict)
    # wlData.loc[i,"FloodingLevel"]*1000
wlData=wlData.set_index('STATIONCODE')

############
# all station latest data
#########
stationStringWL=json.dumps({0:stationAryWL}, cls=NpEncoder)
with open(workdir+"wlData/stationPoint/stationWL.json", "w") as stationFileWL:
    stationFileWL.write(stationStringWL)    
stationFileWL.close()    



####################################
# wl station 24h time series
#####################################

for stationcode in id2Sation.keys():
    # queryTimeSeries = "SELECT OBS_DATETIME,STATIONCODE,TEMP,HUMI,WSPD_10, WDIR_10 FROM AWS.min_tab1 where obs_datetime>='%s' and obs_datetime< '%s'  and STATIONCODE='%s';" %(nowdt24hoursAgoStr,nowdtStr,stationcode)
    queryTimeSeries ="select row.OBS_DATETIME as OBS_DATETIME, round((row.reference_water_level - station.gps_z)/1000.0,2) as wl,row.station_id from NO_WATER_LEVEL_VFTGMS_RAW as row left join station on row.station_id = station.serial_no where (row.OBS_DATETIME between '"+nowdt24hoursAgoStr+"' and  '"+nowdtStr+"') and station.serial_no='"+stationcode+"';"

    wlTimeSeriesData= pd.read_sql(queryTimeSeries,mydb)  
    try:
        wlTimeSeriesData["OBS_DATETIME"] = wlTimeSeriesData["OBS_DATETIME"].dt.strftime('%Y-%m-%d %H:%M:%S')
    except:
        traceback.print_exc()
# .apply(lambda x: x.timestamp.dt.strftime('%Y-%m-%d %H:%M:%S'))


    wlJson=wlTimeSeriesData.to_dict(orient='records')
    wlString2 = json.dumps({0:wlJson}, cls=NpEncoder)

    with open(workdir+"wlData/stationTimeSeries/"+id2Sation[stationcode]+".json", "w") as wlJsonFile:
        wlJsonFile.write(wlString2)
    # awsTimeSeriesData.to_csv("TG.csv",index=False)
    wlJsonFile.close()
mydb.close()  







def awsDataHandle(nowdt,stationOutputFlag=True,fileNameWithTime=True):
    reftime=nowdt.strftime("%Y-%m-%dT%H:%M:00.000Z")
    nowdtStr = nowdt.strftime("%Y-%m-%d %H:%M:00")
    mydb = connection.connect(host="mssv01.smg.net", database = 'AWS',user="cptmain", passwd="",use_pure=True,charset='utf8')
    query = "SELECT OBS_DATETIME,STATIONCODE,TEMP,HUMI,WSPD,WDIR,WSPD_10, WDIR_10 FROM AWS.min_tab1 where obs_datetime='%s' order by obs_datetime desc limit 50;" %nowdtStr

    # 2023-07-17 10:00
    awsData= pd.read_sql(query,mydb)
    awsData=awsData.set_index('STATIONCODE')


    # print(round(math.sin(180*math.pi/180),7),math.cos(180*math.pi/180))
    stationAry=[]

    for i in awsData.index:
        # stat=awsData.loc[i,"STATIONCODE"]
        stat=i
        if stat in longlatData:
            awsData.loc[i,"long"]=longlatData[stat][0]
            awsData.loc[i,"lat"]=longlatData[stat][1]
            md=270-awsData.loc[i,"WDIR_10"]
            rad=md*math.pi/180
            awsData.loc[i,"v"]=awsData.loc[i,"WSPD_10"]*math.sin( rad)
            awsData.loc[i,"u"]=awsData.loc[i,"WSPD_10"]*math.cos( rad) 
            awsData.loc[i,"WSPD_10"]=awsData.loc[i,"WSPD_10"]
            # if i not in stationAry:
            if  np.isnan(awsData.loc[i,"TEMP"]):
                temp=-999
            else:
                temp=awsData.loc[i,"TEMP"]
            if  np.isnan(awsData.loc[i,"HUMI"]):
                humi=-999
            else:
                humi=awsData.loc[i,"HUMI"]
            tmpDict=        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [awsData.loc[i,"long"],awsData.loc[i,"lat"]],
            },
            "properties": {
                "TEMP": temp,
                "WSPD_10": awsData.loc[i,"WSPD_10"],
                "WDIR_10": awsData.loc[i,"WDIR_10"],
                "HUMI":humi,
                "name":i
            }
            }
            stationAry.append(tmpDict)
                                    
    awsData = awsData.dropna(subset=['long', 'lat'])
    awsList=awsData[["long","lat","WSPD_10","WDIR_10"]].values.tolist()
    awsString = json.dumps({0: awsList}, indent=4, cls=NpEncoder)
    
    ############
    # windbarb station data
    ###########
    filenameDTStr=nowdt.strftime("%Y%m%d%H")
    if stationOutputFlag:
        if fileNameWithTime:
            with open(workdir+"awsData/stationPoint/windbarb_"+filenameDTStr+".json", "w") as awsFile:
                awsFile.write(awsString)
            # print(stationAry)
            stationString = json.dumps({0:stationAry}, indent=4, cls=NpEncoder)

            with open(workdir+"awsData/stationPoint/station_"+filenameDTStr+".json", "w") as stationFile:
                stationFile.write(stationString)
            stationFile.close()
        else:
            with open(workdir+"awsData/stationPoint/windbarb.json", "w") as awsFile:
                awsFile.write(awsString)
            # print(stationAry)
            stationString = json.dumps({0:stationAry}, indent=4, cls=NpEncoder)

            with open(workdir+"awsData/stationPoint/station.json", "w") as stationFile:
                stationFile.write(stationString)
            stationFile.close()
              
    

    
    return awsData





    # stationAryWL
def calDist( lat1,lon1,lat2,lon2):
    R = 6371000; # metres
    phi1 = lat1 * math.pi/180 # phi, lambda in radians
    phi2 = lat2 * math.pi/180
    deltaPhi = (lat2-lat1) * math.pi/180
    deltaLambda = (lon2-lon1) * math.pi/180

    a = math.sin(deltaPhi/2) * math.sin(deltaPhi/2)+ \
        math.cos(phi1) * math.cos(phi2) *\
        math.sin(deltaLambda/2) * math.sin(deltaLambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    d = R * c # in metres   
    return d,c 

####################################
# aws station calculte for contour 
# each loop is a hour,total 24 h
#####################################

def awsContourGen(j,minZeroFlag=False):
    nowdt=(datetime.datetime.now()+datetime.timedelta(hours=8,minutes=-1))
    if minZeroFlag:
        nowdt=nowdt.replace( minute=0)
    nowdt=nowdt+datetime.timedelta(hours=-j)
    awsData=awsDataHandle(nowdt,stationOutputFlag=True)
    reftime=nowdt.strftime("%Y-%m-%dT%H:%M:00.000Z")
    nowdtStr=nowdt.strftime("%Y-%m-%d %H:00:00")
    # filesTimeStr=nowdt.strftime("%Y%m-%d %H:00:00")
    awsData=awsData.dropna(subset=['long', 'lat'])
    awsDataTmp=awsData.dropna(subset=['long', 'lat',"TEMP","HUMI"])
    tempSorted=awsDataTmp[["OBS_DATETIME","TEMP"]].sort_values("TEMP")
    # 800
    m=longlatGridDict["ny"] 
    # 500
    n=longlatGridDict["nx"]

    # grid=np.array[10][20]
    grid=np.zeros((m,n))
    u=np.zeros((m,n))
    v=np.zeros((m,n))
    speed=np.zeros((m,n))
    temp=np.zeros((m,n))
    humi=np.zeros((m,n))
    latAry=np.zeros((m,n))
    lonAry=np.zeros((m,n))
    wl=np.zeros((m,n))
    for j in range(m):
        for i in range(n):
            dx=longlatGridDict["dx"]
            dy=longlatGridDict["dy"]
            lon1=longlatGridDict["lo1"]+i*longlatGridDict["dx"]
            lat1=longlatGridDict["la1"]-j*longlatGridDict["dy"]
            tmp={}
            tmpWL={}
            for k in longlatData:
                # print(k)
                if k in awsData.index:
                    lon2=longlatData[k][0]
                    lat2=longlatData[k][1]
                    d,_=calDist( lat1,lon1,lat2,lon2)
                    tmp[k]=d
            sorted_dict = sorted(tmp.items(), key=operator.itemgetter(1))[0:10]
            for k in wlLongLatData:
                # print(k)
                if k in wlData.index:
                    lon2=wlLongLatData[k][0]
                    lat2=wlLongLatData[k][1]
                    d,_=calDist( lat1,lon1,lat2,lon2)
                    tmpWL[k]=d
            sorted_dict_WL = sorted(tmpWL.items(), key=operator.itemgetter(1))[0:5]
            # print(sorted_dict)
            summWL=0
            summSpeed=0
            summTemp=0
            # print("--------------")
            numSpeed=0
            numTEMP=0
            numWL=0
            for r in range(10):
                if numSpeed<3:
                    summSpeed+=1./(sorted_dict[r][1])
                    key=sorted_dict[r][0]
                    # print(key,r,sorted_dict[r][0],sorted_dict[r][1])
                    u[j][i]+=1.*awsData.loc[key,"u"]/(sorted_dict[r][1])
                    v[j][i]+=1.*awsData.loc[key,"v"]/(sorted_dict[r][1])
                    speed[j][i]+=1.*awsData.loc[key,"WSPD_10"]/(sorted_dict[r][1])
                    numSpeed+=1
                    # if (np.abs(lon1-113.55111111111111) <2*dx  and np.abs(lat1-22.11722222222222) <2*dy):
                        # print(key,numSpeed,j,i,lon1,lat1,113.55111111111111,22.11722222222222, speed[j][i],sorted_dict[r][1])
                        
                if not np.isnan(awsData.loc[key,"TEMP"]) and numTEMP<3:
                    summTemp+=1./(sorted_dict[r][1])
                    temp[j][i]+=1.*awsData.loc[key,"TEMP"]/(sorted_dict[r][1])
                    humi[j][i]+=1.*awsData.loc[key,"HUMI"]/(sorted_dict[r][1])
                    numTEMP+=1
            for r in range(5):    
                # try:
                key=sorted_dict_WL[r][0]   
                # print(key,wlData.loc[key,"FloodingLevel"]) 
                if not np.isnan(wlData.loc[key,"FloodingLevel"]) and numWL<3:
                    summWL+=1./(sorted_dict_WL[r][1])
                    wl[j][i]+=1.*wlData.loc[key,"FloodingLevel"]/(sorted_dict_WL[r][1])
                    numWL+=1   
                    # if wl[j][i]>0:
                    #     print(r,j,i,numWL,wl[j][i],summWL)         
                # except:
                #     traceback.print_exc(limit=None, file=None, chain=True)
            latAry[j][i]=  lat1
            lonAry[j][i]=  lon1
            u[j][i]/=summSpeed
            u[j][i]=round(u[j][i],2)
            v[j][i]/=summSpeed
            v[j][i]=round(v[j][i],2)
            
            temp[j][i]/=summTemp
            temp[j][i]=round(temp[j][i],2)
            humi[j][i]/=summTemp
            humi[j][i]=round(humi[j][i],2)
            wl[j][i]/=summWL
            wl[j][i]=round(wl[j][i],2)
            # speed[j][i]=np.sqrt(u[j][i]*u[j][i]+v[j][i]*v[j][i])
            speed[j][i]/=summSpeed
            speed[j][i]=round(speed[j][i],2)
            if np.isnan(temp[j][i]) :
                temp[j][i]=-999
                humi[j][i]=-999
            # else:
            #     temp[j][i]=round(temp[j][i]+273,2)

    # print(speed.shape,lonAry.shape,latAry.shape)
    gridx = np.arange(longlatGridDict["lo1"], longlatGridDict["lo2"],longlatGridDict["dx"])
    gridy = np.arange(longlatGridDict["la2"], longlatGridDict["la1"], longlatGridDict["dy"])
    meanvalue=awsData["WSPD_10"].mean()
    stdvalue=awsData["WSPD_10"].std()
    OK = OrdinaryKriging(
        awsData.loc[:,"long"], # data[:, 0],
        awsData.loc[:,"lat"], #data[:, 1],
        (awsData.loc[:,"WSPD_10"]), #data[:, 2],
        variogram_model="spherical",
        verbose=False,
        enable_plotting=False,
        nlags=2,
    )
    
    print("begin ok")
    print(awsData[["OBS_DATETIME","long","lat","WSPD_10"]],gridx,gridy)
    z, ss = OK.execute("grid",gridx , gridy)
    zz=z
    plt.imshow(z)
    # plt.show()
    print(z)
    plt.savefig('a.png')
    n,m = longlatGridDict["nx"],longlatGridDict["ny"]
    speedAry= {        
            "header": {
                "refTime": reftime,
                "nx": n+1,
                "ny": m+1,
                "lo1": longlatGridDict["lo1"],
                "la1": longlatGridDict["la1"],
                "lo2": longlatGridDict["lo2"],
                "la2": longlatGridDict["la2"],
                "dx": longlatGridDict["dx"],
                "dy": longlatGridDict["dy"],
                "parameterCategory": 0,
                "parameterCategoryName": "Temperature",
                "parameterNumber": 0,
            }, "z":z.tolist()}     
    speedAryString = json.dumps(speedAry)
    with open(workdir+"awsData/contour/speedOK.json", "w") as speedCoutour:
        speedCoutour.write(speedAryString)
    speedCoutour.close()    
    print("end ok")

            # print(i,j,grid[j][i])
    # lon1=longlatGridDict["lo1"]-1*longlatGridDict["dx"]
    # lat1=longlatGridDict["la2"]-1*longlatGridDict["dy"]
    # lon2=longlatGridDict["lo2"]+1*longlatGridDict["dx"]
    # lat2=longlatGridDict["la1"]+1*longlatGridDict["dy"]
    # for j in range(m+2):

    #     lonAry[j,0]=lon1
    #     speed[j,0]=-999
    #     # latAry[j,0]=lat1
    #     lonAry[j,n+1]=lon2
    #     speed[j,n+1]=-999
    #     latAry[j,0]=latAry[j,1]
    #     latAry[j,n+1]=latAry[j,1]
        
    # lonAry[0]=lonAry[1]
    # lonAry[m+1]=lonAry[1]
    #     # latAry[j,11]=lat2
    # for i in range(n+2):

    #     latAry[0,i]=lat1
    #     # lonAry[:,0]=lon1
    #     speed[0,i]=-999
    #     speed[m+1,i]=-999

    #     latAry[m+1,i]=lat2
        


    u=np.reshape(u,(n*m))
    v=np.reshape(v,(n*m))
    # temp=np.reshape(temp,(n*m))
    # print(grid.tolist())
    # 
    resultJsonAry=[
        {
            "header": {
                "refTime": reftime,
                "nx": n+1,
                "ny": m+1,
                "lo1": longlatGridDict["lo1"],
                "la1": longlatGridDict["la1"],
                "lo2": longlatGridDict["lo2"],
                "la2": longlatGridDict["la2"],
                "dx": longlatGridDict["dx"],
                "dy": longlatGridDict["dy"],
                "parameterCategory":2,
                "parameterCategoryName": "Temperature",
                "parameterNumber": 2,
            },
            "data": u.tolist(),

        },
        {
            "header": {
                "refTime": reftime,
                "nx": n+1,
                "ny": m+1,
                "lo1": longlatGridDict["lo1"],
                "la1": longlatGridDict["la1"],
                "lo2": longlatGridDict["lo2"],
                "la2": longlatGridDict["la2"],
                "dx": longlatGridDict["dx"],
                "dy": longlatGridDict["dy"],
                "parameterCategory": 2,
                "parameterCategoryName": "Temperature",
                "parameterNumber": 3,
                },
            "data": v.tolist(),
            
            },
        {
            "header": {
                "refTime": reftime,
                "nx": n+1,
                "ny": m+1,
                "lo1": longlatGridDict["lo1"],
                "la1": longlatGridDict["la1"],
                "lo2": longlatGridDict["lo2"],
                "la2": longlatGridDict["la2"],
                "dx": longlatGridDict["dx"],
                "dy": longlatGridDict["dy"],
                "parameterCategory": 0,
                "parameterCategoryName": "Temperature",
                "parameterNumber": 0,
            },
            "data": temp.tolist(),     
        }
    ]

    # print(resultJsonAry[0]["data"])
    ############
    # wind particule
    #########
    filenameDTStr=nowdt.strftime("%Y%m%d%H")
    jsonString = json.dumps(resultJsonAry)
    if minZeroFlag:
        with open(workdir+"awsData/contour/wdir_"+filenameDTStr+".json", "w") as outfile:
            outfile.write(jsonString)
        outfile.close()
    else:
        with open(workdir+"awsData/contour/wdir.json", "w") as outfile:
            outfile.write(jsonString)
        outfile.close()        

    speedAry= {        
            "header": {
                "refTime": reftime,
                "nx": n+1,
                "ny": m+1,
                "lo1": longlatGridDict["lo1"],
                "la1": longlatGridDict["la1"],
                "lo2": longlatGridDict["lo2"],
                "la2": longlatGridDict["la2"],
                "dx": longlatGridDict["dx"],
                "dy": longlatGridDict["dy"],
                "parameterCategory": 0,
                "parameterCategoryName": "Temperature",
                "parameterNumber": 0,
            },"x": lonAry.tolist(), "y":latAry.tolist(), "z":speed.tolist()} 

    humiAry= {        
            "header": {
                "refTime": reftime,
                "nx": n+1,
                "ny": m+1,
                "lo1": longlatGridDict["lo1"],
                "la1": longlatGridDict["la1"],
                "lo2": longlatGridDict["lo2"],
                "la2": longlatGridDict["la2"],
                "dx": longlatGridDict["dx"],
                "dy": longlatGridDict["dy"],
                "parameterCategory": 0,
                "parameterCategoryName": "Temperature",
                "parameterNumber": 0,
            },"z":humi.tolist()} 

    tempAry= {        
            "header": {
                "refTime": reftime,
                "nx": n+1,
                "ny": m+1,
                "lo1": longlatGridDict["lo1"],
                "la1": longlatGridDict["la1"],
                "lo2": longlatGridDict["lo2"],
                "la2": longlatGridDict["la2"],
                "dx": longlatGridDict["dx"],
                "dy": longlatGridDict["dy"],
                "parameterCategory": 0,
                "parameterCategoryName": "Temperature",
                "parameterNumber": 0,
            },"z":temp.tolist()} 
    speedAryString = json.dumps(speedAry)
    ############
    # aws latest contour
    #########
    if minZeroFlag:
        with open(workdir+"awsData/contour/speed_"+filenameDTStr+".json", "w") as speedCoutour:
            speedCoutour.write(speedAryString)
        speedCoutour.close()
            
        tempString = json.dumps(tempAry)
        with open(workdir+"awsData/contour/temp_"+filenameDTStr+".json", "w") as tempCoutour:
            tempCoutour.write(tempString)
        tempCoutour.close()
        humiString = json.dumps(humiAry)
        with open(workdir+"awsData/contour/humi_"+filenameDTStr+".json", "w") as humiCoutour:
            humiCoutour.write(humiString)
    else:
        with open(workdir+"awsData/contour/speed.json", "w") as speedCoutour:
            speedCoutour.write(speedAryString)
        speedCoutour.close()
            
        tempString = json.dumps(tempAry)
        with open(workdir+"awsData/contour/temp.json", "w") as tempCoutour:
            tempCoutour.write(tempString)
        tempCoutour.close()
        humiString = json.dumps(humiAry)
        with open(workdir+"awsData/contour/humi.json", "w") as humiCoutour:
            humiCoutour.write(humiString)        
    humiCoutour.close()
    wlAry= {        
            "header": {
                "refTime": reftime,
                "nx": n+1,
                "ny": m+1,
                "lo1": longlatGridDict["lo1"],
                "la1": longlatGridDict["la1"],
                "lo2": longlatGridDict["lo2"],
                "la2": longlatGridDict["la2"],
                "dx": longlatGridDict["dx"],
                "dy": longlatGridDict["dy"],
                "parameterCategory": 0,
                "parameterCategoryName": "Temperature",
                "parameterNumber": 0,
            }, "z":wl.tolist()} 
    wlString = json.dumps(wlAry)    
    ############
    # aws latest contour
    #########
    if minZeroFlag:
        with open(workdir+"wlData/contour/wl_"+filenameDTStr+".json", "w") as wlCoutour:
            wlCoutour.write(wlString)
        wlCoutour.close()
    else:
        with open(workdir+"wlData/contour/wl.json", "w") as wlCoutour:
            wlCoutour.write(wlString)
        wlCoutour.close()        


for j in range(27):
    awsContourGen(j,minZeroFlag=True)
awsContourGen(0,minZeroFlag=False)  
nowdt=(datetime.datetime.now()+datetime.timedelta(hours=8,minutes=-1))
awsDataHandle(nowdt,stationOutputFlag=True,fileNameWithTime=False)
####################################
# aws station calculate mean, qualite ,
# thirdQualite , min and max for time series
#####################################

tempQuantileList=[]
humiQuantileList=[]
wspdQuantileList=[]
nowdt=(datetime.datetime.now()+datetime.timedelta(hours=8,minutes=-1))
nowdt24hoursAgo=nowdt+datetime.timedelta(hours=-24)
for j in range(1441):
    
    
    # nowdt=nowdt.replace( minute=0)
    nowdt=nowdt24hoursAgo+datetime.timedelta(minutes=j)
    # if j==0:
    #     stationOutputFlag=True
    # else:
    #     stationOutputFlag=False
    awsData=awsDataHandle(nowdt,stationOutputFlag=True)
    reftime=nowdt.strftime("%Y-%m-%dT%H:%M:%M.000Z")
    nowdtStr=nowdt.strftime("%Y-%m-%d %H:%M:00")
    # filesTimeStr=nowdt.strftime("%Y%m-%d %H:00:00")
    awsData=awsData.dropna(subset=['long', 'lat'])
    awsDataTmp=awsData.dropna(subset=['long', 'lat',"TEMP","HUMI"])
    tempSorted=awsDataTmp[["OBS_DATETIME","TEMP"]].sort_values("TEMP")
    vartempDict={
            "OBS_DATETIME":nowdtStr,
            "min":tempSorted["TEMP"].min(),
            "quantile":tempSorted["TEMP"].quantile(q=0.25,interpolation="linear"),
            "mean":tempSorted["TEMP"].mean(),
            "thirdQuantile":tempSorted["TEMP"].quantile(q=0.75,interpolation="linear"),
            "max":tempSorted["TEMP"].max(),
        }
    
    tempQuantileList.append(vartempDict)
    awsString2 = json.dumps({0:tempQuantileList}, cls=NpEncoder)


    humiSorted=awsDataTmp[["OBS_DATETIME","HUMI"]].sort_values("HUMI")
    varhumiDict={"OBS_DATETIME":nowdtStr,
             "min":humiSorted["HUMI"].min(),
             "quantile":humiSorted["HUMI"].quantile(q=0.25,interpolation="linear"),
             "mean":humiSorted["HUMI"].mean(),
             "thirdQuantile":humiSorted["HUMI"].quantile(q=0.75,interpolation="linear"),
             "max":humiSorted["HUMI"].max(),
        }
    humiQuantileList.append(varhumiDict)   

    
    
    wspdSorted=awsData[["OBS_DATETIME","WSPD_10"]].sort_values("WSPD_10")
    varwspdDict={"OBS_DATETIME":nowdtStr,
            "min":wspdSorted["WSPD_10"].min(),
            "quantile":wspdSorted["WSPD_10"].quantile(q=0.25,interpolation="linear"),
            "mean":wspdSorted["WSPD_10"].mean(),
            "thirdQuantile":wspdSorted["WSPD_10"].quantile(q=0.75,interpolation="linear"),
            "max":wspdSorted["WSPD_10"].max(),
    }
    
    
    wspdQuantileList.append(varwspdDict)   

awsString2 = json.dumps({0:tempQuantileList}, cls=NpEncoder)     
with open(workdir+"awsData/stationTimeSeries/quantile_TEMP.json", "w") as awsJsonFile:
    awsJsonFile.write(awsString2)
# awsTimeSeriesData.to_csv("TG.csv",index=False)
awsJsonFile.close()
awsString2 = json.dumps({0:humiQuantileList}, cls=NpEncoder)

with open(workdir+"awsData/stationTimeSeries/quantile_HUMI.json", "w") as awsJsonFile:
    awsJsonFile.write(awsString2)
# awsTimeSeriesData.to_csv("TG.csv",index=False)
awsJsonFile.close()    
awsString2 = json.dumps({0:wspdQuantileList}, cls=NpEncoder)

with open(workdir+"awsData/stationTimeSeries/quantile_WSPD_10.json", "w") as awsJsonFile:
    awsJsonFile.write(awsString2)
# awsTimeSeriesData.to_csv("TG.csv",index=False)
awsJsonFile.close()    