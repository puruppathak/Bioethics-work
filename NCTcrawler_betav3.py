import csv

__author__ = 'puruppathak'
from itertools import filterfalse, zip_longest
import csv
from random import choice
import sys
import bs4
import lxml
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError
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
acronym=[]
FirstRecvResultDispoDate=[]
str12="NULL"

list1 = ['1001','1002','1024','1932','2001','ALI6504','BDR6639','BEQ10169','BEX6038','EFC10531','EFC6049','HWA486-1024','INT10563','INT10564','INT11697','INT11720','INT11932','INT6039','INT6040','LTS6047','LTS6048','LTS6050','PDY6045','PDY6046','PDY11684','PHM0086','PMH0091','PMH0091','POH0290','POH0295','POP11432','POP6505','POP6507','SIM0041','TDR10892','TES10852','EFC6058','EFC6260','EFC10891'];

#'ALI6504','BDR6639','BEQ10169','BEX6038','EFC10531','EFC6049',' HWA486-1024','INT10563','INT10564','INT11697','INT11720','INT11932','INT6039','INT6040','LTS6047','LTS6048','LTS6050','PDY6045','PDY6046','PDY11684'
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
     party = item.find('nct_id')
     if party is None:
      alist.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      alist.append(NewItem)
  except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
  else:

        print("Good:stage 1")








print(alist)
strURL11 = 'https://clinicaltrials.gov/show/'
strURL21 = '?displayxml=true'

for indic11 in alist:
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

 except URLError as e:
      if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
      elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
 else:

   print("Stage 2")

         #print("Stage 2")










print(OrgID)
f = open('Aubagio.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('Org ID', 'NCT ID','Brief Title','Condition','Overall status','Acronym','Agency','Gender','Minimum Age','Phase','Agency class','Study type','Study Design','Secondary ID','First received','Start Date','Completion date','Last changed date','Verification date','First received result date','Certificate of Delay/ Disposition Date','PCD','Countries','IS FDA regulated','IS section 801'))
    #mylist = list(set(list01))
    #mylist1 = list(set(list02))
    #mylist2 = list(set(list03))
    #for i1 in list11:
    for i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20, i21, i22, i23,i24, i25 in zip(OrgID, NCTID, Btitle,Condition, OverallStatus,acronym, agency, gender, MAge, Phase1, AgencyClass, StudyType, StudyDesign, SecID, FirstRecv, SDate, ComplDate, LastChangedDate, VerificationDate, FirstRecvResultDate, FirstRecvResultDispoDate, PCD, Countries, IsFDA,Is801):

         writer.writerow( (i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23, i24, i25) )
finally:
    f.close()

