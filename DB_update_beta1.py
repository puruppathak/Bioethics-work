import csv
from itertools import filterfalse, zip_longest
import csv
from random import choice
import sys
import bs4
import lxml
import urllib.request
from itertools import islice
from urllib.request import Request, urlopen
from urllib.error import URLError
import xml.etree.ElementTree as ET
import re
import datetime
from dateparser import parse

import pymysql

OrgID=[]
NCTID=[]
Btitle=[]
OverallStatus=[]
condition=[]
agency=[]
gender=[]
MAge=[]
Phase1=[]
AgencyClass=[]
StudyType=[]
StudyDesign=[]
SecID=[]
FirstRecv=[]
SDate=[]
ComplDate=[]
LastChangedDate=[]
VerificationDate=[]
FirstRecvResultDate=[]
PCD=[]
Countries=[]
Condition=[]
IsFDA=[]
Is801=[]
FDAOrg1=[]
Intervention=[]
acronym=[]
alist2=[]
FDAOrg=[]
Rm_Countries=[]
FirstRecvResultDispoDate=[]
NewNCT=[]


##


#making connection to database use proper password and username
connection = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor,
                             db = 'puru')

cursor = connection.cursor()


NCTlist=[]
ECount=[]

strURL11 = 'https://clinicaltrials.gov/show/'
strURL21 = '?displayxml=true'

cursor.execute('SELECT * FROM db_update')

for row in cursor:
    if row["OrgID"] is None:
        NCTlist.append(row["NCT"])


for row in NCTlist:



        strURL31 = strURL11 + row + strURL21

        try:

                req2 = urllib.request.urlopen(strURL31)
                xml = bs4.BeautifulSoup(req2, 'xml')
                for item in xml.findAll('id_info'):
                    party = item.find('org_study_id')
                    if party is None:
                        OrgID.append("NULL")
                    else:
                        NewItem = str(party.text)

                        cursor.execute("update db_update set OrgID = %s where NCT = %s ",(NewItem,row))
                        print('changed', cursor.rowcount)
                        connection.commit()



        except URLError as e:
                if hasattr(e, 'reason'):
                    print('We failed to reach a server.')
                    print('Reason: ', e.reason)
                elif hasattr(e, 'code'):
                    print('The server couldn\'t fulfill the request.')
                    print('Error code: ', e.code)
        else:

                print("Stage 2 processing..")



##




#closing the connection to the database
cursor.close()
connection.close()


