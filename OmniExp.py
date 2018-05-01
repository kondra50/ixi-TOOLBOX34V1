import base64
import os
import smtplib
import requests,json,os,time
import datetime
from xml.etree import ElementTree as ET
from email.mime.application import MIMEApplication
from email.mime.multipart import  MIMEMultipart

class transformer:

    url='http://192.168.3.146:9070/api'
    #log_dict=[]
    password=base64.b64decode(b'SU5UZ3NtNyE3')
    def __init__(self,path):
        self.path=path
        self.AuthToken=self._Get_Tocken()
        tmp=str(path).split("\\")
        self.FileName=tmp[len(tmp)-1]
        self.log_dict=[]
        self.Error=False
    def _Log_Result(self,Error,Table,Action,Response,Key):
         self.Error=Error
         #key="PART_ID ="+ Final_Value['PART_ID']
         #self._Log_Fail('Update Part',str(Response.status_code),str(Response.text))
         if Error: Action= Action +"ERROR :"+Response.text
         self.log_dict.append({"KEY":Key,"ACTION":Action,"TABLE":Table,"FILE":str(self.FileName)})
    def _Get_Tocken(self):
        url='http://192.168.3.146:9070/api/Security/Login'
        password=base64.b64decode(b'SU5UZ3NtNyE3')
        mypass=password.decode("utf-8")
        headers = {'Content-type': 'application/json','Accept':'application/vnd.expandable.api.v930+json'}
        data_json = json.dumps({"DataSource": "ESI","UserName":"MNAFISI","Password":mypass})
        response = requests.post(url, data=data_json,headers=headers)
        res=response.headers
        #print(res['AuthToken'])
        return  res['AuthToken']
        #if (response.status_code!= 200):return  response.text()
    def _Clean_List(self,List):
         values = {k: v for k, v in List.items() if v != '##'}
         New_values = {k: str(v).replace('"','') for k, v in values.items()}
         Final_Value = {k: str(v).replace('\n','') for k, v in New_values.items()}
         return Final_Value
    def _Send_Email(self,Response):
        try:

             msg = MIMEMultipart()
             msg['Subject'] = 'ECUDU Activity Report'
             msg['From'] = "mehrdadn@integenx.com"
             msg['To'] = "mehrdadn@integenx.com"
             img1 = MIMEApplication(Response.content, 'pdf')
             msg.attach(img1)
             s = smtplib.SMTP('IXI-EXCH.microchipbiotech.com')
             s.send_message(msg)
             s.quit()
        except Exception as e:
               print(e)
    def _Log_Fail(self,Stage,Code,Desc):
        print('fail happened as'+Stage +'Error code: '+Code+'Error Desc: '+Desc)
    def _Part_Exist(self,PART_ID):
        data_json = json.dumps({"PART_ID": PART_ID})
        response = requests.post(self.url+'/Part/Query', data=data_json, headers=self.headers)
        if (response.status_code==403 or response.status_code==401):
            self.AuthToken=self._Get_Tocken
            self.headers = {'AuthToken': self.AuthToken,'Content-type': 'application/json'}
            response = requests.post(self.url, data=data_json, headers=self.headers)
        res=response.text
        if str(res).strip()=='[]': return False
        if str(res).strip()!='[]': return True
        return True
    def _BOM_Exist(self,ASSEMBLY_ID,COMPONENT_ID,DWG_ITEM_CODE):
        data_json = json.dumps({"ASSEMBLY_ID": ASSEMBLY_ID,"COMPONENT_ID":COMPONENT_ID,"DWG_ITEM_CODE":DWG_ITEM_CODE})
        response = requests.post(self.url+'/BillOfMaterial/Query', data=data_json, headers=self.headers)
        if (response.status_code==403 or response.status_code==401):
            self.AuthToken=self._Get_Tocken
            self.headers = {'AuthToken': self.AuthToken,'Content-type': 'application/json'}
            response = requests.post(self.url, data=data_json, headers=self.headers)
        res=response.text
        if str(res).strip()=='[]': return False
        if str(res).strip()!='[]': return True
        return True
    def _VP_Exist(self,PART_ID,VENDOR_ID,VENDOR_PART_ID):
        data_json = json.dumps({"PART_ID": PART_ID,"VENDOR_ID":VENDOR_ID,"VENDOR_PART_ID":VENDOR_PART_ID})
        response = requests.post(self.url+'/VendorPart/Query', data=data_json, headers=self.headers)
        if (response.status_code==403 or response.status_code==401):
            self.AuthToken=self._Get_Tocken
            self.headers = {'AuthToken': self.AuthToken,'Content-type': 'application/json'}
            response = requests.post(self.url, data=data_json, headers=self.headers)
        res=response.text
        if str(res).strip()=='[]': return False
        if str(res).strip()!='[]': return True
        return True


    def ReadFile(self):

        Part_Col=['PART_ID' ,'PART_TYPE','PART_DESC','PART_UM','DWG_REV','DWG_SIZE','ECN','ECN_EFF_DATE','PENDING_ECN','PREF_VENDOR','COMM_CODE','USER_1','USER_2','USER_3','USER_4','USER_5','USER_6','USER_7','USER_8','WEIGHT','VOLUME','SUBST_PART',
       'PRODUCT_LINE','PART_STATUS','PART_CLASS','STD_MTL_CST_CUM','PLAN_LEAD_TIME','BUYER_ID','BUYER_ID','USER_9','USER_10','USER_11','USER_12','USER_13','USER_14','USER_15','USER_16','ROHS_COMP_ST',
       'ROHS_COMP_DATE','ROHS_COMP_COMM','ROHS_PROC_ST','ROHS_PROC_DATE','ROHS_PROC_COMM','ROHS_DOC_ST','ROHS_DOC_DATE','ROHS_DOC_COMM','WEEE_RECY_ST','WEEE_RECY_DATE','WEEE_RECY_COMM','PLANNER_ID','BUY_UM,BUY_CONV',
       'SN_REQD','LOT_CONTROL','STOCK_DEC','BUY_DEC','ABC_CODE','DEF_STORES_CODE','SN_REQD_INV','SHELF_LIFE']
        Vp_Col=['PART_ID','MFG_NAME','MFG_ID','VENDOR_ID','VENDOR_PART_ID','BUY_STATUS','POFVP_USER_1','POFVP_USER_2','POFVP_USER_3','POFVP_USER_4','POFVP_USER_5','POFVP_USER_6',
        'POFVP_USER_7','POFVP_USER_8','POFVP_USER_9','POFVP_USER_10','POFVP_USER_11','POFVP_USER_12','POFVP_USER_13','POFVP_USER_14','ROHS_COMP_ST','ROHS_COMP_DATE','ROHS_COMP_COMM','ROHS_PROC_ST','ROHS_PROC_DATE',
        'ROHS_PROC_COMM','ROHS_DOC_ST','ROHS_PROC_DATE','ROHS_PROC_COMM','WEEE_RECY_ST','WEEE_RECY_DATE','WEEE_RECY_COMM','VENDR_LEAD_TIME','LOT_SIZE','PO_DESC','BUY_UM','BUY_CONV','BUY_DEC','QC_FLAG','DEF_STORES_CODE','QUOTE_UNIT_PRIC',
        'QUOTE_QTY','PRICE_CHG','CONTRACT']
        BOM_Col=['ASSEMBLY_ID' ,'COMPONENT_ID','DWG_ITEM_CODE','REQUIRED_QTY','START_DATE','END_DATE','BILLS_TYPE','REMARK','REF_DESIGNATOR']
        VM_Colt=['VENDOR_ID','VENDOR_NAME','ADDRESS_1','ADDRESS_2','CITY','STATE','ZIP_CODE','COUNTRY','PO_CONTACT','PO_PHONE_NO','FAX_NO','VENDOR_STATUS']

        Part_List=[]
        VP_List=[]
        BOM_LIST=[]

        with open(self.path) as f:
            for l in f:
                 line=str(l).replace('##', '"##"');
                 #print(line)
                 if (str(line).strip()=='# ICFPM Data'): linedata='PART'
                 if (str(line).strip()=='# POFVP_3 Data'): linedata='VPART'
                 if (str(line).strip()=='# PDFBM Data'): linedata='BOM'

                 if ((linedata=='PART') and (str(line).strip()!='# ICFPM Data') ):
                    words = line.split('","')
                    r=dict(zip(Part_Col,words))
                    Part_List.append(r)

                 if ((linedata=='VPART') and (str(line).strip()!='# POFVP_3 Data') ):
                    words = line.split('","')
                    r=dict(zip(Vp_Col,words))
                    VP_List.append(r)

                 if ((linedata=='BOM') and (str(line).strip()!='# PDFBM Data') ):
                    words = line.split('","')
                    r=dict(zip(BOM_Col,words))
                    BOM_LIST.append(r)

        return (Part_List,VP_List,BOM_LIST )
    def Call_Expandable_API(self,Part_List,Vendor_Part_List,BOM_List):
        ICFPM_log_dict=[]
        BOM_log_dict=[]
        VP_log_dict=[]
        key=''
        #log_dict=[]

        self.headers = {'AuthToken': self.AuthToken,'Content-type': 'application/json'}
        s = requests.Session()
        s.headers=self.headers


        try:
            for item in Part_List:
                Final_Value=self._Clean_List(item)
                key="PART_ID ="+ Final_Value['PART_ID']
                data_json = json.dumps(Final_Value)
                if  self._Part_Exist(Final_Value['PART_ID']):
                    response = s.post(self.url+'/Part/Update',data=data_json)
                    if (response.status_code!=200): self._Log_Result(True,"ICFPM","Update",response,key)
                    else:self._Log_Result(False,"ICFPM","Updated",response,key)
                else: #New
                    response = s.post(self.url+'/Part/Create',data=data_json)
                    if (response.status_code!=200): self._Log_Result(True,"ICFPM","Insert",response,key)
                    else: self._Log_Result(False,"ICFPM","Inserted",response,key)
        except Exception as e:
            print(e)



        try:
            for item in BOM_List:
                Final_Value=self._Clean_List(item)
                DWG_ITEM_CODE= '%04d' % int(Final_Value['DWG_ITEM_CODE'])
                Final_Value['DWG_ITEM_CODE']=DWG_ITEM_CODE
                key="ASM ="+ Final_Value['ASSEMBLY_ID']+" ,COMP ="+ Final_Value['COMPONENT_ID']+" ,DWG ="+ Final_Value['DWG_ITEM_CODE']
                data_json = json.dumps(Final_Value)
                if  self._BOM_Exist( Final_Value['ASSEMBLY_ID'],Final_Value['COMPONENT_ID'],Final_Value['DWG_ITEM_CODE']):
                    response = s.post(self.url+'/BillOfMaterial/Update',data=data_json)
                    if (response.status_code!=200):self._Log_Result(True,"BOFOM","Update",response,key)
                    else: self._Log_Result(False,"BOFOM","Updated",response,key)
                else: #New
                    response = s.post(self.url+'/BillOfMaterial/Create',data=data_json)
                    if (response.status_code!=200): self._Log_Result(True,"BOFOM","Insert",response,key)
                    else: self._Log_Result(False,"BOFOM","Inserted",response,key)
        except Exception as e:
            print(e)



        try:
            for item in Vendor_Part_List:
                Final_Value=self._Clean_List(item)
                key="PART="+ Final_Value['PART_ID']+" ,VEN="+ Final_Value['VENDOR_ID']+" ,VEN_P="+ Final_Value['VENDOR_PART_ID']
                data_json = json.dumps(Final_Value)
                if  self._VP_Exist( Final_Value['PART_ID'],Final_Value['VENDOR_ID'],Final_Value['VENDOR_PART_ID']):
                    response = s.post(self.url+'/VendorPart/Update',data=data_json)
                    if (response.status_code!=200): self._Log_Result(True,"POFVP","Update",response,key)
                    else: self._Log_Result(False,"POFVP","Updated",response,key)
                else: #New
                    response = s.post(self.url+'/VendorPart/Create',data=data_json)
                    if (response.status_code!=200):self._Log_Result(True,"POFVP","Insert",response,key)
                    else: self._Log_Result(False,"POFVP","Inserted",response,key)
            #print(self.log_dict)
        except Exception as e:
            print(e)

        return self.log_dict,self.Error
    def Prepare_Report(self,FinalDict):

        with open('result.json', 'w') as fp:
            json.dump(FinalDict, fp)

        try:
            # with open('result.json') as fh:
            #
            #     mydata = fh.read()
            response = requests.put('http://192.168.3.146:8051/jasperserver/rest_v2/resources/JSON_EXAMPLE/JSON_ECUDU_LOG',
                            data=json.dumps(FinalDict),
                            headers={'content-type':'application/json','Authorization':'Basic amFzcGVyYWRtaW46amFzcGVyYWRtaW4='}
                             )
        except Exception as e:
            print(e)
            exit()
    def MovFile(self,filename,Haserror,Path):
        plmfile=Path+'\\'+filename
        if (Haserror == False): newfile=Path+'\\PROCESSED\\'+filename
        if (Haserror == True):  newfile=Path+'\\ERROR\\'+filename
        try:
            os.remove(newfile)
        except Exception as e:
            pass
        try:
            os.rename(plmfile, newfile)
        except Exception as e:
            print(e)
    def Send_ECUDU_Jasperreport(self):

        try:
            s = requests.Session()
            s.auth = ('jasperadmin', 'jasperadmin')
            s.headers={'content-type':'application/text'}
            bas_ULR='http://192.168.3.146:8051/jasperserver/rest/'
            response = s.get(bas_ULR+'resource/reports/ECUDU')
            #Get Report Decriptive
            ECUDU_DESCRIPTIV=response.text
            #Run report and get UUID
            response = s.put(bas_ULR+'report',data=ECUDU_DESCRIPTIV)
            tree = ET.fromstring(response.content)
            UUID = tree.findall('uuid')[0].text
            #Downliod the report
            url=bas_ULR+'report/'+UUID+'?file=ecudureport'
            response = s.get(bas_ULR+'report/'+UUID+'?file=report')
            # Send Email
            self._Send_Email(response)
        except Exception as e:
            print(e)
            exit()







