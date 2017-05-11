


import enchant
import ast
import re
import csv
#txt = "VER001-12 was a Phase 1 study of the safety, tolerability and pharmacokinetics of dalbavancin in individuals with impaired hepatic function. In this study individuals received a 1000 mg IV dose of dalbavancin on Day 1, and a 500 mg IV dose on Day 8. Subjects were housed in the site’s Phase 1 clinical trials unit on Days -1 through completion of all assessments on Day 2 (i.e., 2 nights). Subjects did not stay overnight in the unit subsequent to the second dose. Subjects were to return periodically at scheduled visits for examination, solicitation of adverse events, and phlebotomy for pharmacokinetic data and laboratory safety testing, including serum chemistry.An integral part of the study was the inclusion of a control group of individuals with normal hepatic function. Subject 12001004 was a 43 year old male who served as a healthy control. On screening, he reported no significant past medical history. His only recent prior medication was Alka-Seltzer Plus for symptoms of an upper respiratory infection. This individual was noted to have abnormal tests of hepatic function as part of his Day 60 laboratory data, including an ALT value of 2525 IU/L. Unfortunately this was not initially noted to be abnormal, as the site mistakenly thought these data were from a hepatically impaired subject and therefore not unusual."

f = open("123.txt")
filetext=f.read()

IDs=[]
IDlist=[]
Sentence=[]
Phase=[]
define_words = 'study'
wrong=[]
correct=[]

tuples = re.findall(r"([^.]*?%s[^.]*\.)" % define_words,filetext)
for tuple in tuples:
 if len(tuple)>5:
  Sentence.append(tuple)
  tuple1 = re.findall(r'[A-Z0-9-]+',str(tuple))
  #tuple11 = re.findall(r'Phase [0-9]+', str(tuple))



for line in Sentence:
  tuple111 = re.findall(r'[A-Z0-9-]+',str(line))
  if (tuple111 and len(tuple111)>4):
   IDlist.append(tuple111)
  else:
   IDlist.append("NULL")


# To generate individual IDs

for line in Sentence:
  IDtuple = re.findall(r'[A-Z0-9-]+',str(line))
  for tuple in IDtuple:
      if len(tuple) >4:
       IDs.append(tuple)



for line in Sentence:
  tuple11 = re.findall(r'Phase [0-9]+',str(line))
  if tuple11:
   Phase.append(tuple11)
  else:
   Phase.append("NULL")


def nested_remove(L, x):
    if x in L:
        L.remove(x)
    else:
        for element in L:
            if type(element) is list:
                nested_remove(element, x)


for item in IDlist:
 for item1 in item:
  #print(item1)
  if len(item1)<4:
   nested_remove(IDlist,str(item1))



d = enchant.Dict("en_US")

AllIDs = list(set(IDs))





for ID in AllIDs:
 if d.check(ID) == True:
    wrong.append(ID)

 elif d.check(ID) == False:
    correct.append(ID)


print(IDs)

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


# Your input Org IDs go here:
list1 = ['1001','1002','1024','1932','2001','ALI6504','BDR6639','BEQ10169','BEX6038','EFC10531','EFC6049','HWA486-1024','INT10563','INT10564','INT11697','INT11720','INT11932','INT6039','INT6040','LTS6047','LTS6048','LTS6050','PDY6045','PDY6046','PDY11684','PHM0086','PMH0091','POH0290','POH0295','POP11432','POP6505','POP6507','SIM0041','TDR10892','TES10852','EFC6058','EFC6260','EFC10891'];
# Aubagio =  ['1001','1002','1024','1932','2001','ALI6504','BDR6639','BEQ10169','BEX6038','EFC10531','EFC6049','HWA486-1024','INT10563','INT10564','INT11697','INT11720','INT11932','INT6039','INT6040','LTS6047','LTS6048','LTS6050','PDY6045','PDY6046','PDY11684','PHM0086','PMH0091','POH0290','POH0295','POP11432','POP6505','POP6507','SIM0041','TDR10892','TES10852','EFC6058','EFC6260','EFC10891'];
# Bosulif = ['3160A4-200','3160A4-3000','3160A4-2203','3160A4-1109','3160A4-1115','3160A4-1120','3160A1-103','3160A4-1110','3160A1-100','3160A1-102','3160A4-1112','3160A4-105','3160A4-1111','3160A4-104','3160A4-1114','3160A4-1106','3160A4-1108','3160A6-2207','3160A4-2203']




list1 = [x.strip(' ') for x in list1]
len1 = len(list1)-1
alist = [];
strURL1 = 'https://clinicaltrials.gov/ct2/results?term='
strURL2 = '&Search=Searchdisplayxml=true'
for indic1 in correct:


  strURL3 = strURL1 + indic1 + strURL2
#req = urllib.request.urlopen('https://clinicaltrials.gov/show/NCT01487096?displayxml=true')




  try:
    #FDAOrg1.append(indic1)
    req = urllib.request.urlopen(strURL3)
    xml = bs4.BeautifulSoup(req, 'xml')
    for item in xml.findAll('search_results'):
     y=re.findall('<nct_id>(.*)</nct_id>',str(item))
     len2 = len(y)
     print(len2)
     #y1=re.findall('<query>[^ ]* (.*)</query>',str(item))
     #FDAOrg1.append(item)*len2
     if y:
      alist.append(y)
      #final3=sum(FDAOrg1, [])
      #FDAOrg1.append(item)
      l = [indic1] * len2
      FDAOrg1.append(l)
      print (l)
      #FDAOrg1.append(y1)
      #FDAOrg.append(indic1)
     else:
         y1=re.findall('<query>[^ ]* (.*)</query>',str(item))
         if y1:
          alist2.append(y1)
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

final2=sum(alist2, [])
#final3=sum(FDAOrg1, [])
#print(final3)


final=sum(alist, [])
print(final)
set = set(final)
result = list(set)


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
     party = item.find('removed_countries')
     if party is None:
      Rm_Countries.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      Rm_Countries.append(NewItem)



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



         print("Stage 2 processing..")



print(FDAOrg1)
f = open('Full_temp_data.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('FDA Org','Org ID', 'NCT ID','Brief Title','Condition','Overall status','Intervention name','Acronym','Agency','Gender','Minimum Age','Phase','Agency class','Study type','Study Design','Secondary ID','First received','Start Date','Completion date','Last changed date','Verification date','First received result date','Certificate of Delay/ Disposition Date','PCD','Countries','Removed countries','IS FDA regulated','IS section 801'))
    #mylist = list(set(list01))
    #mylist1 = list(set(list02))
    #mylist2 = list(set(list03))
    #for i1 in list11:
    for i1,i111,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20, i21, i22, i23,i24, i25, i26, i27 in zip(final3,OrgID, NCTID, Btitle,Condition, OverallStatus,Intervention, acronym, agency, gender, MAge, Phase1, AgencyClass, StudyType, StudyDesign, SecID, FirstRecv, SDate, ComplDate, LastChangedDate, VerificationDate, FirstRecvResultDate, FirstRecvResultDispoDate, PCD, Countries, Rm_Countries, IsFDA,Is801):

         writer.writerow( (i1,i111, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23, i24, i25,i26, i27) )
finally:
    f.close()

# Writing faulty ID file:

with open('Missing.csv', 'w') as f:
    writer = csv.writer(f)
    for val in final2:
        writer.writerow([val])

f=open('Full_temp_data.csv', 'rU')
csv_f = csv.reader(f)



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





Stage1File = input("What would like to name the output file as?(Eg: xyz.csv) ")


f = open(Stage1File, 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('FDA Org','Org ID', 'NCT ID','Brief Title','Condition','Overall status','Intervention','Acronym','Agency','Gender','Minimum Age','Phase','Agency class','Study Type','Study Design','Secondary ID','First received','Start Date','Completion date','Last changed date','Verification date','First received result date','Certificate of Delay/ Disposition Date','PCD','Countries','IS FDA regulated','IS section 801'))

    for i1 in (registered_trials):

         writer.writerow( (i1) )
finally:
    f.close()

