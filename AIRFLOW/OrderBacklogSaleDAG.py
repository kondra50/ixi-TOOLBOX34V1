from airflow import DAG
#from airflow.operators import  python_operator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

import pymssql
import requests,json,os,time
import xml
import smtplib
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element as EL
from email.mime.application import MIMEApplication
from email.mime.multipart import  MIMEMultipart
conn = pymssql.connect(host='192.168.3.40', user='sysdba', password='e$1s_s', database='ESIDB')
cur = conn.cursor()


def GenerateAndSend(INVOICE_ID):
    se = requests.Session()
    se.auth = ('jasperadmin', 'jasperadmin')
    se.headers={'content-type':'application/text'}
    bas_ULR='http://192.168.3.146:8051/jasperserver/rest/'
    response = se.get(bas_ULR+'resource/reports/Invoice')
    ECUDU_DESCRIPTIV=response.text
    mystr=ECUDU_DESCRIPTIV.split('<resourceDescriptor name="Invoice" wsType="reportUnit" uriString="/reports/Invoice" isNew="false">')
    myparam='<resourceDescriptor name="Invoice" wsType="reportUnit" uriString="/reports/Invoice" isNew="false"><parameter name="INVOICE_ID">'+ str(INVOICE_ID)+'</parameter>'
    print(myparam+mystr[1])
    response = se.put(bas_ULR+'report/Invoice',data=myparam+mystr[1])
    tree = ET.fromstring(response.content)
    UUID = tree.findall('uuid')[0].text
    print(UUID)
    url=bas_ULR+'report/'+UUID+'?file=ecudureport'
    response = se.get(bas_ULR+'report/'+UUID+'?file=report')

    try:

        msg = MIMEMultipart()
        msg['Subject'] = '*********TEST********* Review and Confirm Invoice'
        msg['From'] = "mehrdadn@integenx.com"
        msg['To'] = "mehrdadn@integenx.com" #leilae@integenx.com;
        img1 = MIMEApplication(response.content, 'pdf')
        img1['Content-Disposition'] = 'attachment; filename="'+str(INVOICE_ID)+'.pdf"'
        msg.attach(img1)
        s = smtplib.SMTP('IXI-EXCH.microchipbiotech.com')
        s.send_message(msg)
        s.quit()
    except Exception as e:
        print(e)
def Invoice_JOB():

    try:
        s='select INVOICE_NUMBER from ARFIM where INVOICE_DATE=  DATEADD(day, -10, CONVERT (date, SYSDATETIME())) '
        #s='select INVOICE_NUMBER from ARFIM where INVOICE_DATE=  cast(getdate() as date)'
        cur.execute(s)
        while True:
            row = cur.fetchone()
            print(row[0])
            GenerateAndSend(row[0])
            if row is None:
                #return 'Done'
                break
                #yield row
                #results = cur.fetchall()
    except Exception as e :
            print(e)\


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 6, 1),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '@hourly',
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('send_invoice', default_args=default_args)
send_invoice_task = \
    PythonOperator(task_id='send_invoice',
                   provide_context=True,
                   python_callable=Invoice_JOB,
                   dag=dag)






