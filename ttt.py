# import requests
# from bs4 import BeautifulSoup
from urllib.parse import urljoin
from os.path import basename

# url='http://www.cde.ca.gov/ds/sp/ai/'
#
# response= requests.get(url)
#
# html_doc=response.text
#
# soup= BeautifulSoup(html_doc)

#print(soup.prettify())

# a_tag=soup.find_all('a')
# i=0
# for a in a_tag:
#     #if (str(a.get('href')).find(".pdf",0))>0:
#     if (str(a.get('href')).find('.xls',0))>0:
#         print(a.get('href'))
#         i+=1
#         with open('C:\\Python34\\ixi_TBOX34\\tmp\\t+'+str(i)+'+.xls', 'wb') as f:
#         #with open("/tmp/" + basename(url), 'wb') as f:
#             print("Downloading", url)
#             # Downloading http://www.cde.ca.gov/ds/sp/ai/documents/sat02.xls
#             data = requests.get(url).content
#             f.write(data)
import os
import time,json
import requests
from xml.etree import ElementTree as ET
# path='C:\Python34\ixi_TBOX34\PLM_FILES'
# while (True):
#
#     filenames = next(os.walk(path))
#     plmfile=[f for f in filenames[2]  if '.plm' in str(f)]
#     for f2 in plmfile:
#         print(f2)
#         oldfile=path+'\\'+f2
#         newfile=path+'\\PROCESSED\\'+f2
#         os.rename(oldfile, newfile)
#     time.sleep(10)
try:
    # with open('result.json') as fh:
    #
    #     mydata = fh.read()
    s = requests.Session()
    s.auth = ('jasperadmin', 'jasperadmin')
    s.headers={'content-type':'application/text'}
    bas_ULR='http://192.168.3.146:8051/jasperserver/rest/'
    response = s.get(bas_ULR+'resource/reports/ECUDU')

    ECUDU_SCHEME=response.text



    response = s.put(bas_ULR+'report',data=ECUDU_SCHEME)

    print(response.text)
    tree = ET.fromstring(response.content)
    UUID = tree.findall('uuid')[0].text

    # url='http://192.168.3.146:8051/jasperserver/rest/report/'+UUID+'?file=ecudureport'
    # response = requests.get('http://192.168.3.146:8051/jasperserver/rest/report/'+UUID+'?file=report',
    #              # auth=('jasperadmin', 'jasperadmin'),
    #              headers={'content-type':'application/json','Authorization':'Basic amFzcGVyYWRtaW46amFzcGVyYWRtaW4='}
    #                  )
    url=bas_ULR+'report/'+UUID+'?file=ecudureport'
    response = s.get(bas_ULR+'report/'+UUID+'?file=report')
    with open('C:\Python34\ixi_TBOX34\PLM_FILES\metadata1.pdf', 'wb') as f:
        f.write(response.content)
        #print(response.text)

    # print(data)
except Exception as e:
    print(e)
    exit()



