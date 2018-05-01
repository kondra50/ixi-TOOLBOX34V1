import re
import pymssql
from time import strptime
import datetime
conn = pymssql.connect(host='192.168.3.40', user='sysdba', password='e$1s_s', database='ESI_DATA')
cur = conn.cursor()
filepath='C:\\Python34\\ixi_TBOX34\\access.log'
parts = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]

#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

def Line_TO_DB(line):
    i=0
    badlines=[]
    try:
        pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
        m = pattern.match(line)
        res = m.groupdict()
        host,actiontime,request,size,agent,status =res["host"],res["time"],res["request"],res["size"],res["agent"],res["status"]
        i=len(actiontime)
        actiontime= actiontime[:i-6]
        words = actiontime.split("/")
        mytime=str(words[2]).split(":")
        newtime=str(mytime[0])+' '+str(mytime[1])+':'+str(mytime[2])+':'+str(mytime[3])
        newtime1=str(mytime[1])+':'+str(mytime[2])+':'+str(mytime[3])
        actiontime_new=str(words[0])+'/'+str(strptime(words[1],'%b').tm_mon)+'/'+str(newtime)
        actiontime_new1=str(mytime[0])+'/'+str(strptime(words[1],'%b').tm_mon)+'/'+str(words[0])+' '+str(newtime1)
        #s='INSERT INTO [ESI_DATA].[dbo].[LOG_AP]([HOST] ,[REQUEST],[ACTIONTIME],[SIZE],[STATUS]) values ('+repr(host)+','+repr(request)+','+repr(actiontime)+','+repr(size)+','+repr(status)+')'
        s='INSERT INTO [ESI_DATA].[dbo].[LOG_AP]([HOST] ,[REQUEST],[ACTIONTIME],[SIZE],[STATUS]) values ('+repr(host)+','+repr(request)+','+repr(actiontime_new1)+','+repr(size)+','+repr(status)+')'
        dict={'HOST':host,'REQUEST':request,'ACTIONTIME':actiontime_new1,'SIZE':size,'STATUS':status}
        print(dict)
        print(s)
        #cur.execute(s)
        #conn.commit()
    except Exception as e:


        i=i+1
        with open("err.txt","a") as fileobject:
            fileobject.write(line)
        badlines.append(line)
        print(e)
# badlines=[]
# pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
with open(filepath) as fileobject:
    for line in fileobject:
        Line_TO_DB(line)


# import time
# thefile=open(filepath,"r")
# thefile.seek(0,2) # Go to the end of the file
# while True:
#     line = thefile.readline()
#     if not line:
#         print('nothing...')
#         time.sleep(2) # Sleep briefly
#         continue
#     else:
#          Line_TO_DB(line)


