import re
import pymssql
from time import strptime
import datetime
conn = pymssql.connect(host='192.168.3.40', user='sysdba', password='e$1s_s', database='ESI_DATA')
cur = conn.cursor()
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

i=0
def Line_TO_DB(line):
    try:
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
            print(s)
            cur.execute(s)
            conn.commit()
    except Exception as e:


        i=i+1
        with open("err.txt","a") as fileobject:
            fileobject.write(line)
        badlines.append(line)
        print(e)
badlines=[]
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
with open("access.log") as fileobject:
    for line in fileobject:
        Line_TO_DB(line)
        # try:
        #     m = pattern.match(line)
        #     res = m.groupdict()
        #     host,actiontime,request,size,agent,status =res["host"],res["time"],res["request"],res["size"],res["agent"],res["status"]
        #     i=len(actiontime)
        #     actiontime= actiontime[:i-6]
        #     words = actiontime.split("/")
        #     mytime=str(words[2]).split(":")
        #     newtime=str(mytime[0])+' '+str(mytime[1])+':'+str(mytime[2])+':'+str(mytime[3])
        #     newtime1=str(mytime[1])+':'+str(mytime[2])+':'+str(mytime[3])
        #     actiontime_new=str(words[0])+'/'+str(strptime(words[1],'%b').tm_mon)+'/'+str(newtime)
        #     actiontime_new1=str(mytime[0])+'/'+str(strptime(words[1],'%b').tm_mon)+'/'+str(words[0])+' '+str(newtime1)
        #     #s='INSERT INTO [ESI_DATA].[dbo].[LOG_AP]([HOST] ,[REQUEST],[ACTIONTIME],[SIZE],[STATUS]) values ('+repr(host)+','+repr(request)+','+repr(actiontime)+','+repr(size)+','+repr(status)+')'
        #     s='INSERT INTO [ESI_DATA].[dbo].[LOG_AP]([HOST] ,[REQUEST],[ACTIONTIME],[SIZE],[STATUS]) values ('+repr(host)+','+repr(request)+','+repr(actiontime_new1)+','+repr(size)+','+repr(status)+')'
        #     print(s)
        #     cur.execute(s)
        #     conn.commit()
        # except Exception as e:
        #      i=i+1
        #      with open("err.txt","a") as fileobject:
        #          fileobject.write(line)
        #      badlines.append(line)
        #      print(e)

#print(i)
#print(badlines)



import time
thefile=open("access.log","r")
thefile.seek(0,2) # Go to the end of the file
while True:
    line = thefile.readline()
    if not line:
        print('nothing...')
        time.sleep(2) # Sleep briefly
        continue
    else:
         Line_TO_DB(line)
         # try:
         #    m = pattern.match(line)
         #    res = m.groupdict()
         #    host,actiontime,request,size,agent,status =res["host"],res["time"],res["request"],res["size"],res["agent"],res["status"]
         #    i=len(actiontime)
         #    actiontime= actiontime[:i-6]
         #    words = actiontime.split("/")
         #    mytime=str(words[2]).split(":")
         #    newtime=str(mytime[0])+' '+str(mytime[1])+':'+str(mytime[2])+':'+str(mytime[3])
         #    newtime1=str(mytime[1])+':'+str(mytime[2])+':'+str(mytime[3])
         #    actiontime_new=str(words[0])+'/'+str(strptime(words[1],'%b').tm_mon)+'/'+str(newtime)
         #    actiontime_new1=str(mytime[0])+'/'+str(strptime(words[1],'%b').tm_mon)+'/'+str(words[0])+' '+str(newtime1)
         #    #s='INSERT INTO [ESI_DATA].[dbo].[LOG_AP]([HOST] ,[REQUEST],[ACTIONTIME],[SIZE],[STATUS]) values ('+repr(host)+','+repr(request)+','+repr(actiontime)+','+repr(size)+','+repr(status)+')'
         #    s='INSERT INTO [ESI_DATA].[dbo].[LOG_AP]([HOST] ,[REQUEST],[ACTIONTIME],[SIZE],[STATUS]) values ('+repr(host)+','+repr(request)+','+repr(actiontime_new1)+','+repr(size)+','+repr(status)+')'
         #    print(s)
         #    cur.execute(s)
         #    conn.commit()
         # except Exception as e:
         #     i=i+1
         #     with open("err.txt","a") as fileobject:
         #         fileobject.write(line)
         #     badlines.append(line)
         #     print(e)















# with open('access.log') as f:
#     lines = f.readlines()
#     print(lines)
#import re

# regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'
# import re
# rexp = re.compile('(\d+\.\d+\.\d+\.\d+) - - \[([^\[\]:]+):'
#                   '(\d+:\d+:\d+) -(\d\d\d\d\)] ("[^"]*") '
#                   '(\d+) (-|\d+) ("[^"]*") (".*")\s*\Z')
# with open("access.log") as fileobject:
#     for line in fileobject:
#         print(line)
#         a = rexp.match(line)
#         if not a is None:
#
#             a.group(1) #IP address
#             a.group(2) #day/month/year
#             a.group(3) #time of day
#             a.group(4) #timezone
#             a.group(5) #request
#             a.group(6) #code 200 for success, 404 for not found, etc.
#             a.group(7) #bytes transferred
#             a.group(8) #referrer
#             a.group(9) #browser
#         else:
#             print('test');
#         #do_something_with(line)

#import apachelog
# format = '%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"'
#
# p = apachelog.parser(format)
#
# for line in open('access.log'):
#     try:
#        data = p.parse(line)
#     except:
#       print("Unable to parse %s" % line)




#a = rexp.match(line)

#this line did not match.