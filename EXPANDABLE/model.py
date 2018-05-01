from os import getenv
import pymssql
from flask_restful import Resource, reqparse
server = "192.168.3.40"
user = "sysdba"
password = "e$1s_s"
database="ESIDB"
import string
from flask import  make_response
from flask.ext.jsonpify import jsonpify

conn = pymssql.connect(host='192.168.3.40', user='sysdba', password='e$1s_s', database='ESIDB')





def list(startdate,enddate):
    FedexShipmentS_as_dict=[]

    if (str(enddate) =='None'):  enddate='1900-01-01'
    if (str(startdate) =='None'):  startdate='1900-01-01'
    print(startdate)
    # str(startdate).replace('None', '')
    # str(enddate).replace('None', '')
    print(startdate)
    try:
     with pymssql.connect(server, user, password, database) as conn:
         with conn.cursor(as_dict=True) as cursor:
             cursor.callproc('Admin_Fedex_Shipment', (startdate, enddate))
             for row in cursor:
                FedexShipment_as_dict= {
                    'SO_ID': row['SO_ID'],
                    'CUST_PO_ID': row['CUST_PO_ID'],
                    'SHIP_VIA': row['SHIP_VIA'],
                    'BILL_OF_LADING': row['BILL_OF_LADING'],
                    'ACTION_DATE': row['ACTION_DATE'],
                    'OPERATOR_ID': row['OPERATOR_ID'],
                    'SHIPDESCRIPTION': row['SHIPDESCRIPTION'],
                    'customer_id': row['customer_id'],
                    'customer_name': row['customer_name'],
                     }
                FedexShipmentS_as_dict.append(FedexShipment_as_dict)
         return FedexShipmentS_as_dict

    except Exception as e:
         return {"Error": str(e)}



def sofiguers():
    sdfigureS_as_dict=[]

    try:
     with pymssql.connect(server, user, password, database) as conn:
         with conn.cursor(as_dict=True) as cursor:
             cursor.callproc('Admin_Toolbox_Dash_Figures', ())
             for row in cursor:
                sdfigure_as_dict= {
                    'C': row['CAN'],
                    'LC': row['LCAN'],
                    'O': row['OP'],
                    'BS': row['BS'],
                    'SN': row['SON'],
                    'SOLN': row['SOLN'],
                    'B':row['B'],
                    'S':row['S'],
                    'SO':row['SO'],
                    'SL':row['SL']
                     }
                sdfigureS_as_dict.append(sdfigure_as_dict)
         return sdfigureS_as_dict

    except Exception as e:
         return {"Error": str(e)}



def sodashlist(alert,number,version):
    sodashlistS_as_dict=[]

    try:
     with pymssql.connect(server, user, password, database) as conn:
         with conn.cursor(as_dict=True) as cursor:
             cursor.callproc('Admin_Toolbox_Alerts', (alert, number,version))
             for row in cursor:
                sodashlist_as_dict= {
                    'SO_ID': row['SO_ID'],
                    'RECIPIENT': row['RECIPIENT'],
                    'DATE': row['DATE']
                     }
                sodashlistS_as_dict.append(sodashlist_as_dict)
         return sodashlistS_as_dict

    except Exception as e:
         return {"Error": str(e)}



def sodashbacklockedshort(version):
    sodashlistS_as_dict=[]
    try:
     with pymssql.connect(server, user, password, database) as conn:
         with conn.cursor(as_dict=True) as cursor:
             cursor.callproc('Admin_Toolbox_BackOrder', (version))
             for row in cursor:
                sodashlist_as_dict= {
                    'SO_ID': row['SO_ID'],
                    'LINE_NO': row['SO_LINE_NO'],
                    'SHIP_DATE': row['ORDER_DATE']
                     }
                sodashlistS_as_dict.append(sodashlist_as_dict)
         return sodashlistS_as_dict

    except Exception as e:
         return {"Error": str(e)}


def sodashshipmentshort(version):
    sodashlistS_as_dict=[]
    try:
     with pymssql.connect(server, user, password, database) as conn:
         with conn.cursor(as_dict=True) as cursor:
             cursor.callproc('Admin_Toolbox_SHIPMENT', (version))
             for row in cursor:
                sodashlist_as_dict= {
                    'SO_ID': row['SO_ID'],
                    'SHIP_VIA': row['SHIP_VIA'],
                    'BOL': row['BILL_OF_LADING']
                     }
                sodashlistS_as_dict.append(sodashlist_as_dict)
         return sodashlistS_as_dict

    except Exception as e:
         return {"Error": str(e)}



def notifications(alert, number, version):
    sodashlistS_as_dict=[]

    try:
     with pymssql.connect(server, user, password, database) as conn:
         with conn.cursor(as_dict=True) as cursor:
             cursor.callproc('Admin_Toolbox_Alerts', (alert, number , version))
             for row in cursor:
                sodashlist_as_dict= {
                    'SO_ID': row['SO_ID'],
                    'ALERT': row['ALERT'],
                    'SUBJECT': row['SUBJECT'],
                    'RECIPIENT': row['RECIPIENT'],
                    'DATE': row['DATE'],
                     }
                sodashlistS_as_dict.append(sodashlist_as_dict)
         return sodashlistS_as_dict

    except Exception as e:
         return {"Error": str(e)}



def notificationsbyso(soid,alert):
    sodashlistS_as_dict=[]

    try:
     with pymssql.connect(server, user, password, database) as conn:
         with conn.cursor(as_dict=True) as cursor:
             cursor.callproc('Admin_Toolbox_Alerts_BySO', (soid, alert))
             for row in cursor:
                sodashlist_as_dict= {
                    'SO_ID': row['SO_ID'],
                    'ALERT': row['ALERT'],
                    'SUBJECT': row['SUBJECT'],
                    'RECIPIENT': row['RECIPIENT'],
                    'DATE': row['DATE'],
                     }
                sodashlistS_as_dict.append(sodashlist_as_dict)
         return sodashlistS_as_dict

    except Exception as e:
         return {"Error": str(e)}


def graphs(gtype):
    sodashlistS_as_dict=[]

    try:
     with pymssql.connect(server, user, password, database) as conn:
         with conn.cursor(as_dict=True) as cursor:
             cursor.callproc('[dbo].[Admin_Toolbox_Graph]', ( gtype ))
             for row in cursor:
                sodashlist_as_dict= {
                    'NAME': row['NAME'],
                    'NUMBER': row['NUMBER'],
                     }
                sodashlistS_as_dict.append(sodashlist_as_dict)
         return sodashlistS_as_dict

    except Exception as e:
         return {"Error": str(e)}


def specialnotifications(alert):

    sodashlistS_as_dict = []
    sodashlist_as_dict = []

    try:
     with pymssql.connect(server, user, password, database) as conn:
         with conn.cursor(as_dict=True) as cursor:
             cursor.callproc('Admin_Toolbox_Special_Notifications', (alert))
             for row in cursor:

                 if (alert == repr(0)):
                    sodashlist_as_dict = {
                        'SO_ID': row['SO_ID'],
                        'QUANTITY': row['QUANTITY'],
                        'ACTION_DATE': row['ACTION_DATE']
                         }
                 if ( alert == repr(1)):
                    sodashlist_as_dict = {
                        'SO_ID': row['SO_ID'],
                        'REV_SHIP_DATE': row['REV_SHIP_DATE'],
                        'PART_ID': row['PART_ID'],
                        'SHIPTO_NAME': row['SHIPTO_NAME']
                         }
                 if ( alert == repr(2)):
                    sodashlist_as_dict = {
                        'SO_ID': row['SO_ID'],
                        'PART_ID': row['PART_ID'],
                        'SERIAL_NUMBER': row['SERIAL_NUMBER'],
                        'SO_DESC': row['SO_DESC'],
                         'AMOUNT': row['AMOUNT'],
                         'CUSTOMER_ID': row['CUSTOMER_ID'],
                         'SHIP_TO_CUST': row['SHIP_TO_CUST'],
                         }
                 print(sodashlist_as_dict)
                 sodashlistS_as_dict.append(sodashlist_as_dict)

         return sodashlistS_as_dict

    except Exception as e:
         return {"Error": str(e)}



def eepromlist():
    try:
        cofas_as_dict=[]
        cur = conn.cursor()
        cur.execute('select distinct(ltrim(rtrim(IXI_EEPROM_LOG.JOB_ID))),JOB_DESC,ltrim(rtrim(PART_ID)),ORDER_QTY,JCFJM_USER_6,REV_ORDER_QTY  from IXI_EEPROM_LOG inner join JCFJM on IXI_EEPROM_LOG.JOB_ID=JCFJM.JOB_ID order by ltrim(rtrim(IXI_EEPROM_LOG.JOB_ID)) desc,ltrim(rtrim(PART_ID)) ')
        rows = cur.fetchall()
        for row in rows:
             cofa_as_dict= {
             'JOB_ID': row[0],
             'JOB_DESC': row[1],
             'PART_ID': row[2],
             'ORDER_QTY': row[3],
             'PROGRAMMED': row[4],
             'REV_ORDER_QTY': row[5],
             }
             cofas_as_dict.append(cofa_as_dict)
        return cofas_as_dict
    except Exception as e:
          return {"Error":"There is problem in connecting to database"}

def eepromdetail(jobid):
    try:
        cofas_as_dict=[]
        cur = conn.cursor()
        # cur.execute('select ltrim(rtrim(JOB_ID)),ltrim(rtrim(USER_NAME)),MACHIN_NAME,CARTRIDGE_ID,INSERT_DATE,SYNCED from IXI_EEPROM_LOG where JOB_ID='+repr(110974)+' order by INSERT_DATE desc')
        s='select ltrim(rtrim(JOB_ID)),ltrim(rtrim(USER_NAME)),MACHIN_NAME,CARTRIDGE_ID,INSERT_DATE,SYNCED from IXI_EEPROM_LOG  where JOB_ID='+repr(jobid)+'order by INSERT_DATE desc'
        print(s)
        cur.execute(s)
        rows = cur.fetchall()
        for row in rows:
             cofa_as_dict= {
             'JOB_ID': row[0],
             'USER_NAME': row[1],
             'MACHIN_NAME': row[2],
             'CARTRIDGE_ID': row[3],
             'INSERT_DATE': row[4],
             'SYNCED': row[5],
             }
             cofas_as_dict.append(cofa_as_dict)
        return cofas_as_dict
    except Exception as e:
          return {"Error":"There is problem in connecting to database"}


def so(soid):

    SoInfo_as_dict=[]

    try:
     with pymssql.connect(server, user, password, database) as conn:
         with conn.cursor(as_dict=True) as cursor:
             args = [soid]
             cursor.callproc('Admin_Toolbox_SO',args )
             for row in cursor:
                Info_as_dict= {

                    'SO_ID': row['SO_ID'],
                    'SO_TYPE': row['SO_TYPE'],
                    'ORDER_DATE': row['ORDER_DATE'],
                    'ORDER_CLASS': row['ORDER_CLASS'],
                    'TERMS_CODE': row['TERMS_CODE'],
                    'FOB': row['FOB'],
                    'SALESMAN_ID': row['SALESMAN_ID'],
                    'SALES_REGION': row['SALES_REGION'],
                    'FREIGHT_CODE': row['FREIGHT_CODE'],

                    'SO_STATUS': row['SO_STATUS'],
                    'REFERENCE': row['REFERENCE'],
                    'SHIP_METHOD': row['SHIP_METHOD'],
                    'E_MAIL': row['E_MAIL'],
                    'SHIPMETHOD': row['SHIPMETHOD'],

                    'SHIP_TO_CUST': row['SHIP_TO_CUST'],
                    'SHIPTO_NAME': row['SHIPTO_NAME'],




                      'SHIPTO_ADDRESS_1': row['SHIPTO_ADDRESS_1'],
                      'SHIPTO_ADDRESS_2': row['SHIPTO_ADDRESS_2'],
                      'SHIPTO_ADDRESS_3': row['SHIPTO_ADDRESS_3'],
                      'SHIPTO_CITY': row['SHIPTO_CITY'],
                      'SHIPTO_STATE': row['SHIPTO_STATE'],
                      'SHIPTO_ZIPECODE': row['SHIPTO_ZIPECODE'],
                      'SHIPDATE': row['SHIPDATE'],
                      'SHIPTO_LAST_NAME': row['SHIPTO_LAST_NAME'],
                      'SHIPTO_FIRST_NAME': row['SHIPTO_FIRST_NAME'],
                      'SHIPTOPHONE_NO': row['SHIPTOPHONE_NO'],
                      'SHIPTO_EMAIL': row['SHIPTO_EMAIL'],






                      'BILLTO_NAME': row['BILLTO_NAME'],
                      'BILL_TO_CUST': row['BILL_TO_CUST'],
                      'BILLTO_ADDRESS_1': row['BILLTO_ADDRESS_1'],
                      'BILLTO_ADDRESS_2': row['BILLTO_ADDRESS_2'],
                      'BILLTO_ADDRESS_3': row['BILLTO_ADDRESS_3'],
                      'BILLTO.CITY': row['BILLTO.CITY'],
                      'BILLTO.STATE': row['BILLTO.STATE'],
                      'BILLTO_COUNTRY': row['BILLTO_COUNTRY'],
                      'BILLTO.ZIP_CODE': row['BILLTO.ZIP_CODE'],
                      'BILLTO_PHONE_NO': row['BILLTO_PHONE_NO'],
                      'BILLTO_E_MAIL': row['BILLTO_E_MAIL'],





                      'SOLDTO_CUST': row['SOLDTO_CUST'],
                      'SOLDTO_NAME': row['SOLDTO_NAME'],
                      'SOLDTO_ADDRESS_1': row['SOLDTO_ADDRESS_1'],
                      'SOLDTO_ADDRESS_2': row['SOLDTO_ADDRESS_2'],
                      'SOLDTO_ADDRESS_3': row['SOLDTO_ADDRESS_3'],
                      'SOLDTO.CITY': row['SOLDTO.CITY'],
                      'SOLDTO.STATE': row['SOLDTO.STATE'],
                      'SOLDTO_COUNTRY': row['SOLDTO_COUNTRY'],
                      'SOLDTO.ZIP_CODE': row['SOLDTO.ZIP_CODE'],



                     }
                SoInfo_as_dict.append(Info_as_dict)
         return SoInfo_as_dict

    except Exception as e:
         return {"Error": str(e)}



def sopicklist(soid,beforedate):
    try:
        cofas_as_dict=[]
        cur = conn.cursor()
        # cur.execute('select ltrim(rtrim(JOB_ID)),ltrim(rtrim(USER_NAME)),MACHIN_NAME,CARTRIDGE_ID,INSERT_DATE,SYNCED from IXI_EEPROM_LOG where JOB_ID='+repr(110974)+' order by INSERT_DATE desc')
        s='select ltrim(rtrim(D.SO_LINE_NO)),ltrim(rtrim(D.STORES_CODE)),ltrim(rtrim(D.SO_ID)),ltrim(rtrim(D.PART_ID)),ltrim(rtrim(P.PART_DESC)),ltrim(rtrim(P.PART_UM)),ltrim(rtrim(ON_HAND_QTY)),ltrim(rtrim(STOCK_LOCATION)),ltrim(rtrim(SCH_SHIP_DATE)),ltrim(rtrim(LOT_ID)) from ICFPM as P inner join SOFOD as D on D.PART_ID=P.PART_ID left join LTFLS as L on L.PART_ID=D.PART_ID where SO_ID='+repr(soid)+' and SCH_SHIP_DATE<'+repr(beforedate)+ ' and (ON_HAND_QTY>0 or ON_HAND_QTY is null)'
        print(s)
        cur.execute(s)
        rows = cur.fetchall()
        for row in rows:
             cofa_as_dict= {
             'SO_LINE_NO': row[0],
             'STORES_CODE': row[1],
             'SO_ID': row[2],
             'PART_ID': row[3],
             'PART_DESC': row[4],
             'PART_UM': row[5],
             'ON_HAND_QTY': row[6],
             'STOCK_LOCATION': row[7],
             'SCH_SHIP_DATE': row[8],
             'LOT_ID': row[9]
             }
             cofas_as_dict.append(cofa_as_dict)
        return cofas_as_dict
    except Exception as e:
          return {"Error":"There is problem in connecting to database"}



def bom(assemblyid):
    sodashlistS_as_dict=[]
    try:
     with pymssql.connect(server, user, password, database) as conn:
         with conn.cursor(as_dict=True) as cursor:
             args = [assemblyid]
             cursor.callproc('Admin_Toolbox_BOM', args)
             for row in cursor:
                sodashlist_as_dict= {
                    'Level': row['Level'],
                    'ASSEMBLY_ID': row['ASSEMBLY_ID'],
                    'COMPONENT_ID': row['COMPONENT_ID'],
                    'DES': row['DES']
                     }
                sodashlistS_as_dict.append(sodashlist_as_dict)
         return sodashlistS_as_dict

    except Exception as e:
         return {"Error": str(e)}


def soassembly(assemblyid):
    sodashlistS_as_dict=[]
    try:
     with pymssql.connect(server, user, password, database) as conn:
         with conn.cursor(as_dict=True) as cursor:
             args = [assemblyid]
             cursor.callproc('Admin_Toolbox_SO_AssemblyID', args)
             for row in cursor:
                sodashlist_as_dict= {
                    'SO_ID': row['SO_ID'],
                    'PART_ID': row['PART_ID']
                     }
                sodashlistS_as_dict.append(sodashlist_as_dict)
         return sodashlistS_as_dict

    except Exception as e:
         return {"Error": str(e)}








