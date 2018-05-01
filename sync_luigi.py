import sqlite3
import os
import luigi
import time
from simple_salesforce import Salesforce
#from tinydb import TinyDB, where,Query
from datetime import datetime, timedelta
import requests
#db = TinyDB('db.json')
#CN = Query()
import salesforce_reporting
# import requests,json
# from flask import jsonify
# from SFDC import  dbmodels
attemts=['RHID','RHIT']


#db_path=os.path.abspath("\\\\IXI-APPSVR02\\RHID Sustaining Production\\ttproj.db")
#db_path2=os.path.abspath("\\\\IXI-APPSVR02\\RapidHIT Sustaining\\ttproj.db")

# while True:

class ixisync(luigi.Task):

    def requires(self):
         return []

    def output(self):
        return []
        #return luigi.LocalTarget("squares.txt")


    def run(self):


        sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
        print('NEW START.............................................................................................................')
        for attemt in attemts:
            # try:
            #     c.close();
            #     conn5.commit();
            #     conn5.close();
            #
            # except  Exception as e:
            #     print(e)
            # try:
            #     c.close();
            #     conn6.commit();
            #     conn6.close();
            # except  Exception as e:
            #     print(e)

            # if attemt=='RHID': db_path=os.path.abspath("\\\\IXI-APPSVR02\\RHID Sustaining Production\\ttproj.db")
            # if attemt=='RHIT': db_path=os.path.abspath("\\\\IXI-APPSVR02\\RapidHIT Sustaining\\ttproj.db")
            #while True:
                #time.sleep(60)
               # print("After 5 sec")

            date_S = datetime.now() - timedelta(days=1)
            date_E = datetime.now() - timedelta(days=0)
            print(str(date_S)[0:10])
            print(attemt)
            hastrack= False
            solution=""
            try:
                if attemt=='RHID': db_path=os.path.abspath("\\\\IXI-APPSVR02\\RHID Sustaining Production\\ttproj.db")
                if attemt=='RHIT': db_path=os.path.abspath("\\\\IXI-APPSVR02\\RapidHIT Sustaining\\ttproj.db")
                conn5 = sqlite3.connect(db_path)
                c = conn5.cursor()
                hourago= datetime.now() - timedelta(hours = 1)
                #s='select DefectNum,Summary,Status from DEFECTS inner join DEFECTEVTS on   DEFECTEVTS.ParentID=DEFECTS.idRecord   where dateEvent> '+ str(hourago).rpartition(':')[0]
                # s='select idRecord,DefectNum,Summary,Status,dateModify from DEFECTS  where dateModify >'+ repr(str(hourago).rpartition(':')[0])

                print(str(date_S).rpartition(':')[0])
                #print (str(date_E).rpartition(':')[4])
                s='select idRecord,DefectNum,Summary,Status,dateModify from DEFECTS  where  dateModify >='+  repr(str(date_S).rpartition(':')[0])
                print(s)
                #s='select idRecord,DefectNum,Summary,Status,dateModify from DEFECTS  where  dateModify >='+  repr(str(date_S).rpartition(':')[0]) + '  and  dateModify <='+  repr(str(date_E).rpartition(':')[0])
                #s='select dateModify,idRecord,DefectNum,Summary,Status,dateModify from DEFECTS  where  DefectNum =2976'
                   #'+ repr(str(hourago).rpartition(':')[0])
                c.execute(s)
                rows=c.fetchall()
                defect_as_dict=[]
                #file = open("sync.txt","w")
                for row in rows:

                        DefectNum=row[1]
                        print(DefectNum)
                        Summary=row[2]
                        Status=row[3]
                        if attemt=='RHID': s='select Custvalue from CUSTMVAL where idCustRec=681 and ParentID=' + repr(str(row[0])) + ''
                        if attemt=='RHIT': s='select Custvalue from CUSTMVAL where idCustRec=1072 and ParentID=' + repr(str(row[0])) + ''
                        c.execute(s)
                        rows1=c.fetchall()
                        casenumber=0
                        for row1 in rows1:
                            casenumber=row1[0]
                            print(casenumber)
                        #Synceddict=db.search(CN.casenumber == casenumber)
                        s='select Name,dateEvent,DEFECTEVTS.Notes ,OrderNum  from  DEFECTEVTS  inner join EVENTS on   DEFECTEVTS.EvtDefID=EVENTS.idRecord  and ParentID=' + str(row[0]) + ' order by OrderNum'
                        c.execute(s)
                        tracks_as_dict=[]
                        tracktext=""
                        tracks=c.fetchall()
                        for track in tracks:
                            hastrack= True
                            if (track[0]=="Verified"): solution=track[2]
                            track_as_dict={
                                'Event': track[0],
                                'Date': track[1],
                                'Notes': track[2]
                            }
                            if (hastrack):
                             tracks_as_dict.append(track_as_dict)
                             tracktext=str(tracks_as_dict)



                         #UPDATE WORKFLOW

                        list=sf.query("SELECT Id,Defect_Ref__c FROM Case WHERE CaseNumber = " + repr(str(casenumber)))
                        dict=list["records"]
                        if len(dict)> 0:
                             cid=dict[0]['Id']
                             CurrentDefectNumber=dict[0]['Defect_Ref__c']
                             sf.Case.update(cid,{'Workflow_from_ALM__c': tracktext})
                             if  CurrentDefectNumber is None:
                                 #sf.headers({'Sforce-Auto-Assign': 'FALSE'})
                                 sf.Case.update(cid,{'Defect_Ref__c': DefectNum})


                             #Write the log
                             file = open("C:\Python34\ixi_TBOX34\sync.txt","a")
                             logstr="|"+ str(casenumber) + "|" + str(DefectNum) +"|" + attemt +"|" + repr(str(datetime.now()))
                             file.write(logstr+"\n")
                             file.close()


                        #UPDATE SOLUTIONS
                        if Status == 10:

                            if (str(solution) != ""):

                                   list=sf.query("SELECT Id FROM Case WHERE CaseNumber = " + repr(str(casenumber)))
                                   dict=list["records"]
                                   if len(dict)> 0:
                                       print(dict[0]['Id'])
                                       cid=dict[0]['Id']
                                       mydict = sf.Solution.create({'SolutionNote':solution, 'SolutionName': 'solution - '+ Summary})
                                       #db.insert({'casenumber': casenumber})
                                       print(mydict['id'])
                                       sid=mydict['id']
                                       solution = sf.Solution.get(mydict['id'])
                                       print(mydict['success'])
                                       #orderdisc=solution('OrderDict')
                                       print(solution['SolutionNumber'])
                                       sn=solution['SolutionNumber']

                                       mydict = sf.CaseSolution.create({'CaseId': cid ,  'SolutionId':sid})
                                       print(mydict)

                        #Update case
                        #file.close()
                        #sf.Case.Update

            except  Exception as e:
                print(e)



if __name__ == '__main__':
    luigi.run()
    #luigi.run(["--local-scheduler"], sync_luigi=ixisync)

# def DoSync():
#     sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
#     print('NEW START.............................................................................................................')
#     for attemt in attemts:
#         # try:
#         #     c.close();
#         #     conn5.commit();
#         #     conn5.close();
#         #
#         # except  Exception as e:
#         #     print(e)
#         # try:
#         #     c.close();
#         #     conn6.commit();
#         #     conn6.close();
#         # except  Exception as e:
#         #     print(e)
#
#         # if attemt=='RHID': db_path=os.path.abspath("\\\\IXI-APPSVR02\\RHID Sustaining Production\\ttproj.db")
#         # if attemt=='RHIT': db_path=os.path.abspath("\\\\IXI-APPSVR02\\RapidHIT Sustaining\\ttproj.db")
#         #while True:
#             #time.sleep(60)
#            # print("After 5 sec")
#
#         date_S = datetime.now() - timedelta(days=1)
#         date_E = datetime.now() - timedelta(days=0)
#         print(str(date_S)[0:10])
#         print(attemt)
#         hastrack= False
#         solution=""
#         try:
#             if attemt=='RHID': db_path=os.path.abspath("\\\\IXI-APPSVR02\\RHID Sustaining Production\\ttproj.db")
#             if attemt=='RHIT': db_path=os.path.abspath("\\\\IXI-APPSVR02\\RapidHIT Sustaining\\ttproj.db")
#             conn5 = sqlite3.connect(db_path)
#             c = conn5.cursor()
#             hourago= datetime.now() - timedelta(hours = 1)
#             #s='select DefectNum,Summary,Status from DEFECTS inner join DEFECTEVTS on   DEFECTEVTS.ParentID=DEFECTS.idRecord   where dateEvent> '+ str(hourago).rpartition(':')[0]
#             # s='select idRecord,DefectNum,Summary,Status,dateModify from DEFECTS  where dateModify >'+ repr(str(hourago).rpartition(':')[0])
#
#             print(str(date_S).rpartition(':')[0])
#             #print (str(date_E).rpartition(':')[4])
#             s='select idRecord,DefectNum,Summary,Status,dateModify from DEFECTS  where  dateModify >='+  repr(str(date_S).rpartition(':')[0])
#             print(s)
#             #s='select idRecord,DefectNum,Summary,Status,dateModify from DEFECTS  where  dateModify >='+  repr(str(date_S).rpartition(':')[0]) + '  and  dateModify <='+  repr(str(date_E).rpartition(':')[0])
#             #s='select dateModify,idRecord,DefectNum,Summary,Status,dateModify from DEFECTS  where  DefectNum =2976'
#                #'+ repr(str(hourago).rpartition(':')[0])
#             c.execute(s)
#             rows=c.fetchall()
#             defect_as_dict=[]
#             #file = open("sync.txt","w")
#             for row in rows:
#
#                     DefectNum=row[1]
#                     print(DefectNum)
#                     Summary=row[2]
#                     Status=row[3]
#                     if attemt=='RHID': s='select Custvalue from CUSTMVAL where idCustRec=681 and ParentID=' + repr(str(row[0])) + ''
#                     if attemt=='RHIT': s='select Custvalue from CUSTMVAL where idCustRec=1072 and ParentID=' + repr(str(row[0])) + ''
#                     c.execute(s)
#                     rows1=c.fetchall()
#                     casenumber=0
#                     for row1 in rows1:
#                         casenumber=row1[0]
#                         print(casenumber)
#                     #Synceddict=db.search(CN.casenumber == casenumber)
#                     s='select Name,dateEvent,DEFECTEVTS.Notes ,OrderNum  from  DEFECTEVTS  inner join EVENTS on   DEFECTEVTS.EvtDefID=EVENTS.idRecord  and ParentID=' + str(row[0]) + ' order by OrderNum'
#                     c.execute(s)
#                     tracks_as_dict=[]
#                     tracktext=""
#                     tracks=c.fetchall()
#                     for track in tracks:
#                         hastrack= True
#                         if (track[0]=="Verified"): solution=track[2]
#                         track_as_dict={
#                             'Event': track[0],
#                             'Date': track[1],
#                             'Notes': track[2]
#                         }
#                         if (hastrack):
#                          tracks_as_dict.append(track_as_dict)
#                          tracktext=str(tracks_as_dict)
#
#
#
#                      #UPDATE WORKFLOW
#
#                     list=sf.query("SELECT Id,Defect_Ref__c FROM Case WHERE CaseNumber = " + repr(str(casenumber)))
#                     dict=list["records"]
#                     if len(dict)> 0:
#                          cid=dict[0]['Id']
#                          CurrentDefectNumber=dict[0]['Defect_Ref__c']
#                          sf.Case.update(cid,{'Workflow_from_ALM__c': tracktext})
#                          if  CurrentDefectNumber is None:
#                              #sf.headers({'Sforce-Auto-Assign': 'FALSE'})
#                              sf.Case.update(cid,{'Defect_Ref__c': DefectNum})
#
#
#                          #Write the log
#                          file = open("C:\Python34\ixi_TBOX34\sync.txt","a")
#                          logstr="|"+ str(casenumber) + "|" + str(DefectNum) +"|" + attemt +"|" + repr(str(datetime.now()))
#                          file.write(logstr+"\n")
#                          file.close()
#
#
#                     #UPDATE SOLUTIONS
#                     if Status == 10:
#
#                         if (str(solution) != ""):
#
#                                list=sf.query("SELECT Id FROM Case WHERE CaseNumber = " + repr(str(casenumber)))
#                                dict=list["records"]
#                                if len(dict)> 0:
#                                    print(dict[0]['Id'])
#                                    cid=dict[0]['Id']
#                                    mydict = sf.Solution.create({'SolutionNote':solution, 'SolutionName': 'solution - '+ Summary})
#                                    #db.insert({'casenumber': casenumber})
#                                    print(mydict['id'])
#                                    sid=mydict['id']
#                                    solution = sf.Solution.get(mydict['id'])
#                                    print(mydict['success'])
#                                    #orderdisc=solution('OrderDict')
#                                    print(solution['SolutionNumber'])
#                                    sn=solution['SolutionNumber']
#
#                                    mydict = sf.CaseSolution.create({'CaseId': cid ,  'SolutionId':sid})
#                                    print(mydict)
#
#                     #Update case
#                     #file.close()
#                     #sf.Case.Update
#
#         except  Exception as e:
#             print(e)
#
#
#     # print('Waiting...')
#     # time.sleep(3000)

