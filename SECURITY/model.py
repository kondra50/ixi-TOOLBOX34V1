
import pymssql
server = "192.168.3.40"
user = "sysdba"
password = "e$1s_s"
database="ESIDB"

conn = pymssql.connect(host='192.168.3.40', user='sysdba', password='e$1s_s', database='ESIDB')


def Accesslist(group):
    try:
        pids_as_dict=[]
        cur = conn.cursor()
        wherecluse='%-%'
        s='select SUBSTRING(PROGRAM_ID,2,len(PROGRAM_ID)-1),RUN_PERMIT,ADD_PERMIT,DELETE_PERMIT,MOD_PERMIT,PIDDESC,ltrim(rtrim(HREF)) from XXFRTS where USER_OR_GROUP='+repr(group)+' and PROGRAM_ID like  '+ repr(wherecluse)+''
        cur.execute(s)
        rows = cur.fetchall()
        concat = ''
        for row in rows:
             # s = row[0]
             # s = repr(s)+':1'
             # concat = concat+s+','
             pid_as_dict= {

             'program_id':row[0],
             'view':row[1],
             'insert':row[2],
             'delete':row[3],
             'update':row[4],
             'PIDDESC':row[5],
             'HREF':row[6],
             'Print':'1'
             }
             pids_as_dict.append(pid_as_dict)
        # pids_as_dict = {'ACL' : concat[0:len(concat)-1]}
        return pids_as_dict
    except Exception as e:
          return {"Error":"There is problem in connecting to database"}