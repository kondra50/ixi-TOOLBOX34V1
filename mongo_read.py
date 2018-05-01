from pymongo import MongoClient
from datetime import datetime
client = MongoClient()
db = client.test
empCol = db.test.find({"HOST":'192.168.3.205'})
print('\n All data from EmployeeData Database \n')
for emp in empCol:
    print(emp)
