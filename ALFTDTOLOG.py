import pymssql
import csv
import datetime
conn = pymssql.connect(host='192.168.3.40', user='sysdba', password='e$1s_s', database='ESIDB')

try:
    cur = conn.cursor()
    mydate='10-03-2016'
    print(max)
    s='SELECT  [RECNUM],[PROGRAM_ID],[TABLE_NAME],[OPERATOR_ID] ,[FIRST_NAME],[LAST_NAME],[INITIAL],[MACHINE] ,[CHANGE_TYPE],[KEY1],[KEY2] ,[KEY3],[KEY4],[KEY5],[KEY6],[MAINT_LOG],[TIME_LAST_UPDT],[DATE_LAST_UPDT],[DELETE_FLAG] FROM [ALFTD] where DATE_LAST_UPDT<=(SELECT MIN(DATE_LAST_UPDT+3)FROM [ESIDB].[dbo].[ALFTD] where DATE_LAST_UPDT< getdate()-15) order by DATE_LAST_UPDT'
    print(s)
    cur.execute('SELECT  [RECNUM],[PROGRAM_ID],[TABLE_NAME],[OPERATOR_ID] ,[FIRST_NAME],'
                    '[LAST_NAME],[INITIAL],[MACHINE] ,[CHANGE_TYPE],[KEY1],[KEY2] ,[KEY3],[KEY4],[KEY5],'
                    '[KEY6],[MAINT_LOG],[TIME_LAST_UPDT],[DATE_LAST_UPDT],[DELETE_FLAG] FROM [ALFTD] where DATE_LAST_UPDT<=(SELECT MIN(DATE_LAST_UPDT+3)FROM [ESIDB].[dbo].[ALFTD] where DATE_LAST_UPDT< getdate()-15) order by DATE_LAST_UPDT')
    # where [DATE_LAST_UPDT] >= '+ repr(mydate))
    rows = cur.fetchall()
    len1=len(rows)
    mindate=str(rows[0][17])[:10]
    print(mindate)
    maxdate=str(rows[len1-1][17])[:10]

    print(maxdate)

    file_path='C:\Python34\ixi_TBOX34\\'+mindate+'-'+maxdate+'-explog.csv'
    with open(file_path, 'a') as outcsv:
        #configure writer to write standard csv file
        writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['RECNUM', 'PROGRAM_ID', 'TABLE_NAME', 'OPERATOR_ID', 'FIRST_NAME', 'LAST_NAME', 'INITIAL', 'MACHINE','CHANGE_TYPE', 'KEY1', 'KEY2', 'KEY3', 'KEY4', 'KEY5', 'KEY6', 'MAINT_LOG', 'TIME_LAST_UPDT', 'DATE_LAST_UPDT', 'DELETE_FLAG'])
        for row in rows:
            print(row[15])
            writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],repr(str(row[15]).replace(',','')),row[16],row[17],row[18]])


    # d-'delete  FROM [ALFTD] where DATE_LAST_UPDT<=(SELECT MIN(DATE_LAST_UPDT+3)FROM [ESIDB].[dbo].[ALFTD] where DATE_LAST_UPDT< DATEADD(month, datediff(month, 0, getdate())-1, 0)) order by DATE_LAST_UPDT'
    # print(d)
    cur.execute('delete  FROM [ALFTD] where DATE_LAST_UPDT<=(SELECT MIN(DATE_LAST_UPDT+3)FROM [ESIDB].[dbo].[ALFTD] where DATE_LAST_UPDT< getdate()-15)')
    conn.commit()
    conn.close()


except Exception as e:
          print( e)
# list()