
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
Source=[]
PMCID=[]
allTrials=[]

# http://www.ebi.ac.uk/europepmc/webservices/rest/PMC3257301/fullTextXML




f=open('PMClist.csv', 'rU')
csv_f = csv.reader(f)

for i in range(1, 2, 1):
    next(csv_f, None)



for row in csv_f:
    if(row[0] != ""):
        allTrials.append(row[0])

print(allTrials)

#list1 = [x.strip(' ') for x in list1]
alist = [];
strURL1 = 'https://clinicaltrials.gov/ct2/results?term='
strURL2 = '%20'


# ['NCT00134563','NCT00228163','NCT00475865','NCT00489489','NCT00622700','NCT00751881','NCT00803049','NCT00811395','NCT00883337','NCT01252355','NCT01487096','NCT00261846','NCT00811070','NCT00574873','NCT00195260','NCT00097357','NCT00643201','NCT00412984','NCT00313300','NCT00831441','NCT00457002','NCT00633893','NCT00496769','NCT00376168','NCT00712348','NCT00705939','NCT00962260','NCT01132690','NCT00636610','NCT00739661','NCT00968981','NCT00959647','NCT01209143','NCT01160250','NCT00833417','NCT01174264','NCT00447005','NCT00569946','NCT00094055','NCT00282048','NCT00678392','NCT00835978','NCT00094107','NCT00076011','NCT00094094','NCT00134719','NCT00127855','NCT00129116','NCT00129129','NCT00359983','NCT00614614','NCT00289783','NCT00345579','NCT00345683','NCT00545688','NCT00976989','NCT00058552','NCT01674062','NCT00058539','NCT02004093','NCT00063154','NCT00096993','NCT00567190','NCT01600963','NCT00910871','NCT00449644','NCT00523926','NCT00910806','NCT01287598','NCT00934882','NCT01003015','NCT01096030','NCT01103323','NCT00960258','NCT01318265','NCT01339104','NCT00664326','NCT00892437','NCT00869557','NCT01108510','NCT00708162','NCT01106586','NCT00445146','NCT01363011','NCT00298350','NCT01095796','NCT00413660','NCT00847613','NCT00814307','NCT00856544','NCT00147498','NCT00603512','NCT00687193','NCT00661661','NCT00413699','NCT00976599','NCT01164579','NCT00853385','NCT00550446','NCT01059864','NCT00960440',' NCT00561470','NCT00851084','NCT00574275','NCT00327444','NCT00532155','NCT00519285','NCT00327171','NCT00284141','NCT00396591','NCT00918346','NCT01087671','NCT01026831']

#final=['NCT00134563','NCT00228163','NCT00475865','NCT00489489','NCT00622700','NCT00751881','NCT00803049','NCT00811395','NCT00883337','NCT01252355','NCT01487096','NCT00261846','NCT00811070','NCT00574873','NCT00195260','NCT00097357','NCT00643201','NCT00412984','NCT00313300','NCT00831441','NCT00457002','NCT00633893','NCT00496769','NCT00376168','NCT00712348','NCT00705939','NCT00962260','NCT01132690','NCT00636610','NCT00739661','NCT00968981','NCT00959647','NCT01209143','NCT01160250','NCT00833417','NCT01174264','NCT00447005','NCT00569946','NCT00094055','NCT00282048','NCT00678392','NCT00835978','NCT00094107','NCT00076011','NCT00094094','NCT00134719','NCT00127855','NCT00129116','NCT00129129','NCT00359983','NCT00614614','NCT00289783','NCT00345579','NCT00345683','NCT00545688','NCT00976989','NCT00058552','NCT01674062','NCT00058539','NCT02004093','NCT00063154','NCT00096993','NCT00567190','NCT01600963','NCT00910871','NCT00449644','NCT00523926','NCT00910806','NCT01287598','NCT00934882','NCT01003015','NCT01096030','NCT01103323','NCT00960258','NCT01318265','NCT01339104','NCT00664326','NCT00892437','NCT00869557','NCT01108510','NCT00708162','NCT01106586','NCT00445146','NCT01363011','NCT00298350','NCT01095796','NCT00413660','NCT00847613','NCT00814307','NCT00856544','NCT00147498','NCT00603512','NCT00687193','NCT00661661','NCT00413699','NCT00976599','NCT01164579','NCT00853385','NCT00550446','NCT01059864','NCT00960440','NCT00561470','NCT00851084','NCT00574275','NCT00327444','NCT00532155','NCT00519285','NCT00327171','NCT00284141','NCT00396591','NCT00918346','NCT01087671','NCT01026831']


strURL11 = 'http://www.ebi.ac.uk/europepmc/webservices/rest/'
strURL21 = '/fullTextXML'

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
        Source.append(y)

       else:
        Source.append("NULL")

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


final3=sum(Source, [])



#result=reduce(operator.add, Source)


print(final3)
print(PMID)
f = open('PMClist.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow(( 'Pubmed ID','PMC ID','Source'))
    #mylist = list(set(list01))
    #mylist1 = list(set(list02))
    #mylist2 = list(set(list03))
    #for i1 in list11:
    for i2,i222,i3 in zip(PMID,PMCID,final3):

         writer.writerow( ( i2,i222,i3) )
finally:
    f.close()
