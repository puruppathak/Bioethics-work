
__author__ = 'puruppathak'

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
import operator

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
enrollment=[]
PMID=[]
ID=[]
FText=[]
PMCID=[]
IDlist=[]
PubID=[]


# http://www.ebi.ac.uk/europepmc/webservices/rest/PMC3257301/fullTextXML

# http://www.ebi.ac.uk/europepmc/webservices/rest/PMC4264640/fullTextXML



f=open('PMClist.csv', 'rU')
csv_f = csv.reader(f)

for i in range(1, 2, 1):
    next(csv_f, None)



for row in csv_f:
    if(row[1] != "NULL"):
        IDlist.append(row[1])
        PubID.append(row[0])

print(IDlist)

result = list(IDlist)

alist = [];



strURL11 = 'http://www.ebi.ac.uk/europepmc/webservices/rest/'
strURL21 = '/fullTextXML'

for indic11 in result:


 strURL31 = strURL11 + indic11 + strURL21

 try:


    req2 = urllib.request.urlopen(strURL31)
    xml = bs4.BeautifulSoup(req2, 'xml')
    for item in xml.findAll('article-meta'):
       party = item.find('article-id')
       if party is None:
        PMID.append("NULL")
       else:
        NewItem = party.text
        PMID.append(NewItem)

    for item in xml.findAll('body'):
       y=re.findall('<body>(.*)</body>',str(item))
       if y:
           FText.append(y)

       else:
           FText.append("NULL")



 except URLError as e:
      if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
      elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
 else:



         print("Stage 2 processing..")


#final3=sum(FText, [])


f = open('PMCMidStage.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow(( 'Pubmed ID','PMC ID','Full Text'))
    for i2,i222,i3 in zip(PubID,PMID,FText):

         writer.writerow((i2,i222,i3))
finally:
    f.close()


# Filters start from here

f=open('PubMedData.csv', 'rU')
csv_f = csv.reader(f)


#patients=['31','28']
allTrials = []
first_stage_cleared = []
registered_trials = []
published_trials = []
reported_trials = []
timely_reported_trials = []
available_trials = []
available_trials1=[]
available_trials2=[]

patients=['60','24','40','1149','598','641','1064','345','54','6','45','16','43','28','35','486','42','48','969','70','49','36','135','203']

for row in csv_f:
    if(row[1] != ""):
        allTrials.append(row)

    for i in patients:
        for row in allTrials:
            if (i in str(row[2]).lower()):
                registered_trials.append(row)

print()


for row in registered_trials:
    if("cerexa" in row[2].lower()):
        available_trials1.append(row)




NCTs=['NCT01624246','NCT01499290','NCT01595438','NCT01599806','NCT01500239','NCT01644643','NCT01290900','NCT01448395','NCT01395420','NCT01291602','NCT01430910','NCT01534247','NCT01893346','NCT01726023','NCT01920399','NCT01789528','NCT01808092','NCT00690378','NCT00752219']
NCT_check=[]

for i in NCTs:
  for row in allTrials:
    if (i in str(row[2])):
        NCT_check.append(row)


for row in allTrials:
    if ((row in available_trials1) or (row in NCT_check)):
        available_trials2.append(row)




f = open('PMCoutput.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow(('Pubmed ID','PMC ID','Full Text'))

    for i1 in (available_trials2):

         writer.writerow( (i1) )
finally:
    f.close()
