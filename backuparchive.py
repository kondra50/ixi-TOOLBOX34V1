import datetime
import glob
import os
import luigi
from shutil import copyfile,copy
import smtplib
from myemail.mime.text import MIMEText


class papa(luigi.Task):

    #src = "qwqw"

    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget('test3')

    def run(self):
        print('test')
        # yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        # filename = 'ESIDB_backup_'+ str(yesterday.year) +'_'+ str(yesterday.month).zfill(2) +'_'+ str(yesterday.day).zfill(2) +'_*.bak'
        # os.chdir('\\\\ixi-erp\\Backup')
        # for file in glob.glob(filename):
        #     src=file
        #     print(file)
        #
        # # CREATE A NEW FOLDER
        # newpath = '\\\\ixi-erp\ExpandableArchives\\'+ str(yesterday.year) +'_'+ str(yesterday.month).zfill(2) +'_'+ str(yesterday.day).zfill(2)
        # print(newpath)
        # if not os.path.exists(newpath):
        #     os.makedirs(newpath)
        #
        # # COPY END OF THE MONTH BACKUP FILE
        # copy(src, newpath)
        #
        #
        # msg = MIMEText('Hi Mark,I put the back up of last month in this address: '+ newpath +' .Please copy it onto the Append Only IXI_ERP tape.')
        # msg['Subject'] = 'Backup Archive '+ str(yesterday.year) +'_'+ str(yesterday.month).zfill(2) +'_'+ str(yesterday.day).zfill(2)
        # msg['From'] = 'mehrdadn@integenx.com'
        # msg['To'] = 'mehrdadn@integenx.com'
        # s = smtplib.SMTP('IXI-EXCH.microchipbiotech.com')
        # s.sendmail('mehrdadn@integenx.com', 'mehrdadn@integenx.com', msg.as_string())
        # s.quit()

if __name__ == '__main__':
    luigi.run()


# # FIND YESTERDAY BACKUP
# yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
# filename = 'ESIDB_backup_'+ str(yesterday.year) +'_'+ str(yesterday.month).zfill(2) +'_'+ str(yesterday.day).zfill(2) +'_*.bak'
# print (filename)
# print(yesterday.month)
# os.chdir('\\\\ixi-erp\\Backup')
# for file in glob.glob(filename):
#     src=file
#     print(file)
#
#
# # CREATE A NEW FOLDER
# newpath = '\\\\ixi-erp\ExpandableArchives\\'+ str(yesterday.year) +'_'+ str(yesterday.month).zfill(2) +'_'+ str(yesterday.day).zfill(2)
# print(newpath)
# if not os.path.exists(newpath):
#     os.makedirs(newpath)
#
# # COPY END OF THE MONTH BACKUP FILE
#
#
# copy(src, newpath)
#
#
# msg = MIMEText('Hi Mark,I put the back up of last month in this address: '+ newpath +' .Please copy it onto the Append Only IXI_ERP tape.')
# msg['Subject'] = 'Backup Archive '+ str(yesterday.year) +'_'+ str(yesterday.month).zfill(2) +'_'+ str(yesterday.day).zfill(2)
# msg['From'] = 'mehrdadn@integenx.com'
# msg['To'] = 'mehrdadn@integenx.com'
#
#
# s = smtplib.SMTP('IXI-EXCH.microchipbiotech.com')
# s.sendmail('mehrdadn@integenx.com', 'mehrdadn@integenx.com', msg.as_string())
# s.quit()