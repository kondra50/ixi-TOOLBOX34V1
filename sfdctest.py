from simple_salesforce import Salesforce
import salesforce_reporting
import requests,json
from flask import jsonify
from SFDC import  dbmodels
sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
analytic_sf = salesforce_reporting.Connection('3MVG99OxTyEMCQ3glBkdKh4SE2HJs4uODXEl2Fux.LFlCzqkgs9Tr8XLqmCvUsOSdsVpbGoj9xhN5f4hpJ2OZ', '86072956447270870',
'customerservice@integenx.com', 'password123453GKZny4jRWgmXNUmvFjzKhggQ', 'na13')
list=sf.query("SELECT id, Name  from Organization")
      #list=sf.query("SELECT Approved FROM [Expandable Sales Orders] ")
dict=list["records"]
opps_as_dict=[]
for record in  dict:
    opp_as_dict = {'Name' :  record["Name"]}
    opps_as_dict.append(opp_as_dict)

print(opps_as_dict)