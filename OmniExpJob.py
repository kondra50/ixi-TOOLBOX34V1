import OmniExp
import os,time
Main_Path='C:\Python34\ixi_TBOX34\PLM_FILES'
# OX=OmniExp.transformer("C:\\Python34\\ixi_TBOX34\\PLM_FILES\\2.plm")
# Part_List,Vendor_Part_List,BOM_List= OX.ReadFile()
# Result,Error=OX.Call_Expandable_API(Part_List,Vendor_Part_List,BOM_List)
# OX.Prepare_Report(Result)
# OX.MovFile("2.plm",Error)
# print(Part_List)
# print(OX.path)

while (True):

    filenames = next(os.walk(Main_Path))
    plmfiles=[f for f in filenames[2]  if '.plm' in str(f)]
    for file in plmfiles:
        plmfile=Main_Path+'\\'+file
        OX=OmniExp.transformer(plmfile)
        Part_List,Vendor_Part_List,BOM_List= OX.ReadFile()
        Result,Error=OX.Call_Expandable_API(Part_List,Vendor_Part_List,BOM_List)
        OX.Prepare_Report(Result)
        OX.MovFile(file,Error,Main_Path)
        OX.Send_ECUDU_Jasperreport()

    print('Waiting')
    time.sleep(10)



