# a = [2, 3, 5, 6]
# b = [4, 6, 8, 3]
#
# result = zip(a, b)
# print(list(result))
# # map(lambda item: item['link'], data['data']
#
# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))
# print(squared)
#
#
# number_list = range(-5, 5)
# #less_than_zero = list(filter(lambda x: x < 0, number_list))
# mylist=list(filter(lambda x:x <0,number_list))
# print(mylist)

# import os,glob
#
# os.chdir("c:")
# for file in glob.glob('*.txt'):
#     print(file)

# for i in range (1,101):
#     if i % 5 == 0 and i %3 == 0:
#         print('both')
#     elif i % 3 == 0 :
#         print('fizz')
#     elif i % 5 ==0 :
#         print('buzz')
#     else:
#         print(i)

# a,b = 0,1
# sum=0
# for i in range (1,10):
#     # sum=sum+i;
#     # print("Tsum is", sum, "number is", i)
#     a,b=b,a+b
#     print("a", a, "nb", b)


# mylist=[]
#
# mylist =[x*x for x in range(1,10)]
# print(mylist)
import json
# js = open('C:\Python34\ixi_TBOX34\myjson.json').read()
# print(js)
# json_str = json.dumps(js)
# data = json.loads(json_str)
# print(data["color"])


# json_data = '{"name": "Brian", "city": "Seattle"}'
# python_obj = json.loads(json_data)
# print(len(python_obj))
# # print(python_obj[1]["name"])
# # print(python_obj[1]["city"])
# for item in python_obj:
#     for key,value in item.iteritems():
#
#         print(key,value)
import pandas as pd

#pd.read_csv('C:\Python34\ixi_TBOX34\input.csv')
#print(pd)
# mylist = open('C:\Python34\ixi_TBOX34\input.csv', 'r')
# mylist1=[1,2,7,1123,3,2346,12,1,5,6]
# print(list(mylist))
# mylist1.sort()
# import csv
# with open('C:\Python34\ixi_TBOX34\input.csv', 'r') as f:
#     reader = csv.reader(f)
#     L = list(reader)
#print [int(x) for x in L]
# print(L)
# convertedlist=[x for x in L]
# print(list(L3))
#
# T=['3','4','5']
# for x in T:
#     print(x);

#
import csv
list=[]
outputlist=[]
fh = open('C:\Python34\ixi_TBOX34\input.csv', 'r')
for line in fh:
   list.append(line.strip().split(','))

print(list)

# for x in list[0]:
#     print(x)

mylist=[int(x) for x in list[0]]
mylist.sort()
print(len(mylist))
print(mylist[9])
for x in range(mylist[0],mylist[9]):
    if  x  not in mylist:
        outputlist.append(x)
        #print(x)

print(outputlist)
L2=[x + 1 for x, y in zip(mylist[:-1], mylist[1:]) if y - x > 1]

print(L2)


with open("C:\Python34\ixi_TBOX34\output.csv",'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(outputlist)

# mylist=[]
# rf = open('C:\\Python34\\ixi_TBOX34\\1.log', 'r')
# for l in rf:
#     print(l.strip().split(' '))
#     mylist.append(l.strip().split(' '))
