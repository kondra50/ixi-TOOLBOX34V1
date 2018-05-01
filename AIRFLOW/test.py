from  utility import utility
import base64
utl=  utility()
s= utl.db_connection_strong()
print(s)

print(utl.recipients('IncominQC'))



# file = open("recipients.txt", 'r')
# lines = file.readlines()
# file.close()
# for line in lines:
#     parts = line.split(':')
#     print(parts[0])
#     if (parts[0]=='test'): print(parts[1])