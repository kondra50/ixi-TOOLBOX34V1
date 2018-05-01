#
# import smtplib,os
#
#
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# from email.mime.image import MIMEImage
# from email.mime.multipart import  MIMEMultipart
#
#
# try:
#       msg = MIMEMultipart()
#       msg['Subject'] = 'The contents of '
#       msg['From'] = "mehrdadn@integenx.com"
#       msg['To'] = "mehrdadn@integenx.com"
#
#       with open("C:\\Python34\\ixi_TBOX34\\PLM_FILES\\C.pdf", 'rb') as fp:
#         img = MIMEApplication(fp.read(), 'pdf')
#         msg.attach(img)
# except Exception as e:
#
#       print(e)
#
#
#
# msg['Subject'] = 'The contents of '
# msg['From'] = "mehrdadn@integenx.com"
# msg['To'] = "mehrdadn@integenx.com"
#
# try:
#
#       s = smtplib.SMTP('IXI-EXCH.microchipbiotech.com')
#       s.send_message(msg)
#       s.quit()
# except Exception as e:
#
#       print(e)

filepath="C:\\Python34\\ixi_TBOX34\\PLM_FILES\\PROCESSED\\2-8-2017 10-51-20 AM-ECO-001812-2017-02-08_10-52-52-AM.plm"
mylist=str(filepath).split("\\")
print(mylist[len(mylist)-1])
for item in mylist:
    print(item)
















# SERVER = "IXI-EXCH.microchipbiotech.com"
# FROM = "mehrdadn@integenx.com"
# TO = ["mehrdadn@integenx.com"
#       ""
#       ""
#       ""] # must be a list
#
# SUBJECT = "Subject"
# TEXT = "Your Text"
#
#
#
#
#
# import os
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# try:
#       msg = MIMEMultipart()
#       fp = open('C:\Python34\ixi_TBOX34\PLM_FILES\metadata.pdf', 'rb')
#       msg.attach(MIMEText(fp.read()))
#
# except Exception as e:
#
#       print(e)
#
#
#
#
#
#
#
#
#
#
# message = "test"
#
# print('tets')
# import smtplib
# server = smtplib.SMTP(SERVER)
# server.sendmail(FROM, TO, message)
# server.quit()