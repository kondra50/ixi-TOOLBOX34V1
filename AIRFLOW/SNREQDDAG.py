from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta
import pymssql
from jinja2 import Template
resaults_as_dict=[]
s="""
USE ESIDB
SELECT PART_ID, PART_DESC, SN_REQD, SN_REQD_INV FROM ICFPM WHERE SN_REQD = 'N' AND SN_REQD_INV = 'Y'
"""
conn = pymssql.connect(host='192.168.3.40', user='sysdba', password='e$1s_s', database='ESI_JUN_2017')
# t = Template(" <ul>{% for row in rows %}<li>{{row.PART_ID}}</li>{% endfor %}</ul>")
t = Template(
             '<table style="width:100%"><tr><th>PART_ID</th><th>PART_DESC</th><th>PART_UM</th><th>PO_ID</th><th>QUANTITY</th><th>CREATED_BY</th><th>TIME_LAST_UPDT</th></tr>'
             '{% for row in rows %}<tr><td>{{row.PART_ID}}</td><td>{{row.PART_DESC}}</td><td>{{row.PART_UM}}</td><td>{{row.PO_ID}}</td><td>{{row.QUANTITY}}</td><td>{{row.CREATED_BY}}</td><td>{{row.TIME_LAST_UPDT}}</td></tr>{% endfor %}'
             '</table>')
def getdata():
    try:
        cur = conn.cursor()
        cur.execute(s)
        for row in cur:
            val = row
            res_as_dict = {
                                'PART_ID' : val[0].strip(),
                                'PART_DESC' : val[1].strip(),
                                'PART_UM' : val[2],
                                'PO_ID' : val[3],
                                'QUANTITY' : val[4],
                                'CREATED_BY' : val[5],
                                'TIME_LAST_UPDT' : val[6],
                                }
            resaults_as_dict.append(res_as_dict)
    except Exception as e:
        res_as_dict = {'ERROR': str(e)}
        resaults_as_dict.append(res_as_dict)

    finally:
         cur.close()
         #conn.commit()
         conn.close()
         return resaults_as_dict
dadaset=getdata()
if not bool(dadaset):
    print("There is no result")
else:
    print(dadaset)
    body=t.render(rows=dadaset)
    print(body)

default_args = {
    'owner': 'IXI',
    'depends_on_past': False,
    'start_date': datetime(2017, 10, 4),
    'email': ['mehrdadn@integenx.com.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)}

dag = DAG('IncominQC', description='Check every 15 min to see if there is any incoming QC',
          schedule_interval='*/15 * * * *',
          start_date=datetime(2017, 10, 4), catchup=False)
email=EmailOperator(
   task_id='sendemail',
   to='mehrdadn@integenx.com',
   subject='IncominQC',
   html_content=t.render(rows=dadaset),
   dag=dag)
getdata_operator = PythonOperator(task_id='Fetchdata', python_callable=getdata , dag=dag)
email>>getdata_operator