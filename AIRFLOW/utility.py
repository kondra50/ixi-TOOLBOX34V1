import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import base64



class utility(object):
     def __init__(self):
        """Return a Customer object whose name is *name*."""
     def db_connection_strong(self):
         #str= """ host='192.168.3.40', user='', password='', database='ESI_JUN_2017' """""
         return base64.b64decode('aG9zdD0nMTkyLjE2OC4zLjQwJywgdXNlcj0nc3lzZGJhJywgcGFzc3dvcmQ9J2UkMXNfcycsIGRhdGFiYXNlPSdFU0lfSlVOXzIwMTcnIA==')
         #return base64.b64encode(str)

     def recipients(self,DAG):
         file = open("recipients.txt", 'r')
         lines = file.readlines()
         file.close()
         for line in lines:
             parts = line.split(':')
             if (parts[0]==DAG): return parts[1]
