
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
Source=[]
PMCID=[]

# http://www.ebi.ac.uk/europepmc/webservices/rest/search??query=aubagio%20


# Your input Org IDs go here:
alist = [];
strURL1 = 'https://clinicaltrials.gov/ct2/results?term='
strURL2 = '%20'



strURL11 = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search??query='
strURL21 = '%20'

strURL31 = strURL11 + 'aubagio' + strURL21

try:


    req2 = urllib.request.urlopen(strURL31)
    xml = bs4.BeautifulSoup(req2, 'xml')
    for item in xml.findAll('result'):
       party = item.find('pmid')
       if party is None:
        PMID.append("NULL")
       else:
        NewItem = party.text
        PMID.append(NewItem)

    for item in xml.findAll('result'):
       party = item.find('source')
       if party is None:
        Source.append("NULL")
       else:
        NewItem = party.text
        Source.append(NewItem)

    for item in xml.findAll('result'):
       party = item.find('pmcid')
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

print(PMID)
print(PMCID)
f = open('PMClist.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow(( 'Pubmed ID','PMC ID','Source'))
    for i2,i222,i3 in zip(PMID,PMCID,Source):

         writer.writerow( ( i2,i222,i3) )
finally:
    f.close()
