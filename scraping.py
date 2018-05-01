import itertools
from operator import itemgetter

students = [
    {'name': 'alex','class': 'A'},
    {'name': 'richard','class': 'A'},
    {'name': 'john','class': 'C'},
    {'name': 'harry','class': 'B'},
    {'name': 'rudolf','class': 'B'},
    {'name': 'charlie','class': 'E'},
    {'name': 'budi','class': 'C'},
    {'name': 'gabriel','class': 'B'},
    {'name': 'dessy', 'class': 'B'}
]




import requests,json

# The California city whose city manager earns the most total wage per population of its city in 2012
# import csv
# import requests
# from io import BytesIO
# from zipfile import ZipFile
# YEAR = 2012
# def foosalary(row):
#     return float(row['Total Wages']) / int(row['Entity Population'])
#
# url = 'http://publicpay.ca.gov/Reports/RawExport.aspx?file=%s_City.zip' % YEAR
# print("Downloading:", url)
# resp = requests.get(url)
#
# with ZipFile(BytesIO(resp.content)) as zfile:
#     fname = zfile.filelist[0].filename # 2012_City.csv
#     rows = zfile.read(fname).decode('latin-1').splitlines()
#     # first 4 lines are Disclaimer lines
#     managers = [r for r in csv.DictReader(rows[4:]) if r['Position'].lower() == 'city manager'
#                                                      and r['Total Wages']]
#     topman = max(managers, key = foosalary)
#     print("City: %s; Pay-per-Capita: $%s" % (topman['Entity Name'], int(foosalary(topman))))
# City: Industry; Pay-per-Capita: $465

#
# from lxml import html
# from subprocess import check_output
# from urllib.parse import urljoin
# import requests
# url = 'http://www.supremecourt.gov/oral_arguments/argument_transcript.aspx'
# doc = html.fromstring(requests.get(url).text)
# # get the most recent ruling, e.g. the top of table
# href = doc.cssselect('table.datatables tr a')[0].attrib['href']
# # download PDF
# pdf_url = urljoin(url, href)
# with open("/tmp/t.pdf", 'wb') as f:
#     f.write(requests.get(pdf_url).content)
# # punt to shell and run pdftotext
# # http://www.foolabs.com/xpdf/download.html
# txt = check_output("pdftotext -layout /tmp/t.pdf -", shell = True).decode()
# print(txt.count("(Laughter.)"))


# from urllib.request import urlopen
# url='http://maps.googleapis.com/maps/api/geocode/json'
# my_params = {'address': '100 Broadway, New York, NY, U.S.A',
#              'language': 'ca'}
# responde=requests.get(url,my_params)
# myjson = responde.text
# print(myjson)
# # print(myjson['results'][0]['address_components'])
# decoded_data = json.loads(myjson)
# print(decoded_data)
# #
#
# import urllib, json
# url = "http://maps.googleapis.com/maps/api/geocode/json?address=google"
# response=requests.get(url)
# #response = urllib.urlopen(url)
# #data = json.loads(response.json)
# print(list(response))


# import urllib
# import json
#
# response = urllib.urlopen('https://api.instagram.com/v1/tags/pizza/media/XXXXXX')
# data = json.load(response)
# print(data)

# import requests
# r = requests.get("https://analytics.usa.gov/data/live/ie.json")
# mytxt=r.text
# print(mytxt)
# myjson=json.loads(mytxt)
# print(myjson)
# print(r.json()['totals']['ie_version']['6.0'])
# print(myjson['totals']['ie_version']['6.0'])
# import pandas
# input = [
#           (11013331, 'KAT'),
#           (9085267,  'NOT'),
#           (5238761,  'ETH'),
#           (5349618,  'ETH'),
#           (11788544, 'NOT'),
#           (962142,   'ETH'),
#           (7795297,  'ETH'),
#           (7341464,  'ETH'),
#           (9843236,  'KAT'),
#           (5594916,  'ETH'),
#           (1550003,  'ETH')
#         ]
#
# for v,k in input:
#     print(k)
#
# result = pandas.DataFrame(input).groupby(1).groups
# print(result['KAT'])

# from collections import defaultdict
# res = defaultdict(list)
# for v, k in input: res[k].append(v)
# print(list(res))

