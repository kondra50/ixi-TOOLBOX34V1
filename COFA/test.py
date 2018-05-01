from flask import jsonify
import pymssql
conn = pymssql.connect(host='192.168.3.40', user='sysdba', password='e$1s_s', database='ESIDB')

def report(M_PART_ID,M_LOT_ID):
  try:
        header_as_dict=[]
        details_as_dict=[]
        all_as_dict=[]
        cur = conn.cursor()
        cur.execute('select [Product_Name] ,ltrim(rtrim([Product_Type])),[Manuf_Date],[Exp_Date],ltrim(rtrim([Storage_Condition])),[IsPart],[IsValid],ltrim(rtrim([DWG_REV])),[TEMPLATE_ID],[REF_CAT] FROM [ESIDB].[dbo].[Adm_tmp_CerOfAna_BACKLOG] where [M_PART_ID]='+ M_PART_ID +' and M_LOT_ID='+ M_LOT_ID +' ')
        rows = cur.fetchall()
        for row in rows:
             cofa_as_dict= {
             'Product_Name': row[0],
             'Product_Type': row[1],
             'Manuf_Date': row[2],
             'Exp_Date': row[3],
             'Storage_Condition': row[4],
             'IsPart': row[5],
             'IsValid': row[6],
             'DWG_REV': row[7],
             'TEMPLATE_ID': row[8],
             'REF_CAT': row[9]
             }
             header_as_dict.append(cofa_as_dict)



        cur.execute('select  ltrim(rtrim([PART_ID])) ,[PART_DESC],ltrim(rtrim([LOT_ID])) FROM [ESIDB].[dbo].[Adm_tmp_LOTTRACE_Crystal_BACKKLOG] where [M_PART_ID]='+ M_PART_ID +' and M_LOT_ID='+ M_LOT_ID +' ')
        rows = cur.fetchall()
        for row in rows:
             cofa_as_dict= {
             'PART_ID': row[0].strip(),
             'PART_DESC': row[1].strip(),
             'LOT_ID': row[2].strip()
             }
             details_as_dict.append(cofa_as_dict)



        return header_as_dict,details_as_dict
  except Exception as e:
          return {"Error":"There is problem in connecting to database"}


  report('P040581','160126')