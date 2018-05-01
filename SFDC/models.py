from simple_salesforce import Salesforce
import salesforce_reporting
import requests,json
from flask import jsonify
from SFDC import  dbmodels
sf = Salesforce(username='', password='', security_token='3GKZny4jRWggQ')
analytic_sf = salesforce_reporting.Connection('3MVG99OxTyEMCQ3glBkdKh4SE2HJs4uODXEl2Fux.LFlCzqkgs9Tr8XLqmCvUsOSdsVpbGoj9xhN5f4hpJ2OZ', '86072956447270870',
'cgenx.com', 'passKhggQ', 'na13')

report=analytic_sf.get_report('00Oa0000008uK2BEAU', filters=None, details=True)
parser = salesforce_reporting.ReportParser(report)
dict=parser.records()



class Opportunity():
    def __int__(self,AccountId,Amount,CloseDate,OwnerId,FiscalYear,CreatedById):
         self.AccountId= AccountId,
         self.Amount= Amount,
         self.CloseDate= CloseDate,
         self.OwnerId= OwnerId,
         self.FiscalYear= FiscalYear,
         self.CreatedById= CreatedById,

    def Load(self):
         try:
          #list=sf.query("SELECT AccountId,Amount,CloseDate,OwnerId,FiscalYear,CreatedById FROM Opportunity ")
          #sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
          list=sf.query("SELECT AccountId,Amount,CloseDate,OwnerId,FiscalYear,CreatedById FROM Opportunity ")
          #list=sf.query("SELECT Approved FROM [Expandable Sales Orders] ")
          dict=list["records"]
          #print(JobId)
          #cursor.callproc("select * from LDFEM")
          #self.__int__(self,cursor(0)[0],cursor(0)[1],cursor(0)[2],cursor(0)[3],cursor(0)[4],cursor(0)[5],cursor(0)[6],cursor(0)[7],cursor(0)[8],cursor(0)[9])
          for record in dict:
               mylist=[]
               mylist.append(record)
               val = mylist[0]
               self.__int__(self,'1','2','3','4','6','6')

         except Exception as e:
            print(e)
         finally:
          return self




    @property
    def serialize(Self):
        return  {
                'AccountId': Self.AccountId[0],
                'Amount': Self.Amount[0],
                'CloseDate':Self.CloseDate[0],
                'OwnerId': Self.OwnerId[0],
                'FiscalYear' : Self.FiscalYear[0],
                'CreatedById':Self.CreatedById[0],
                }

    @property
    def allOpportunity(base):
      #sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
      list=sf.query("SELECT AccountId,Amount,CloseDate,OwnerId,FiscalYear,CreatedById FROM Opportunity ")
      #list=sf.query("SELECT Approved FROM [Expandable Sales Orders] ")
      dict=list["records"]
      opps_as_dict=[]
      for record in  dict:
            opp_as_dict = {
                   'AccountId' :  record["AccountId"]}
            opps_as_dict.append(opp_as_dict)

      return opps_as_dict

def Opportunities():
      #sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
      list=sf.query("SELECT AccountId,Amount,CloseDate,OwnerId,FiscalYear,CreatedById FROM Opportunity ")
      #list=sf.query("SELECT Approved FROM [Expandable Sales Orders] ")
      dict=list["records"]
      opps_as_dict=[]
      for record in  dict:
            opp_as_dict = {
                   'AccountId' :  record["AccountId"],
                   'Amount' :  record["Amount"],
                   'CloseDate' :  record["CloseDate"],
                   'FiscalYear' :  record["FiscalYear"],
                   'CreatedById' :  record["CreatedById"],}
            opps_as_dict.append(opp_as_dict)

      return opps_as_dict
def PriceBooks():
      #sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
      list=sf.query("SELECT Name,Description,IsActive,IsStandard FROM Pricebook2 ")
      #list=sf.query("SELECT Approved FROM [Expandable Sales Orders] ")
      dict=list["records"]
      pbs_as_dict=[]
      for record in  dict:
            pb_as_dict = {
                   'Name' :  record["Name"],
                   'Description' :  record["Description"],
                   'IsActive' :  record["IsActive"],
                   'IsStandard' :  record["IsStandard"],}
            pbs_as_dict.append(pb_as_dict)

      return pbs_as_dict

def Products():
      #sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
      list=sf.query("SELECT ProductCode,Name,IsActive,Family,Description FROM Product2 ")
      #list=sf.query("SELECT Approved FROM [Expandable Sales Orders] ")
      dict=list["records"]
      prs_as_dict=[]
      for record in  dict:
            pr_as_dict = {
                   'Name' :  record["Name"],
                   'Description' :  record["Description"],
                   'IsActive' :  record["IsActive"],
                   'Family' :  record["Family"],
                   'ProductCode' :  record["ProductCode"],}
            prs_as_dict.append(pr_as_dict)

      return prs_as_dict

def Users():
      #sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
      list=sf.query("SELECT Alias,City,CompanyName,ContactId,Country,Department,Email FROM User ")
      #list=sf.query("SELECT Approved FROM [Expandable Sales Orders] ")
      dict=list["records"]
      prs_as_dict=[]
      for record in  dict:
            pr_as_dict = {
                   'Alias' :  record["Alias"],
                   'City' :  record["City"],
                   'CompanyName' :  record["CompanyName"],
                   'ContactId' :  record["ContactId"],
                   'Country' :  record["Country"],
                   'Department' :  record["Department"],
                   'Email' :  record["Email"],
            }
            prs_as_dict.append(pr_as_dict)

      return prs_as_dict

def Accounts():
      #sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
      list=sf.query("SELECT AccountNumber,Description,Industry,BillingCity,BillingCountry,LastActivityDate,Name,OwnerId,Phone FROM Account ")
      #list=sf.query("SELECT Approved FROM [Expandable Sales Orders] ")
      dict=list["records"]
      prs_as_dict=[]
      for record in  dict:
            pr_as_dict = {
                   'AccountNumber' :  record["AccountNumber"],
                   'Description' :  record["Description"],
                   'Industry' :  record["Industry"],
                   'BillingCity' :  record["BillingCity"],
                   'BillingCountry' :  record["BillingCountry"],
                   'LastActivityDate' :  record["LastActivityDate"],
                   'Name' :  record["Name"],
                   'OwnerId' :  record["OwnerId"],
                   'Phone' :  record["Phone"],
            }
            prs_as_dict.append(pr_as_dict)

      return prs_as_dict


def Cases():
      #sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
      list=sf.query("SELECT AccountId,CaseNumber,ClosedDate,ContactId,Description FROM Case ")
      #list=sf.query("SELECT Approved FROM [Expandable Sales Orders] ")
      dict=list["records"]
      prs_as_dict=[]
      for record in  dict:
            pr_as_dict = {
                   'AccountId' :  record["AccountId"],
                   'CaseNumber' :  record["CaseNumber"],
                   'ClosedDate' :  record["ClosedDate"],
                   'ContactId' :  record["ContactId"],
                   'Description' :  record["Description"]
            }
            prs_as_dict.append(pr_as_dict)

      return prs_as_dict


def SOFOD():
    list=sf.query("SELECT ESI__SO_ID__c,ESI__PRODUCT_LINE__c,ESI__SO_LINE_NO__c,ESI__SO_LINE_STATUS__c,ESI__REV_SHIP_DATE__c,ESI__LAST_SHIP_NO__c,ESI__REV_ORDER_QTY__c,ESI__AMOUNT__c from ESI__Sales_Order_Detail__c")
    dict=list["records"]
    prs_as_dict=[]
    for record in  dict:
      rps_as_dict=[]
      all=''
      i=0
      rps_as_dict=[]
      for record in  dict:
            i=i+1
            rp_as_dict = {
                   'Sales Order Number' :  record['ESI__SO_ID__c'],
                   'Prod Line' :  record['ESI__PRODUCT_LINE__c'],
                   'Sales Order Line' :  record['ESI__SO_LINE_NO__c'],
                   'Line St' :  record['ESI__SO_LINE_STATUS__c'],
                   'Rev Ship' :  record['ESI__REV_SHIP_DATE__c'],
                   'Last Shipment' :  record['ESI__LAST_SHIP_NO__c'],
                   'Rev Ord Qty' :  record['ESI__REV_ORDER_QTY__c'],
                   'Amount' :  record['ESI__AMOUNT__c']
                   #'Opportunity Owner' :  record[15],
            }
            print (i)
            dbmodels.EXPUPDATE.FillSFDC7New(rp_as_dict)
            rps_as_dict.append(rp_as_dict)

      return rps_as_dict  #



def Reports():
      #sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
      list=sf.query("SELECT Id,Name,DeveloperName FROM Report ")
      #list=sf.query("SELECT Approved FROM [Expandable Sales Orders] ")
      dict=list["records"]
      rps_as_dict=[]
      for record in  dict:
            rp_as_dict = {
                   'Id' :  record["Id"],
                   'Name' :  record["Name"],
                   'DeveloperName' :  record["DeveloperName"],
            }
            rps_as_dict.append(rp_as_dict)

      return rps_as_dict


# def Run_Forecast_PIP-old():
#
#       report=analytic_sf.get_report('00Oa0000008uK2BEAU')
#       parser = salesforce_reporting.ReportParser(report)
#       dict=parser.records()
#       rps_as_dict=[]
#       all=''
#
#       try:
#          for record in  dict:
#               all=''
#               i=0
#               fileds=len(record)
#               while (i<fileds):
#                  strkey='Filed'+ str(i)
#                  strvalue= str(record[i]),
#                  one= strkey +':'+ str(strvalue[0])
#                  all= str(all)+''+ str(one)
#                  if (i!=(fileds-1)): all = all+','
#                  i=i+1
#               rp_as_dict = { all }
#               rps_as_dict.append(rp_as_dict)
#
#          return rps_as_dict
#
#       except Exception as e:
#           print(e)


def Run_Forecast_PIP():

      report=analytic_sf.get_report('00Oa0000008uK2BEAU')
      parser = salesforce_reporting.ReportParser(report)
      dict=parser.records()

      rps_as_dict=[]
      all=''
      i=0
      rps_as_dict=[]
      for record in  dict:
            i=i+1
            rp_as_dict = {
                   'Close Date' :  record[0],
                   'Account Owner' :  record[1],
                   'Opportunity Name' :  record[2],
                   'Expandable Customer ID' :  record[3],
                   'Account Name' :  record[4],
                   'Amount' :  record[5],
                   'Stage' :  record[6],
                   'Probability (%)' :  record[7],
                   'Created Date' :  record[8],
                   'Product Name' :  record[9],
                   'Quantity' :  record[10],
                   'Sales Price' :  record[11],
                   'Total Price' :  record[12],
                   'List Price' :  record[13],
                   'Opportunity ID' :  record[14]
                   #'Opportunity Owner' :  record[15],
            }
            rps_as_dict.append(rp_as_dict)
            print (i)
      return rps_as_dict  #00Oa0000008272QEAQ

def Run_Exp_SF4_Cleanup():
      #report=analytic_sf.get_report('00Oa0000008272QEAQ',all(true))
      try:
          #report=analytic_sf.get_report('00Oa0000008272QEAQ', filters=None, details=True)
          #parser = salesforce_reporting.ReportParser(report)
          #dict=parser.records()
          list=sf.query("select ESI__SO_ID__r.ESI__SO_ID__c,ESI__PRODUCT_LINE__c,ESI__SO_LINE_NO__c,ESI__SO_LINE_STATUS__c,ESI__SO_ID__r.ESI__SO_STATUS__c,ESI__REV_SHIP_DATE__c,ESI__LAST_SHIP_NO__c,ESI__REV_ORDER_QTY__c,ESI__AMOUNT__c  from ESI__Sales_Order_Detail__c where ESI__SO_ID__r.ESI__ORDER_DATE__c>2015-06-01 ")
          dict=list["records"]
          rps_as_dict=[]
          #dbmodels.EXPUPDATE.FillSFDC7()
          all=''
          i=0
          rps_as_dict=[]
          for record in  dict:
                i=i+1
                sub= record['ESI__SO_ID__r']
                rp_as_dict = {
                       'Sales Order Number' :  sub['ESI__SO_ID__c'],
                       'Prod Line' :  record['ESI__PRODUCT_LINE__c'],
                       'Sales Order Line' :  record['ESI__SO_LINE_NO__c'],
                       'Line St' :  record['ESI__SO_LINE_STATUS__c'],
                       'Status' :  sub['ESI__SO_STATUS__c'],
                       'Rev Ship' :  record['ESI__REV_SHIP_DATE__c'],
                       'Last Shipment' :  record['ESI__LAST_SHIP_NO__c'],
                       'Rev Ord Qty' :  record['ESI__REV_ORDER_QTY__c'],
                       'Last Modified Date' :  "NA",
                       'Part ID' :  "NA",
                       'Description' :  "NA",
                       'Created Date' :  "NA",
                       'Platform' :  "NA",
                       'Base Price' :  "NA",
                       'Amount' :  record['ESI__AMOUNT__c']
                       #'Opportunity Owner' :  record[15],
                }
                print (i)
                #dbmodels.EXPUPDATE.FillSFDC7(rp_as_dict)
                rps_as_dict.append(rp_as_dict)

          return rps_as_dict  #


      except Exception as e:
        return e






"""
@api {get} /api/sfanalytic/forecast  forecast piplene all 75 report
@apiSampleRequest http://192.168.3.146:8090/api/sfanalytic/forecast
@apiName Gereport
@apiGroup SFDC ANALYTIC
@apiVersion 0.1.0


@apiSuccess {String} AccountName
@apiSuccess {String} AccountOwner
@apiSuccess {String} Amount
@apiSuccess {Date} CloseDate
@apiSuccess {Date} CreatedDate
@apiSuccess {String} ExpandableCustomerID
@apiSuccess {String} ListPrice
@apiSuccess {String} OpportunityID
@apiSuccess {String} Probability%
@apiSuccess {String} ProductName
@apiSuccess {String} Quantity
@apiSuccess {String} SalesPrice
@apiSuccess {String} Stage
@apiSuccess {String} TotalPrice

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
 {
  "ForecastPipeline": [
    {
      "Account Name": "Metropolitan Police",
      "Account Owner": "Elaine Julian",
      "Amount": "$4,395,000.00",
      "Close Date": "3/4/2016",
      "Created Date": "3/1/2016",
      "Expandable Customer ID": "-",
      "List Price": "$22,500.00",
      "Opportunity ID": "006a000001HjncD",
      "Opportunity Name": "MetPolice-RHID-NGMSE",
      "Probability (%)": "75%",
      "Product Name": "RapidHIT ID NGM SElect Express 150 Sample Kit",
      "Quantity": "6",
      "Sales Price": "$8,250.00",
      "Stage": "Stage 3 - Negotiating",
      "Total Price": "$49,500.00"
    },

  }
}
"""











"""
@api {get} /api/sfdc/report Reports list
 @apiSampleRequest http://192.168.3.146:8090/api/sfdc/report
@apiName Gereport
@apiGroup SFDC
@apiVersion 0.1.0


@apiSuccess {String} DeveloperName    report DeveloperName
@apiSuccess {Number} ID  Oppotinity  ID DeveloperName
@apiSuccess {DATE} Name   Oppotinity  Name DeveloperName

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
 {
  "Report": [
    {
      "DeveloperName": "All_Activities_by_Rep",
      "Id": "00Oa0000008TQU9EAO",
      "Name": "All Activities by Rep"
    },
    {
      "DeveloperName": "of_open_opportunuities",
      "Id": "00Oa0000008TTKtEAO",
      "Name": "# of open opportunuities"
    },
    {
      "DeveloperName": "Accounts_for_Price_Book_Update",
      "Id": "00Oa0000008nemGEAQ",
      "Name": "Accounts for Price Book Update"
    },
    {
      "DeveloperName": "Accounts_for_TAM_Updates",
      "Id": "00Oa0000008neueEAA",
      "Name": "Accounts for TAM Updates"
    },

  }
}
"""





"""
@api {get} /api/sfdc/opportunity  Opportunities
@apiSampleRequest http://192.168.3.146:8090/api/sfdc/opportunity
@apiName opportunity
@apiGroup SFDC
@apiVersion 0.1.0


@apiSuccess {String} AccountId    SFDC Account ID
@apiSuccess {Number} Amount  Oppotinity amount
@apiSuccess {DATE} CloseDate   Oppotinity CloseDate
@apiSuccess {String} CreatedById   SFDC user
@apiSuccess {Number} FiscalYear   Oppotinity year.
@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "Oppurtinity": [
    {
      "AccountId": "001a000001dGcAgAAK",
      "Amount": null,
      "CloseDate": "2015-06-30",
      "CreatedById": "005a000000BfbjOAAR",
      "FiscalYear": 2015
    },
    {
      "AccountId": "001a000001HeDb6AAF",
      "Amount": 25000.0,
      "CloseDate": "2014-06-30",
      "CreatedById": "005a0000007uu5aAAA",
      "FiscalYear": 2014
    },
    {
      "AccountId": "001a000001JE5K6AAL",
      "Amount": 347500.0,
      "CloseDate": "2016-06-15",
      "CreatedById": "005a000000BiZyIAAV",
      "FiscalYear": 2016
    },
    {
      "AccountId": "001a000001ACPkcAAH",
      "Amount": 30000.0,
      "CloseDate": "2014-09-30",
      "CreatedById": "00530000006OyS9AAK",
      "FiscalYear": 2014
    },
  }
}
"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

@api {get} /api/sfdc/pricebook  Pricebooks
@apiSampleRequest http://192.168.3.146:8090/api/sfdc/pricebook
@apiName Pricebook
@apiGroup SFDC
@apiVersion 0.1.0



@apiSuccess {String} Name    SFDC Price Book Name
@apiSuccess {String} Description  Price Book Description
@apiSuccess {Boolean} IsActive  IsActive
@apiSuccess {Boolean} IsStandard   IsStandard
@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "Pricebook": [
    {
      "Description": "Expandable ERP Price List Integration Managed Price Book",
      "IsActive": true,
      "IsStandard": false,
      "Name": "GSS - GSS Price List (Qty 1)"
    },
    {
      "Description": "Expandable ERP Price List Integration Managed Price Book",
      "IsActive": true,
      "IsStandard": false,
      "Name": "ILB - IL Biosystems PL (Qty 1)"
    },
    {
      "Description": "Expandable ERP Price List Integration Managed Price Book",
      "IsActive": true,
      "IsStandard": false,
      "Name": "KFS - Key Forensic PL (Qty 1)"
    },
    {
      "Description": "Expandable ERP Price List Integration Managed Price Book",
      "IsActive": true,
      "IsStandard": false,
      "Name": "ODA - Orange Cty PL (Qty 1)"
    },
    {
      "Description": "Expandable ERP Price List Integration Managed Price Book",
      "IsActive": true,
      "IsStandard": false,
      "Name": "RYT - Ryan Price List (Qty 1)"
    },
    {
      "Description": "Expandable ERP Price List Integration Managed Price Book",
      "IsActive": true,
      "IsStandard": false,
      "Name": "TRI - Triolab Price List (Qty 1)"
    },
    {
      "Description": "Expandable ERP Price List Integration Managed Price Book",
      "IsActive": true,
      "IsStandard": false,
      "Name": "SRP - Sci Resources PL (Qty 1)"
    }
  }
}



"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""

@api {get} /api/sfdc/product  Products
@apiSampleRequest http://192.168.3.146:8090/api/sfdc/product
@apiName Products
@apiGroup SFDC
@apiVersion 0.1.0




@apiSuccess {String} Name    SFDC Product Name
@apiSuccess {String} Description  Product Description
@apiSuccess {Boolean} IsActive  IsActive
@apiSuccess {String} Family   Family
@apiSuccess {String} ProductCode   ProductCode
@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "Product": [
    {
      "Description": null,
      "Family": "RIDA - RapidHIT ID Accessories",
      "IsActive": true,
      "Name": "RH ID Command Cntr License, per year, per instrument",
      "ProductCode": "500036"
    },
    {
      "Description": null,
      "Family": "SUPP - Support",
      "IsActive": true,
      "Name": "International, Zone 1 Travel Charge",
      "ProductCode": "200026"
    },
    {
      "Description": null,
      "Family": "SUPP - Support",
      "IsActive": true,
      "Name": "Additional Day Travel Charge",
      "ProductCode": "200028"
    },
    {
      "Description": null,
      "Family": "SUPP - Support",
      "IsActive": true,
      "Name": "US, Zone 2 Travel Charge",
      "ProductCode": "200024"
    },
    {
      "Description": null,
      "Family": "SUPP - Support",
      "IsActive": true,
      "Name": "US, Zone 3 Travel Charge",
      "ProductCode": "200025"
    },
    {
      "Description": null,
      "Family": "RHIT - RapidHit 200 Instruments",
      "IsActive": true,
      "Name": "Kinship Analysis Module requires v2.0 or higher",
      "ProductCode": "500032"
    },
    {
      "Description": null,
      "Family": "SUPP - Support",
      "IsActive": true,
      "Name": "Fluidic Pogo Plunger, RapidHIT (CC) (Spare)",
      "ProductCode": "P040474"
    }
  }
}

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
@api {get} /api/sfdc/user  Users
@apiSampleRequest http://192.168.3.146:8090/api/sfdc/user
@apiName Users
@apiGroup SFDC
@apiVersion 0.1.0


@apiSuccess {String} Alias    SFDC User Alias
@apiSuccess {String} City     City
@apiSuccess {Boolean} CompanyName  CompanyName
@apiSuccess {String} Country   Country
@apiSuccess {String} Department   Department
@apiSuccess {String} Email   Email

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "User": [
    {
      "Alias": "JGall",
      "City": "San Francisco",
      "CompanyName": "IntegenX",
      "ContactId": null,
      "Country": "US",
      "Department": "Customer Service",
      "Email": "joannag@integenx.com"
    },
    {
      "Alias": "ladmi",
      "City": null,
      "CompanyName": null,
      "ContactId": null,
      "Country": null,
      "Department": null,
      "Email": "integenx@lexnetcrm.com"
    },
    {
      "Alias": "hgold",
      "City": "Pleasanton",
      "CompanyName": "IntegenX",
      "ContactId": null,
      "Country": "USA",
      "Department": "Commercial Operations",
      "Email": "howardg@integenx.com"
    },
    {
      "Alias": "bennyw",
      "City": "Pleasanton",
      "CompanyName": "IntegenX",
      "ContactId": null,
      "Country": "USA",
      "Department": "Field Service",
      "Email": "bennyw@integenx.com"
    },
    {
      "Alias": "j_gub",
      "City": "Pleasanton",
      "CompanyName": "IntegenX",
      "ContactId": null,
      "Country": "USA",
      "Department": "Customer Service",
      "Email": "jillg@integenx.com"
    },
    {
      "Alias": "larryk",
      "City": "Pleasanton",
      "CompanyName": "IntegenX",
      "ContactId": null,
      "Country": "USA",
      "Department": "Sales",
      "Email": "larryk@integenx.com"
    },
    {
      "Alias": "RGuar",
      "City": "Medina",
      "CompanyName": "IntegenX",
      "ContactId": null,
      "Country": "USA",
      "Department": null,
      "Email": "rossg@integenx.com"
    }
  }
}
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

@api {get} /api/sfdc/account  Accounts
@apiSampleRequest http://192.168.3.146:8090/api/sfdc/account
@apiName Accounts
@apiGroup SFDC
@apiVersion 0.1.0




@apiSuccess {String} AccountNumber    SFDC AccountNumber
@apiSuccess {String} Description     Description
@apiSuccess {String} Industry  Industry
@apiSuccess {String} BillingCity   BillingCountry
@apiSuccess {String} BillingCountry   Department
@apiSuccess {String} LastActivityDate   LastActivityDate
@apiSuccess {String} Name   Name
@apiSuccess {String} OwnerId   OwnerId
@apiSuccess {String} Phone   Phone
@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "Account": [
    {
      "AccountNumber": null,
      "BillingCity": "Seattle",
      "BillingCountry": "USA",
      "Description": null,
      "Industry": "Forensics",
      "LastActivityDate": "2015-09-01",
      "Name": "Washington State Patrol Crime Lab",
      "OwnerId": "005a000000BfCdVAAV",
      "Phone": "(206) 262-6020"
    },
    {
      "AccountNumber": "ADP001",
      "BillingCity": "Phoenix",
      "BillingCountry": "USA",
      "Description": null,
      "Industry": "Forensics",
      "LastActivityDate": "2016-02-04",
      "Name": "Arizona Department of Public Safety",
      "OwnerId": "005a000000BfCdVAAV",
      "Phone": "(602) 223-2494"
    },
    {
      "AccountNumber": null,
      "BillingCity": "Denver",
      "BillingCountry": "USA",
      "Description": null,
      "Industry": "Forensics",
      "LastActivityDate": "2015-09-01",
      "Name": "Denver Police Department Crime Lab",
      "OwnerId": "005a000000BfCdVAAV",
      "Phone": "(720) 337-2010"
    },
    {
      "AccountNumber": null,
      "BillingCity": "Essex",
      "BillingCountry": "United Kingdom",
      "Description": null,
      "Industry": null,
      "LastActivityDate": null,
      "Name": "Genetic Research Instrumentation, LTD UK",
      "OwnerId": "005a000000BiZyIAAV",
      "Phone": "[44]01376332900"
    },
    {
      "AccountNumber": "UMS001",
      "BillingCity": "Pleasanton",
      "BillingCountry": "USA",
      "Description": null,
      "Industry": "Biotechnology Company",
      "LastActivityDate": "2014-10-17",
      "Name": "User Meetings/Shows",
      "OwnerId": "005a0000007vmNGAAY",
      "Phone": "(858) 202-4502"
    },
    {
      "AccountNumber": "ITS001",
      "BillingCity": "Johnstown",
      "BillingCountry": "USA",
      "Description": null,
      "Industry": "Distributor",
      "LastActivityDate": "2015-09-01",
      "Name": "ITSI-Biosciences",
      "OwnerId": "005a000000BfCdVAAV",
      "Phone": "(814) 262-7331"  }
    }
}
}



"""
