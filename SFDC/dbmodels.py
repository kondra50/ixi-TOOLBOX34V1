from sqlalchemy import  sql,create_engine,text
engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/ESIDB')

# with engine.connect() as con:
#     rs = con.execute("delete from SFDC7")
#
# con.close()
#
# with engine.connect() as con:
#     rs = con.execute('INSERT INTO [SFDC7]([Sales Order Number] ,[Prod Line],[Sales Order Line],[Line St],'
#                      '[Status] ,[Rev Ship],[Last Shipment],[Rev Ord Qty],'
#                      '[Last Modified Date] ,[Part ID],[Description],[Created Date],[Platform],[Base Price],[Amount])'
#                      'values(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)')

#con.close()
class EXPUPDATE():
   @staticmethod
   def FillSFDC7(*mydict):
       try:
          with engine.connect() as con:
            dict=mydict[0]
            am=str(dict['Amount']).replace(',','')
            bp=str(dict['Base Price']).replace(',','')
            val=dict.values()
            key=dict.keys()
            st='INSERT INTO [SFDC7](SO_ID,PRODUCT_LINE,SO_LINE ,LINE_STATUS,STATUS,REV_SHIP,LAST_SHIPMENT,REV_ORDER_QUANTITY,LAST_MOD_DATE,PART_ID,[DESC],CREATED_DATE,PLATFORM,BASE_PRICE,AMOUNT) values('+ repr(dict['Sales Order Number']) +',' + repr(str(dict['Prod Line'])) + ','+ str(dict['Sales Order Line']) +',' + repr(str(dict['Line St'])) + ',' + repr(str(dict['Status'])) + ',' + repr(str(dict['Rev Ship'])) + ',' + repr(str(dict['Last Shipment'])) + ',' + repr(str(dict['Rev Ord Qty'])) + ',' + repr(str(dict['Last Modified Date'])) + ',' + repr(str(dict['Part ID'])) + ',' + repr(str(dict['Description'])) + ',' + repr(str(dict['Created Date'])) + ',' + repr(str(dict['Platform'])) + ',' + repr(str(bp)) + ',' +str(am) + '' ')'
            rs = con.execute(st)

            con.close()

       except Exception as e:
           print(e)

   @staticmethod
   def CLEANSFDC7():
       try:
          with engine.connect() as con:
            st='Delete from SFDC7'
            rs = con.execute(st)
            con.close()
       except Exception as e:
           print(e)



   def FillSFDC7New(*mydict):
       try:
          with engine.connect() as con:
            dict=mydict[0]
            am=str(dict['Amount']).replace(',','')
            #bp=str(dict['Base Price']).replace(',','')
            val=dict.values()
            key=dict.keys()
            st='INSERT INTO [SFDC7]([Sales Order Number],[Prod Line],[Sales Order Line] ,[Line St],[Rev Ship],[Last Shipment],[Rev Ord Qty],[Last Modified Date],[Amount]) ' \
               'values('+ repr(dict['Sales Order Number']) +',1,1,1,1,1,1,4,5)'
            rs = con.execute(st)

            con.close()

       except Exception as e:
           print(e)
   @staticmethod
   def SFDC_EXP_DESCREPANCY():
       try:
           connection = engine.raw_connection()
           cursor = connection.cursor()
           cursor.callproc('[Admin_SFDCEXP_DESCREPANCY]')
           DESCREPANCY_AS_DICT=[]
           DESCREPANCIES_AS_DICT=[]
           for row in cursor:
               print(row)
               DESCREPANCY_AS_DICT= {
                  'SO_ID':row[0],
                  'SO_LINE':row[1],
                  'LINE_STATUS':row[2],
                  'STATUS':row[3],
                  'REV_SHIP':row[4],
                  'AMOUNT':row[5],
                  'Field':row[6]
               }
               DESCREPANCIES_AS_DICT.append(DESCREPANCY_AS_DICT)
           return DESCREPANCIES_AS_DICT
       except Exception as e:
           return {
                  'ERROR': str(e)
               }
       finally:
          cursor.close()
          connection.commit()
          connection.close()