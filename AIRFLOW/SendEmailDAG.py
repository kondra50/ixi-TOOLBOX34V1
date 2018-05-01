from __future__ import print_function
from email.mime.application import MIMEApplication
from email.mime.multipart import  MIMEMultipart
import smtplib

from builtins import range
import airflow
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG

import time
from pprint import pprint


def send_email(random_base):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = '*********TEST********* Review and Confirm Invoice'
        msg['From'] = "mehrdadn@integenx.com"
        msg['To'] = "mehrdadn@integenx.com" #leilae@integenx.com;
        img1 = MIMEApplication("THIS IS TEST", 'pdf')
        img1['Content-Disposition'] = 'attachment; filename="'+str(12)+'.pdf"'
        msg.attach(img1)
        s = smtplib.SMTP('IXI-EXCH.microchipbiotech.com')
        s.send_message(msg)
        s.quit()
    except Exception as e:
        print(e)

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
    'schedule_interval':'*/5 * * * *',
}

dag = DAG(
    dag_id='sendemail', default_args=args,
    schedule_interval=None)


def my_sleeping_function(random_base):
    """This is a function that will run within the DAG execution"""
    time.sleep(random_base)


def print_context(ds, **kwargs):
    pprint(kwargs)
    print(ds)
    return 'Whatever you return gets printed in the logs'

run_this = PythonOperator(
    task_id='send_email',
    provide_context=True,
    python_callable=send_email,
    dag=dag)
# task = PythonOperator(
#         task_id='sleep_for_' ,
#         python_callable=send_email,
#         op_kwargs={'random_base'},
#         dag=dag)
#
# task.set_upstream(run_this)
# Generate 10 sleeping tasks, sleeping from 0 to 9 seconds respectively
# for i in range(10):
#     task = PythonOperator(
#         task_id='sleep_for_' + str(i),
#         python_callable=send_email,
#         op_kwargs={'random_base': float(i) / 10},
#         dag=dag)
#
#     task.set_upstream(run_this)