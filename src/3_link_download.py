import sys
import time
import random
from smtplib import SMTP
from email.mime.text import MIMEText
import glob
import os

doc=open('email_links/links','r',encoding='utf-8')
doc_links = doc.readlines()
doc.close()

downloaded={}
try:
    doc=open('email_links/downloaded','r')
    doc_downloaded=doc.readlines()
    doc.close()
except:
    doc_downloaded=[]


for i in doc_downloaded:
    tmp=i.split()
    downloaded[tmp[0]] = True


for info in doc_links:
    if info.__contains__('http://'):
        doc_downloaded=open('email_links/downloaded','a')
        tmp = info.split()
        link = tmp[1]
        filename = link.split('/')
        filename = filename[-1]
        if (link in downloaded.keys() ):
            print('link %s has been downloaded'%(link))
        elif (os.path.exists('./data/%s'%(filename))):
             print('link %s has been downloaded, but not record'%(link))
            #  doc_downloaded.write('%s \n'%(link))
        else:
            os.system('wget %s -P ./data'%(link))
            doc_downloaded.write('%s \n'%(link))
        doc_downloaded.close()
