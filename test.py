
import pandas
import xlrd

import xlrd
import os.path
# wb = xlrd.open_workbook(os.path.join('c:\\temp\\Part StatusUpdates.xlsx'))
# wb.sheet_names()
# sh = wb.sheet_by_index(0)
# values = []
# for r in range(sh.nrows):
#     col_names = sh.row(0)
#     # print(col_names)
#     col_value = []
#     for name, col in zip(col_names, range(sh.ncols)):
#         value  = (sh.cell(r,col).value)
#         try : value = str(int(value))
#         except : pass
#         col_value.append((name.value, value))
#     values.append(col_value)
# print(values)
    # for c in range(sh.ncols):
    #     data =sh.cell_value(r,s)+" "
    #     print (data)

#x='%03d' % 70
#print(x)

# #df = pandas.read_excel('c:\\temp\\Part StatusUpdates.xlsx')
# book = xlrd.open_workbook('c:\\temp\\Part StatusUpdates.xlsx')
# first_sheet = book.sheet_by_index(0)
# print(book.nsheets)
# cells = first_sheet.row_slice(rowx=0,
#                               start_colx=0,
#                               end_colx=2)
# for cell in cells:
#     print(cell.value)
#
#
# rows=first_sheet.row(3)
# for row in rows:
#     print(row)

#print the column names
#print(df.columns)
#get the values for a given column
#values = df['Arm_id'].values
#get a data frame with selected columns
#FORMAT = ['Arm_id', 'DSPName', 'Pincode']
#df_selected = df[FORMAT]



# from operator import itemgetter
# import itertools
# tmp = [
#     {'name': 'foo', 'age': 35, 'level': 1},
#     {'name': 'foo', 'age': 35, 'level': 1},
#     {'name': 'bar', 'age': 11, 'level': 5},
#     {'name': 'john', 'age': 28, 'level': 3},
#     {'name': 'doe', 'age': 74, 'level': 9},
#     {'name': 'alex', 'age': 12, 'level': 7},
# ]
#
#
# tmp=sorted(tmp, key=itemgetter('level'))
# sumdict=[]
# for key,val in itertools.groupby(tmp, key=itemgetter('level')):
#     print(key)
#     sum=0
#     for i in val:
#         sum+=i.get('age')
#     innerdict=[key,sum]
#     sumdict.append(innerdict)
#
# print(sumdict)
#
# print(sorted(tmp, key=itemgetter('level')))
#
# students = [
#     {'name': 'alex','class': 'A'},
#     {'name': 'richard','class': 'A'},
#     {'name': 'john','class': 'C'},
#     {'name': 'harry','class': 'B'},
#     {'name': 'rudolf','class': 'B'},
#     {'name': 'charlie','class': 'E'},
#     {'name': 'budi','class': 'C'},
#     {'name': 'gabriel','class': 'B'},
#     {'name': 'dessy', 'class': 'B'}
# ]
#
# # Sort students data by `class` key.
# students = sorted(students, key=itemgetter('class'))
#
# # for key,value in  itertools.groupby(students,key=itemgetter('level')):
# #     print (key)
# subdict=[]
#
# for key, value in itertools.groupby(students, key=itemgetter('class')):
#     print(key)
#     count=0
#     for i in value:
#         print(i.get('name'))
#         count += 1
#     smalldict=[key,count]
#     subdict.append(smalldict)
#
# print(subdict)

import pandas as pd
df = pd.read_excel("PartStatusUpdates.xlsx")
part_list=df['PART_ID']
my_list = [str(x) for x in part_list]
lis1=my_list
print(my_list)