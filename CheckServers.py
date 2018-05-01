import requests,time,smtplib,socket
from datetime import datetime

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

App = ""
max_number=0
def sendemail(Code,App):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login('thrnafism@gmail.com','INTgsm7!7')
    message='Error!('+str(Code)+') '+str(App)+' is not responding at '+str(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
    server.sendmail('4159994618','4159994618@txt.att.net',message)
    #print(str(datetime.now().strftime('%H:%M:%S')))

def reset():
     time.sleep(1800)
     global max_number
     max_number=0





while(True):

    if (max_number==3): reset()

    ########################################## INTRANET#############################################

    try:

       url = 'http://192.168.3.146'
       req = Request(url)
       response = urlopen(req)
    except HTTPError as e:
        print('The Intranet Server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        sendemail(e.code,'Intranet Server');max_number+=1;time.sleep(10)
    except URLError as e:
        print('We failed to reach Intranet Server.')
        print('Reason: ', e.reason)
        sendemail(e.reason,'Intranet Server');max_number+=1;time.sleep(10)
    except Exception as e:
        print('We failed to reach Intranet Server.')
        print('Reason: ', e)
        sendemail(e,'Intranet Server');max_number+=1;time.sleep(10)
    else:
        print ('Intranet Server is working fine')


    ########################################## EXPANDABLE API SERVER #############################################


    try:

       url = 'http://192.168.3.146:9070'
       req = Request(url)
       response = urlopen(req)
    except HTTPError as e:
        print('The Expandable API Server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        sendemail(e.code,'Expandable API Server');max_number+=1;time.sleep(10)
    except URLError as e:
        print('We failed to reach Expandable API Server.')
        print('Reason: ', e.reason)
        sendemail(e.reason,'Expandable API Server');max_number+=1;time.sleep(10)
    except Exception as e:
        print('We failed to reach Expandable API Server.')
        print('Reason: ', e)
        sendemail(e,'Expandable API Server');max_number+=1;time.sleep(10)

    else:
        print ('Expandable API Server is working fine')




    ########################################## JASPER #############################################

    try:

       url = 'http://192.168.3.146:8051/jasperserver'
       req = Request(url)
       response = urlopen(req)
    except HTTPError as e:
        print('The Jasper Report Server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        sendemail(e.code,'Jasper Report Server');max_number+=1;time.sleep(10)
    except URLError as e:
        print('We failed to reach Jasper Report Server.')
        print('Reason: ', e.reason)
        sendemail(e.reason,'Jasper Report Server');max_number+=1;time.sleep(10)
    except Exception as e:
         print('We failed to reach Jasper Report Server.')
         print('Reason: ', e)
         sendemail(e,'Jasper Report Server');max_number+=1;time.sleep(10)
    else:
        print ('Jasper Report Server is working fine')














    time.sleep(2)






