from pymongo import MongoClient
from datetime import datetime
client = MongoClient()
db = client.test
#dbExp=client.ExpLog
# result = db.restaurants.insert_one(
#     {
#         "address": {
#             "street": "2 Avenue",
#             "zipcode": "10075",
#             "building": "1480",
#             "coord": [-73.9557413, 40.7720266]
#         },
#         "borough": "Manhattan",
#         "cuisine": "Italian",
#         "grades": [
#             {
#                 "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
#                 "grade": "A",
#                 "score": 11
#             },
#             {
#                 "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
#                 "grade": "B",
#                 "score": 17
#             }
#         ],
#         "name": "Vella",
#         "restaurant_id": "41704620"
#     }
# )
# print(result.inserted_id)


import re
import pymssql
from time import strptime
import datetime
conn = pymssql.connect(host='192.168.3.40', user='sysdba', password='e$1s_s', database='ESIDB')
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
dict={}
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
        #print(dict)
        # print(s)
        result = db.test.insert_one(dict)
        print(result.inserted_id)
    except Exception as e:


        i=i+1
        with open("err.txt","a") as fileobject:
            fileobject.write(line)
        badlines.append(line)
        print(e)
# badlines=[]

def DB_TO_MONGO():
    s=' select [PROGRAM_ID] ,[TABLE_NAME],[OPERATOR_ID] ,[FIRST_NAME] ,[LAST_NAME] ,[INITIAL],[MACHINE] ,[CHANGE_TYPE] ,[KEY1],[KEY2],[KEY3] ,[KEY4] ,[KEY5] ,[KEY6],[MAINT_LOG],[TIME_LAST_UPDT],[DATE_LAST_UPDT] ,[DELETE_FLAG] from dbo.ALFTD'
    try:
        cur.execute(s)
        while True:
            row = cur.fetchone()
            if row is None:
                break
            yield row
            #results = cur.fetchall()
    except Exception as e :
        print(e)


HeadeList=['PROGRAM_ID' ,'TABLE_NAME','OPERATOR_ID' ,'FIRST_NAME' ,'LAST_NAME' ,'INITIAL','MACHINE' ,'CHANGE_TYPE' ,'KEY1','KEY2','KEY3' ,'KEY4' ,'KEY5' ,'KEY6','MAINT_LOG','TIME_LAST_UPDT','DATE_LAST_UPDT' ,'DELETE_FLAG']

rows = DB_TO_MONGO()
try:
    for row in rows:
         print(row[0])
         PROGRAM_ID=row[0]
         dict={'PROGRAM_ID': row[0],'TABLE_NAME':row[1],'OPERATOR_ID':row[2] ,'FIRST_NAME':row[3] ,'LAST_NAME' :row[4],'INITIAL':row[5],'MACHINE':row[6] ,'CHANGE_TYPE' :row[7] ,'KEY1':row[8],'KEY2' :row[9],'KEY3':row[10] ,'KEY4':row[11] ,'KEY5':row[12] ,'KEY6':row[13],'MAINT_LOG':row[14],'TIME_LAST_UPDT':row[15],'DATE_LAST_UPDT':row[16] ,'DELETE_FLAG':row[17]}
         result = db.gizillion.insert_one(dict)
         print(result.inserted_id)
         #dict={'PROGRAM_ID': row[0] ,'TABLE_NAME':row[0],,'OPERATOR_ID':actiontime_new1,'FIRST_NAME':size,'LAST_NAME':status,'INITIAL','MACHINE' ,'CHANGE_TYPE' ,'KEY1','KEY2','KEY3' ,'KEY4' ,'KEY5' ,'KEY6','MAINT_LOG','TIME_LAST_UPDT','DATE_LAST_UPDT' ,'DELETE_FLAG'}
         #zipped=zip(HeadeList,row)
         #print(list((zipped)))
except Exception as e:
    print(e)

# pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
# with open(filepath) as fileobject:
#     for line in fileobject:
#         Line_TO_DB(line)





