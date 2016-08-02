# This script takes inconsistent IDs as input and cleans them by dealing with missing characters
# Algorithm coded and designed by Mr. Puru Pathak.
# This software is a property of Bioethics International. All rights reserved.
# Republication or redistribution of the software content is prohibited.
# Stage 2 software for ClinicalTrials.org


__author__ = 'puruppathak'

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
FDAOrg1=[]
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
Intervention=[]
acronym=[]
listStr=[]
alist3=[]
FirstRecvResultDispoDate=[]
str12="NULL"
allTrials=[]

# Aubagio =  ['1001','1002','1024','1932','2001','ALI6504','BDR6639','BEQ10169','BEX6038','EFC10531','EFC6049','HWA486-1024','INT10563','INT10564','INT11697','INT11720','INT11932','INT6039','INT6040','LTS6047','LTS6048','LTS6050','PDY6045','PDY6046','PDY11684','PHM0086','PMH0091','PMH0091','POH0290','POH0295','POP11432','POP6505','POP6507','SIM0041','TDR10892','TES10852','EFC6058','EFC6260','EFC10891'];
# Bosulif = ['3160A4-200','3160A4-3000','3160A4-2203','3160A4-1109','3160A4-1115','3160A4-1120','3160A1-103','3160A4-1110','3160A1-100','3160A1-102','3160A4-1112','3160A4-105','3160A4-1111','3160A4-104','3160A4-1114','3160A4-1106','3160A4-1108','3160A6-2207','3160A4-2203']
# Elelyso = ['P-01-2005','PB-06-001','PB-06-002','PB-06-003','PB-06-004','PB-06-005']
# Eliquis = ['CV185030','CV185048','CV185001','CV185002a','CV185002b','CV185005','CV185006','CV185007','CV185008','CV185010','CV185013','CV185015','CV185017','CV185018','CV185019','CV185020','CV185022','CV185023','CV185024','CV185025','CV185026','CV185028','CV185031','CV185032','CV185033','CV185036','CV185045','CV185046','CV185054','CV185055','CV185056','CV185057','CV185058','CV185059','CV185060','CV185061','CV185067','CV185068','CV185070','CV185074','CV185104']
# Erivedge = ['SHH4893s','SHH3925g','SHH4318g','SHH4429g','SHH4433g','SHH4437g','SHH4476g','SHH4489g','SHH4593g','SHH4610g','SHH4683g','SHH4811g','SHH4871g','SHH8395g']
# Inlyta = ['A4060010','A4060019','A4061003','A4061004','A4061006','A4061007','A4061011','A4061012','A4061014','A4061015','A4061018','A4061021','A4061022','A4061023','A4061026','A4061032','A4061033','A4061035','A4061036','A4061037','A4061044','A4061046','A4061047','A4061050','A4061052','A4061053','A4061063','A4061019','A4061045']
# Menhibrix = ['103813','105067','102370','102371','101858','102015','105987','105988','107824','110870','792014/001','792014/002','792014/003','100381/004']
# Perjeta = ['WO20697','BO22280','WO20698','TOC4129g','TOC2682g','TOC2572g','TOC3258g','BO17003','BO17021','WO20024','BO16934','BO17004','BO17931','BO17929','JO17076','TOC2689g']
# Signifor = ['B2101','B2102','B2103','B2106','B2107','B2108','B2110','B2112','B2113','B2114','B2124','B2125','B2201','B2201E1','B2202','B2208','B2208E1','B2216','B2305','C2101']
# Sirturo = ['TMC207-C202','TMC207-C208','TMC207-C209','CDE-101','BAC1003','C108','C110','C111','CDE-102','C104','C109','C117','C112','TBC1003','C210']
# Stivarga = ['11650','11651','11656','11726','12434','12435','12436','12437','13172','14596','14656','14814','14996','15524','14387']
# Stribild = ['GS-US-183-0101','GS-US-183-0102','GS-US-183-0105','GS-US-183-0113','GS-US-183-0119','GS-US-183-0126','GS-US-183-0128','GS-US-183-0130','GS-US-183-0133','GS-US-183-0140','GS-US-183-0145','GS-US-183-0146','GS-US-216-0105','GS-US-216-0106','GS-US-216-0107','GS-US-216-0114','GS-US-216-101','GS-US-216-111','GS-US-216-112','GS-US-216-113','GS-US-216-116','GS-US-216-120','GS-US-216-121','GS-US-216-122','GS-US-216-123','GS-US-216-124','GS-US-236-0101','GS-US-236-0102','GS-US-236-0103','GS-US-236-0104','GS-US-236-0105','GS-US-236-0106','GS-US-236-0110','GS-US-183-0103','GS-US-183-0121','GS-US-236-0118']
# Xeljanz = ['A3921002','A3921003','A3921004','A3921005','A3921006','A3921010','A3921013','A3921014','A3921015','A3921019','A3921020','A3921024','A3921025','A3921028','A3921032','A3921033','A3921035','A3921036','A3921039','A3921040','A3921041','A3921044','A3921045','A3921046','A3921054','A3921056','A3921059','A3921064','A3921065','A3921068','A3921071','A3921073','A3921075','A3921076','A3921077','A3921109','A3921152']
# Zaltrap = ['ARD6122','ARD6123','ARD6772','EFC10261','EFC10262','EFC10547','EFC10668','EFC10688','EFC6125','EFC6546','POH0251','POH0253','POH0262','POH0263','POH0265','POH0274','PDY 6655','PDY6656','TCD10173','TCD6117','TCD6118','TCD6119','TCD6120','TCD6121','TED6113','TED6114','TED6115','TED6116','TES10897','TED10089']
# Zioptan = ['74450','74451','74452','74453','74457','74458','74460','77552','MK-2452-001','15001','15002','15003','15005','77550','77551','77553','MK-2452-002']



f=open('Missing.csv', 'rU')
csv_f = csv.reader(f)

for row in csv_f:
    if(row[0] != ""):
        allTrials.append(row)

listStr=sum(allTrials, [])

for indc1 in listStr:
    hash=indc1
    lengthStr=len(hash)
    for i in range(0,lengthStr):

       lengthStr=lengthStr-i
       hash1 = hash[:lengthStr] + '-' + hash[lengthStr:]
       alist3.append(hash1)

for indc2 in listStr:
    hash=indc2
    lengthStr=len(hash)
    for i in range(0,lengthStr):

       lengthStr=lengthStr-i
       hash1 = hash[:lengthStr] + '/' + hash[lengthStr:]
       alist3.append(hash1)



print(alist3)




list1 = [x.strip(' ') for x in alist3]
len1 = len(list1)-1
alist = [];
strURL1 = 'https://clinicaltrials.gov/ct2/results?term='
strURL2 = '&Search=Searchdisplayxml=true'
for indic1 in list1:


  strURL3 = strURL1 + indic1 + strURL2
#req = urllib.request.urlopen('https://clinicaltrials.gov/show/NCT01487096?displayxml=true')




  try:
    req = urllib.request.urlopen(strURL3)
    xml = bs4.BeautifulSoup(req, 'xml')
    for item in xml.findAll('search_results'):
     y=re.findall('<nct_id>(.*)</nct_id>',str(item))
     len2 = len(y)
     if y:
      alist.append(y)
      l = [indic1] * len2
      FDAOrg1.append(l)
      print (l)
     #print ("NCT IS: "+item.text)
    #for i in range(0,len1):
     #alist.append(item)
  except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
  else:

        print("Stage 1 processing ...")







final3=sum(FDAOrg1, [])
print(alist)

final=sum(alist, [])
print (final)

set = set(final)
result = list(set)
print(result)



strURL11 = 'https://clinicaltrials.gov/show/'
strURL21 = '?displayxml=true'

for indic11 in final:
 strURL31 = strURL11 + indic11 + strURL21


 try:


    req2 = urllib.request.urlopen(strURL31)
    xml = bs4.BeautifulSoup(req2, 'xml')
    for item in xml.findAll('id_info'):
       party = item.find('org_study_id')
       if party is None:
        OrgID.append("NULL")
       else:
        NewItem = party.text

    #for i in range(0,len1):
        OrgID.append(NewItem)
    for item in xml.findAll('id_info'):
      party = item.find('nct_id')
      if party is None:
        NCTID.append("NULL")
      else:
         NewItem = party.text

        #for i in range(0,len1):
         NCTID.append(NewItem)

    for item in xml.findAll('clinical_study'):
     party = item.find('brief_title')
     if party is None:
      Btitle.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      Btitle.append(NewItem)


    for item in xml.findAll('clinical_study'):
     party = item.find('overall_status')
     if party is None:
      OverallStatus.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      OverallStatus.append(NewItem)


    for item in xml.findAll('clinical_study'):
     party = item.find('condition')
     if party is None:
      condition.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      condition.append(NewItem)


     for item in xml.findAll('lead_sponsor'):
      party = item.find('agency')
      if party is None:
       agency.append("NULL")
      else:
       NewItem = party.text

    #for i in range(0,len1):
       agency.append(NewItem)


     for item in xml.findAll('eligibility'):
      party = item.find('gender')
      if party is None:
       gender.append("NULL")
      else:
       NewItem = party.text

    #for i in range(0,len1):
       gender.append(NewItem)




     for item in xml.findAll('eligibility'):
      party = item.find('minimum_age')
      if party is None:
       MAge.append("NULL")
      else:
       NewItem = party.text

    #for i in range(0,len1):
       MAge.append(NewItem)



     for item in xml.findAll('clinical_study'):
      party = item.find('phase')
      if party is None:
       Phase1.append("NULL")
      else:
       NewItem = party.text

    #for i in range(0,len1):
       Phase1.append(NewItem)



     for item in xml.findAll('lead_sponsor'):
      party = item.find('agency_class')
      if party is None:
       AgencyClass.append("NULL")
      else:
       NewItem = party.text

    #for i in range(0,len1):
       AgencyClass.append(NewItem)


     for item in xml.findAll('clinical_study'):
      party = item.find('study_type')
      if party is None:
       StudyType.append("NULL")
      else:
       NewItem = party.text
       StudyType.append(NewItem)




     for item in xml.findAll('clinical_study'):
      party = item.find('study_design')
      if party is None:
       StudyDesign.append("NULL")
      else:
       NewItem = party.text
       StudyDesign.append(NewItem)


     for item in xml.findAll('id_info'):
      party = item.find('secondary_id')
      if party is None:
       SecID.append("NULL")
      else:
       NewItem = party.text

    #for i in range(0,len1):
       SecID.append(NewItem)



     for item in xml.findAll('clinical_study'):
      party = item.find('firstreceived_date')
      if party is None:
       FirstRecv.append("NULL")
      else:
       NewItem = party.text

    #for i in range(0,len1):
       FirstRecv.append(NewItem)

     for item in xml.findAll('clinical_study'):
      party = item.find('start_date')
      if party is None:
       SDate.append("NULL")
      else:
       NewItem = party.text

    #for i in range(0,len1):
       SDate.append(NewItem)


    for item in xml.findAll('clinical_study'):
     party = item.find('completion_date')
     if party is None:
      ComplDate.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      ComplDate.append(NewItem)



    for item in xml.findAll('clinical_study'):
     party = item.find('lastchanged_date')
     if party is None:
      LastChangedDate.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      LastChangedDate.append(NewItem)



    for item in xml.findAll('clinical_study'):
     party = item.find('verification_date')
     if party is None:
      VerificationDate.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      VerificationDate.append(NewItem)

    for item in xml.findAll('clinical_study'):
     party = item.find('firstreceived_results_date')
     if party is None:
      FirstRecvResultDate.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      FirstRecvResultDate.append(NewItem)

    for item in xml.findAll('clinical_study'):
     party = item.find('firstreceived_results_disposition_date')
     if party is None:
      FirstRecvResultDispoDate.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      FirstRecvResultDispoDate.append(NewItem)




    for item in xml.findAll('clinical_study'):
     party = item.find('primary_completion_date')
     if party is None:
      PCD.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      PCD.append(NewItem)



    for item in xml.findAll('clinical_study'):
     party = item.find('location_countries')
     if party is None:
      Countries.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      Countries.append(NewItem)


    for item in xml.findAll('clinical_study'):
     party = item.find('condition')
     if party is None:
      Condition.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      Condition.append(NewItem)



    for item in xml.findAll('clinical_study'):
     party = item.find('is_fda_regulated')
     if party is None:
      IsFDA.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      IsFDA.append(NewItem)

    for item in xml.findAll('clinical_study'):
     party = item.find('acronym')
     if party is None:
      acronym.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      acronym.append(NewItem)



    for item in xml.findAll('clinical_study'):
     party = item.find('is_section_801')
     if party is None:
      Is801.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      Is801.append(NewItem)

    for item in xml.findAll('clinical_study'):
       y=re.findall('<intervention_name>(.*)</intervention_name>',str(item))
       if y:
        Intervention.append(y)
       else:
        Intervention.append("NULL")



 except URLError as e:
      if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
      elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
 else:



         print("Stage 2 processing ...")







f = open('cleaned.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('FDA Org ID','Org ID', 'NCT ID','Brief Title','Condition','Overall status','Intervention name','Acronym','Agency','Gender','Minimum Age','Phase','Agency class','Study type','Study Design','Secondary ID','First received','Start Date','Completion date','Last changed date','Verification date','First received result date','Certificate of Delay/ Disposition Date','PCD','Countries','IS FDA regulated','IS section 801'))
    #mylist = list(set(list01))
    #mylist1 = list(set(list02))
    #mylist2 = list(set(list03))
    #for i1 in list11:
    for i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20, i21, i22, i23,i24, i25, i26, i27 in zip(final3,OrgID, NCTID, Btitle,Condition, OverallStatus,Intervention, acronym, agency, gender, MAge, Phase1, AgencyClass, StudyType, StudyDesign, SecID, FirstRecv, SDate, ComplDate, LastChangedDate, VerificationDate, FirstRecvResultDate, FirstRecvResultDispoDate, PCD, Countries, IsFDA,Is801):

         writer.writerow( (i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23, i24, i25,i26,i27) )
finally:
    f.close()



f=open('cleaned.csv', 'rU')
csv_f = csv.reader(f)



month_dict = {'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

#for i in range(1, 13, 1):
#    next(csv_f, None)

name1 = input("What's the drug name? ")
name2 = input("What's another drug name? ")
name3 = input("What's the sponsor's name?(If nothing, please enter NULL) ")
name4 = input("Is there any other name for the sponsor(If not, please enter NULL)? ")




allTrials = []
first_stage_cleared = []
registered_trials = []
published_trials = []
reported_trials = []
timely_reported_trials = []
available_trials = []

for row in csv_f:
    if(row[1] != ""):
        allTrials.append(row)


print ("number of trials analyzed is " + str(len(allTrials)-1))

for row in allTrials:
    if (name1.lower() in str(row[6]).lower() or name2.lower() in str(row[6]).lower() or name3.lower() in str(row[8]).lower() or name4.lower() in str(row[8]).lower()):
        registered_trials.append(row)
print ("number of valid trials "+str(len(registered_trials)))
for row in registered_trials:
    print (row[1])


Stage2File = input(" What would like to name the Stage-2 output file as?(Eg: xyz.csv) ")


f = open(Stage2File, 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('FDA Org ID','Org ID', 'NCT ID','Brief Title','Condition','Overall status','Intervention','Acronym','Agency','Gender','Minimum Age','Phase','Agency class','Study Type','Study Design','Secondary ID','First received','Start Date','Completion date','Last changed date','Verification date','First received result date','Certificate of Delay/ Disposition Date','PCD','Countries','IS FDA regulated','IS section 801'))

    for i1 in (registered_trials):

         writer.writerow( (i1) )
finally:
    f.close()





#print(OrgID)






"""
alist3=[]


listStr=['39ed345','45dgf4']

for indc1 in listStr:
    hash=indc1
    lengthStr=len(hash)
    lengthStr=lengthStr-3
    hash1 = hash[:lengthStr] + '-' + hash[lengthStr:]
    alist3.append(hash1)

print(alist3)

"""
#hash = "355879ACB6"
#hash = hash[:4] + '-' + hash[4:]

"""
def insert_dash(string, index):

    lengthStr=len(string)
    lengthStr=lengthStr-index
    return string[:lengthStr] + '-' + string[lengthStr:]

print (insert_dash("355879ACB6", 3))
"""