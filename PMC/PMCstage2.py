
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

# http://www.ebi.ac.uk/europepmc/webservices/rest/PMC3257301/fullTextXML




f=open('PMClist.csv', 'rU')
csv_f = csv.reader(f)

for i in range(1, 2, 1):
    next(csv_f, None)



for row in csv_f:
    if(row[0] != ""):
        IDlist.append(row[1])

print(IDlist)



alist = [];
strURL1 = 'https://clinicaltrials.gov/ct2/results?term='
strURL2 = '%20'



strURL11 = 'http://www.ebi.ac.uk/europepmc/webservices/rest/'
strURL21 = '/fullTextXML'

for indic11 in IDlist:


 strURL31 = strURL11 + 'PMC3257301' + strURL21

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

    for item in xml.findAll('publisher'):
       party = item.find('publisher-name')
       if party is None:
        PMCID.append("NULL")
       else:
        NewItem = party.text
        PMCID.append(NewItem)


 except URLError as e:
      if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
      elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
 else:



         print("Stage 2 processing..")


final3=sum(FText, [])



print(final3)
print(PMID)
f = open('PMCoutput.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow(( 'Pubmed ID','PMC ID','Source'))
    for i2,i222,i3 in zip(PMID,PMCID,FText):

         writer.writerow( ( i2,i222,i3) )
finally:
    f.close()
