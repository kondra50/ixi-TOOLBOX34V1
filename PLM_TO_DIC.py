import base64
import os
import requests,json,os,time
global AuthToken
import datetime
url='http://192.168.3.146:9070/api'
Main_Path='C:\Python34\ixi_TBOX34\PLM_FILES'
log_dict=[]
#log_dict["TRANSACTION"]={}
#log_dict.append({"Transaction":{}})
FileName=''

def Get_Tocken():
    url='http://192.168.3.146:9070/api/Security/Login'
    password=base64.b64decode(b'SU5UZ3NtNyE3')
    mypass=password.decode("utf-8")
    headers = {'Content-type': 'application/json','Accept':'application/vnd.expandable.api.v930+json'}
    data_json = json.dumps({"DataSource": "ESI","UserName":"MNAFISI","Password":mypass})
    response = requests.post(url, data=data_json,headers=headers)
    res=response.headers
    print(res['AuthToken'])
    return  res['AuthToken']
def ReadFile(path):

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

    with open(path) as f:
        for l in f:
             line=str(l).replace('##', '"##"');
             print(line)
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
def Log_Fail(Stage,Code,Desc):
    print('fail happened as'+Stage +'Error code: '+Code+'Error Desc: '+Desc)
def Part_Exist(PART_ID):
    data_json = json.dumps({"PART_ID": PART_ID})
    #headers = {'AuthToken': AuthToken,'Content-type': 'application/json'}
    response = requests.post(url+'/Part/Query', data=data_json, headers=headers)
    if (response.status_code==403 or response.status_code==401):
        AuthToken=Get_Tocken
        response = requests.post(url, data=data_json, headers=headers)
    res=response.text
    if str(res).strip()=='[]': return False
    if str(res).strip()!='[]': return True
    return True
def BOM_Exist(ASSEMBLY_ID,COMPONENT_ID,DWG_ITEM_CODE):
    data_json = json.dumps({"ASSEMBLY_ID": ASSEMBLY_ID,"COMPONENT_ID":COMPONENT_ID,"DWG_ITEM_CODE":DWG_ITEM_CODE})
    #headers = {'AuthToken': AuthToken,'Content-type': 'application/json'}
    response = requests.post(url+'/BillOfMaterial/Query', data=data_json, headers=headers)
    if (response.status_code==403 or response.status_code==401):
        AuthToken=Get_Tocken
        response = requests.post(url, data=data_json, headers=headers)
    res=response.text
    if str(res).strip()=='[]': return False
    if str(res).strip()!='[]': return True
    return True
def VP_Exist(PART_ID,VENDOR_ID,VENDOR_PART_ID):
    data_json = json.dumps({"PART_ID": PART_ID,"VENDOR_ID":VENDOR_ID,"VENDOR_PART_ID":VENDOR_PART_ID})
    #headers = {'AuthToken': AuthToken,'Content-type': 'application/json'}
    response = requests.post(url+'/VendorPart/Query', data=data_json, headers=headers)
    if (response.status_code==403 or response.status_code==401):
        AuthToken=Get_Tocken
        response = requests.post(url, data=data_json, headers=headers)
    res=response.text
    if str(res).strip()=='[]': return False
    if str(res).strip()!='[]': return True
    return True
def Call_Expandable_API(Part_List,Vendor_Part_List,BOM_List):
    ICFPM_log_dict=[]
    BOM_log_dict=[]
    VP_log_dict=[]
    key=''
    #FileName="test.plm"
    output_list=[]
    Error=False
    s = requests.Session()
    s.headers=headers
    try:
        for item in Part_List:
            values = {k: v for k, v in item.items() if v != '##'}
            New_values = {k: str(v).replace('"','') for k, v in values.items()}
            Final_Value = {k: str(v).replace('\n','') for k, v in New_values.items()}
            data_json = json.dumps(Final_Value)
            if  Part_Exist(Final_Value['PART_ID']):
                response = s.post(url+'/Part/Update',data=data_json)
                if (response.status_code!=200):
                    Error=True
                    key="PART_ID ="+ Final_Value['PART_ID']
                    Log_Fail('Update Part',str(response.status_code),str(response.text))
                    log_dict.append({"KEY":key,"ACTION":"UPDATE ERROR: "+response.text,"TABLE":"ICFPM","FILE":str(FileName)})
                else:
                    key="PART_ID ="+ Final_Value['PART_ID']
                    log_dict.append({"KEY":key,"ACTION":"UPDATE","TABLE":"ICFPM","FILE":str(FileName)})

            else:
                print('-----------------------------------------------NEW------------------------------------------------------------')
                response = s.post(url+'/Part/Create',data=data_json)
                if (response.status_code!=200):
                    Error=True
                    key="PART_ID ="+ Final_Value['PART_ID']
                    Log_Fail('Update Part',str(response.status_code),str(response.text))
                    log_dict.append({"KEY":key,"ACTION":"INSERT ERROR: "+response.text,"TABLE":"ICFPM","FILE":str(FileName)})
                else:
                    key="PART_ID ="+ Final_Value['PART_ID']
                    log_dict.append({"KEY":key,"ACTION":"INSERTED","TABLE":"ICFPM","FILE":str(FileName)})
                #log_dict.append({"Summary":{"TableName":"ICFPM","details":ICFPM_log_dict}})
    except Exception as e:
        print(e)


    # with open('result.json', 'w') as fp:
    #     json.dump(log_dict, fp)
    #
    # exit()

    try:
        for item in BOM_List:
            values = {k: v for k, v in item.items() if v != '##'}
            New_values = {k: str(v).replace('"','') for k, v in values.items()}
            Final_Value = {k: str(v).replace('\n','') for k, v in New_values.items()}
            DWG_ITEM_CODE= '%04d' % int(Final_Value['DWG_ITEM_CODE'])
            Final_Value['DWG_ITEM_CODE']=DWG_ITEM_CODE
            data_json = json.dumps(Final_Value)
            if  BOM_Exist( Final_Value['ASSEMBLY_ID'],Final_Value['COMPONENT_ID'],Final_Value['DWG_ITEM_CODE']):
                response = s.post(url+'/BillOfMaterial/Update',data=data_json)
                if (response.status_code!=200):
                    Error=True
                    Log_Fail(' Update BOM ',str(response.status_code),str(response.text))
                    key="ASSEMBLY_ID ="+ Final_Value['ASSEMBLY_ID']+" ,COMPONENT_ID ="+ Final_Value['COMPONENT_ID']+" ,DWG_ITEM_CODE ="+ Final_Value['DWG_ITEM_CODE']
                    log_dict.append({"KEY":key,"ACTION":"UPDATE ERROR: "+response.text,"TABLE":"BOFOM","FILE":str(FileName)})
                else:
                    key="ASSEMBLY_ID ="+ Final_Value['ASSEMBLY_ID']+" ,COMPONENT_ID ="+ Final_Value['COMPONENT_ID']+" ,DWG_ITEM_CODE ="+ Final_Value['DWG_ITEM_CODE']
                    log_dict.append({"KEY":key,"ACTION":"UPDATED","TABLE":"BOFOM","FILE":str(FileName)})



            else:
                print('-----------------------------------------------NEW------------------------------------------------------------')
                response = s.post(url+'/BillOfMaterial/Create',data=data_json)
                if (response.status_code!=200):
                    Error=True
                    Log_Fail(' INSERT BOM ',str(response.status_code),str(response.text))
                    key="ASSEMBLY_ID ="+ Final_Value['ASSEMBLY_ID']+" ,COMPONENT_ID ="+ Final_Value['COMPONENT_ID']+" ,DWG_ITEM_CODE ="+ Final_Value['DWG_ITEM_CODE']
                    log_dict.append({"KEY":key,"ACTION":"INSERT ERROR: "+response.text,"TABLE":"BOFOM","FILE":str(FileName)})
                else:
                    key="ASSEMBLY_ID ="+ Final_Value['ASSEMBLY_ID']+" ,COMPONENT_ID ="+ Final_Value['COMPONENT_ID']+" ,DWG_ITEM_CODE ="+ Final_Value['DWG_ITEM_CODE']
                    log_dict.append({"KEY":key,"ACTION":"INSERTED","TABLE":"BOFOM","FILE":str(FileName)})
                #log_dict.append({"Summary":{"TableName":"PDFBM","details":BOM_log_dict}})

    except Exception as e:
        print(e)



    try:
        for item in Vendor_Part_List:
            values = {k: v for k, v in item.items() if v != '##'}
            New_values = {k: str(v).replace('"','') for k, v in values.items()}
            Final_Value = {k: str(v).replace('\n','') for k, v in New_values.items()}
            data_json = json.dumps(Final_Value)
            if  VP_Exist( Final_Value['PART_ID'],Final_Value['VENDOR_ID'],Final_Value['VENDOR_PART_ID']):

                response = s.post(url+'/VendorPart/Update',data=data_json)

                if (response.status_code!=200):
                    Error=True
                    Log_Fail(' Update VP ',str(response.status_code),str(response.text))
                    key="PART_ID ="+ Final_Value['PART_ID']+" ,VENDOR_ID ="+ Final_Value['VENDOR_ID']+" ,VENDOR_PART_ID ="+ Final_Value['VENDOR_PART_ID']
                    log_dict.append({"KEY":key,"ACTION":"UPDATE ERROR: "+response.text,"TABLE":"POFVP","FILE":str(FileName)})
                else:
                    key="PART_ID ="+ Final_Value['PART_ID']+" ,VENDOR_ID ="+ Final_Value['VENDOR_ID']+" ,VENDOR_PART_ID ="+ Final_Value['VENDOR_PART_ID']
                    log_dict.append({"KEY":key,"ACTION":"UPDATED","TABLE":"POFVP","FILE":str(FileName)})
            else:
                print('-----------------------------------------------NEW------------------------------------------------------------')
                response = s.post(url+'/VendorPart/Create',data=data_json)

                if (response.status_code!=200):
                    Error=True
                    Log_Fail(' Update VP ',str(response.status_code),str(response.text))
                    key="PART_ID ="+ Final_Value['PART_ID']+" ,VENDOR_ID ="+ Final_Value['VENDOR_ID']+" ,VENDOR_PART_ID ="+ Final_Value['VENDOR_PART_ID']
                    log_dict.append({"KEY":key,"ACTION":"INSERT ERROR: "+response.text,"TABLE":"POFVP","FILE":str(FileName)})
                else:
                    key="PART_ID ="+ Final_Value['PART_ID']+" ,VENDOR_ID ="+ Final_Value['VENDOR_ID']+" ,VENDOR_PART_ID ="+ Final_Value['VENDOR_PART_ID']
                    log_dict.append({"KEY":key,"ACTION":"INSERTED","TABLE":"POFVP","FILE":str(FileName)})
        #log_dict.append({"Summary":{"TableName":"PDFVP","details":VP_log_dict}})
        print(log_dict)
    except Exception as e:
        print(e)

    return log_dict,Error
def Prepare_Report(self,FinalDict):

    with open('result.json', 'w') as fp:
        json.dump(FinalDict, fp)



    try:
        with open('result.json') as fh:

            mydata = fh.read()
            response = requests.put('http://192.168.3.146:8051/jasperserver/rest_v2/resources/JSON_EXAMPLE/JSON_ECUDU_LOG',
                        data=mydata,
                     # auth=('jasperadmin', 'jasperadmin'),
                     headers={'content-type':'application/json','Authorization':'Basic amFzcGVyYWRtaW46amFzcGVyYWRtaW4='}
                         )
    except Exception as e:
        print(e)
        exit()


try:
    AuthToken=Get_Tocken()
except Exception as e:
    print(e)
headers = {'AuthToken': AuthToken,'Content-type': 'application/json'}
linedata=""

def MovFile(filename,Haserror):
    global Main_Path
    plmfile=Main_Path+'\\'+filename
    if (Haserror == False): newfile=Main_Path+'\\PROCESSED\\'+filename
    if (Haserror == True):  newfile=Main_Path+'\\ERROR\\'+filename
    try:
        os.remove(newfile)
    except Exception as e:
        pass
    try:
        os.rename(plmfile, newfile)
    except Exception as e:
        print(e)


#res_list=[]
while (True):

    filenames = next(os.walk(Main_Path))
    plmfiles=[f for f in filenames[2]  if '.plm' in str(f)]
    for f in plmfiles:
        FileName=f
        plmfile=Main_Path+'\\'+f
        Part_List,Vendor_Part_List,BOM_List= ReadFile(plmfile)
        FinalDict,Haserror=Call_Expandable_API(Part_List,Vendor_Part_List,BOM_List)
        Prepare_Report(FinalDict)
        MovFile(f,Haserror)


#log_dict.append({"FileNAme":"2.plm"})
#log_dict.append({"Summary":{"FILENAME":"1123123.PLM","DATE":str(datetime.datetime.now())}})



print('Done!')




























# you may also want to remove whitespace characters like `\n` at the end of each line
#content = [x.strip() for x in content]
#print(content)
# PART_LIST=['PART_ID','MFG_NAME','MFG_ID','VENDOR_ID','VENDOR_PART_ID','BUY_STATUS','POFVP_USER_1','POFVP_USER_2','POFVP_USER_3','POFVP_USER_4','POFVP_USER_5',
#            'POFVP_USER_6','POFVP_USER_7','POFVP_USER_8','POFVP_USER_9','POFVP_USER_10','POFVP_USER_11','POFVP_USER_12','POFVP_USER_13','POFVP_USER_14','POFVP_USER_15','ROHS_COMP_DATE','ROHS_COMP_COMM',
#            'ROHS_PROC_ST','ROHS_PROC_DATE','ROHS_PROC_COMM','ROHS_DOC_ST','','','','','','','']
#       <ROHS_COMP_DATE>##</ROHS_COMP_DATE>
#       <ROHS_COMP_COMM>##</ROHS_COMP_COMM>
#       <ROHS_PROC_ST>##</ROHS_PROC_ST>
#       <ROHS_PROC_DATE>##</ROHS_PROC_DATE>
#       <ROHS_PROC_COMM>##</ROHS_PROC_COMM>
#       <ROHS_DOC_ST>##</ROHS_DOC_ST>
#       <ROHS_PROC_DATE>##</ROHS_PROC_DATE>
#       <ROHS_PROC_COMM>##</ROHS_PROC_COMM>
#       <WEEE_RECY_ST>##</WEEE_RECY_ST>
#       <WEEE_RECY_DATE>##</WEEE_RECY_DATE>
#       <WEEE_RECY_COMM>##</WEEE_RECY_COMM>
#       <VENDR_LEAD_TIME>##</VENDR_LEAD_TIME>
#       <LOT_SIZE>##</LOT_SIZE>
#       <PO_DESC>
#       </PO_DESC>
#     </vp>
