from sqlalchemy import  sql,create_engine,text
engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/ESIDB')
from simple_salesforce import Salesforce
import salesforce_reporting
import requests,json
from flask import jsonify
sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
analytic_sf = salesforce_reporting.Connection('3MVG99OxTyEMCQ3glBkdKh4SE2HJs4uODXEl2Fux.LFlCzqkgs9Tr8XLqmCvUsOSdsVpbGoj9xhN5f4hpJ2OZ', '86072956447270870',
                                              'customerservice@integenx.com', 'password123453GKZny4jRWgmXNUmvFjzKhggQ', 'na13')


def FillSFDC7(*mydict):
       try:
          with engine.connect() as con:
            dict=mydict[0]
            val=dict.values()
            key=dict.keys()
            rs = con.execute('INSERT INTO [SFDC7]([Sales Order Number] )'
                     'values('+ val[0] +')')
            con.close()
       except Exception as e:
           print(e)

# report=analytic_sf.get_report('00Oa0000008272QEAQ')
# parser = salesforce_reporting.ReportParser(report)
# dict=parser.records()
# rps_as_dict=[]
#       #dbmodels.EXPUPDATE.FillSFDC7()
# all=''
# rps_as_dict=[]
# for record in  dict:
#             rp_as_dict = {
#                    'Sales Order Number' :  record[0],
#                    'Prod Line' :  record[1],
#                    'Sales Order Line' :  record[2],
#                    'Line St' :  record[3],
#                    'Status' :  record[4],
#                    'Rev Ship' :  record[5],
#                    'Last Shipment' :  record[6],
#                    'Rev Ord Qty' :  record[7],
#                    'Last Modified Date' :  record[8],
#                    'Part ID' :  record[9],
#                    'Description' :  record[10],
#                    'Created Date' :  record[11],
#                    'Platform' :  record[12],
#                    'Base Price' :  record[13],
#                    'Amount' :  record[14]
#                    #'Opportunity Owner' :  record[15],
#             }
#             #print(rp_as_dict)
#             #FillSFDC7(rp_as_dict)
#             rps_as_dict.append(rp_as_dict)
#SELECT Name, (SELECT Name FROM Job_Applications__r) FROM Position__c
#SELECT ESI__AMOUNT__c,ESI__SO_ID__c,ESI__Sales_Order_Master__r.ESI__SO_STATUS__c  FROM ESI__Sales_Order_Detail__c
#[Sales Order Number],[Prod Line],[Sales Order Line] ,[Line St],[Status],[Rev Ship],[Last Shipment],[Rev Ord Qty],
#[Last Modified Date],[Part ID],[Description],[Created Date],[Platform],[Base Price],[Amount])'



#list=sf.query("SELECT ESI__SO_STATUS__c,(select ESI__SO_ID__c,ESI__PRODUCT_LINE__c,ESI__SO_LINE_NO__c,ESI__SO_LINE_STATUS__c,ESI__REV_SHIP_DATE__c,ESI__LAST_SHIP_NO__c,ESI__REV_ORDER_QTY__c,ESI__AMOUNT__c from ESI__Sales_Order_Master__c.SO_IDx) from ESI__Sales_Order_Master__c")
#list=sf.query("select ESI__SO_ID__c,ESI__PRODUCT_LINE__c,ESI__SO_LINE_NO__c,ESI__SO_LINE_STATUS__c,ESI__REV_SHIP_DATE__c,ESI__LAST_SHIP_NO__c,ESI__REV_ORDER_QTY__c,ESI__AMOUNT__c from ESI__Sales_Order_Detail__c LIMIT 2100")

#list=sf.query("select ESI__SO_ID__c,ESI__PRODUCT_LINE__c,ESI__SO_LINE_NO__c,ESI__SO_LINE_STATUS__c,ESI__REV_SHIP_DATE__c,ESI__LAST_SHIP_NO__c,ESI__REV_ORDER_QTY__c,ESI__AMOUNT__c,ESI__SO_ID__r.ESI__SO_STATUS__c  from ESI__Sales_Order_Detail__c where ESI__SO_ID__r.ESI__ORDER_DATE__c>2016-01-01 ")
#list=sf.query("select ESI__SO_STATUS__c,(select ESI__SO_ID__c,ESI__PRODUCT_LINE__c,ESI__SO_LINE_NO__c,ESI__SO_LINE_STATUS__c,ESI__REV_SHIP_DATE__c,ESI__LAST_SHIP_NO__c,ESI__REV_ORDER_QTY__c,ESI__AMOUNT__c  from ESI__SO_IDx__r) from ESI__Sales_Order_Master__C")
#list=sf.query("SELECT ESI__Sales_Order_Master__r.Name FROM ESI__Sales_Order_Detail__c LIMIT 1")
      #list=sf.query("SELECT Approved FROM [Expandable Sales Orders] ")

#
# list=sf.query("select ESI__SO_ID__r.ESI__SO_ID__c ,ESI__PRODUCT_LINE__c,ESI__SO_LINE_NO__c,ESI__SO_LINE_STATUS__c,ESI__SO_ID__r.ESI__SO_STATUS__c,ESI__REV_SHIP_DATE__c,ESI__LAST_SHIP_NO__c,ESI__REV_ORDER_QTY__c,ESI__AMOUNT__c  from ESI__Sales_Order_Detail__c where ESI__SO_ID__r.ESI__ORDER_DATE__c>2016-01-01 ")
#
#
# dict=list["records"]
# #dict2=dict[0]
# prs_as_dict=[]
# i=0
# # for record in  dict2:
# #    print(record)
# for record in  dict:
#    i=i+1
#    print(record)
#    print(record["ESI__SO_ID__c"])
#    # print(record["ESI__SO_ID__c"])
#    # print(record["ESI__SO_STATUS__c"])
# # for record in  dict:
# #    i=i+1
# #    print(record)
# #    print(record["ESI__SO_STATUS__c"])


#print(i)


connection = engine.raw_connection()
cursor = connection.cursor()
cursor.callproc('[Admin_SFDCEXP_DESCREPANCY]')
for row in cursor:
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
        print(row)
        print(DESCREPANCY_AS_DICT)