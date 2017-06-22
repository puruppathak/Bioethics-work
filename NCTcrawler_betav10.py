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


# Your input Org IDs go here:
list1 = ['GO28141','GPO14821','NO25395','MEK4592g','GP28369','GP28370','GP28620','MEK4953g','MEK4954g','MEK4952g']
# Aubagio =  ['1001','1002','1024','1932','2001','ALI6504','BDR6639','BEQ10169','BEX6038','EFC10531','EFC6049','HWA486-1024','INT10563','INT10564','INT11697','INT11720','INT11932','INT6039','INT6040','LTS6047','LTS6048','LTS6050','PDY6045','PDY6046','PDY11684','PHM0086','PMH0091','POH0290','POH0295','POP11432','POP6505','POP6507','SIM0041','TDR10892','TES10852','EFC6058','EFC6260','EFC10891'];
# Bosulif = ['3160A4-200','3160A4-3000','3160A4-2203','3160A4-1109','3160A4-1115','3160A4-1120','3160A1-103','3160A4-1110','3160A1-100','3160A1-102','3160A4-1112','3160A4-105','3160A4-1111','3160A4-104','3160A4-1114','3160A4-1106','3160A4-1108','3160A6-2207','3160A4-2203']
# Alecensa = ['NP29040','NP28989','NP28990','NP29042','NP28991','NP28761','NP28673','BO28984','AF-001JP','AF-002JG']
# Bridion = ['P06042','P101','19.4.306','19.4.334','P07981','P105','19.4.301','19.4.302','19.4.310','19.4.303','P07982','19.4.110','19.4.112','19.4.113','19.4.114','19.4.115','19.4.116','19.4.313','19.4.316','19.4.318','19.4.324','P06101','19.4.328','19.4.333','19.4.335','P07025','P07044','P07038','19.4.319','19.4.101','19.4.102','19.4.105','19.4.106','19.4.107','19.4.108','19.4.109','19.4.201','19.4.202','19.4.203','19.4.204','19.4.205','19.4.206','19.4.207','19.4.208A','19.4.208B','19.4.209A','19.4.209B','19.4.210','19.4.304','19.4.305','19.4.308','19.4.309','19.4.311','19.4.312']
# Corlanor = ['CL1-001','CL1-002','CL1-003','CL1-004','CL1-005','CL1-007','CL1-008','CL1-024','CL1-027','CL1-029','CL1-033','CL1-036','CL1-038','CL1-039','CL1-040','CL1-041','CL1-042','CL1-043','CL1-048','CL1-049','CL1-055','CL2-002','CL2-006','CL2-009','CL2-010','CL2-011','CL2-012','CL2-013','CL2-014','CL2-015','CL2-026','CL2-028','CL2-030','CL2-044','CL2-045','CL2-047','CL2-050','CL2-052','CL2-054','CL2-061','CL2-062','CL2-073','CL2-16257-053','CL3-017','CL3-018','CL3-019','CL3-021','CL3-022','CL3-023','CL3-044','CL3-064','CL3-068','CL3-078','CL3-16257-056','CL3-16257-063','CL3-16257-067','CL3-16257-083','NP15364','PKH-001','PKH-002','PKH-003','PKH-004','PKH-005','PKH-006','PKH-007','PKH-008','PKH-009','PKH-010','PKH-012','PKH-013','PKH-014','PKH-015','PKH-017','CL3-057','CL2-060']
# Cotellic = ['GO28141','GPO14821','NO25395','MEK4592g','GP28369','GP28370','GP28620','MEK4953g','MEK4954g','MEK4952g']
# Daklinza = ['AI443014','AI443102','AI444218','AI444004','AI444005','AI444006','AI444008','AI444009','AI444010','AI444011','AI444012','AI444013','AI444014','AI444020','AI444021','AI444022','AI444024','AI444026','AI444027','AI444031','AI444032','AI444033','AI444034','AI444039','AI444040','AI444042','AI444044','AI444046','AI444052','AI444054','AI444063','AI444064','AI444065','AI444084','AI444099','AI444258','AI444237','AI444215','AI444216','AI446026','AI446028','AI446029','AI447007','AI447009','AI447011','AI447016','AI447017','AI447026','AI447027','AI447028','AI447029','AI447030','AI447031','AI447034','AI447040','AI447043','AI452017','TMC435HPC1005']
# Entresto = ['CLCZ696B2314','CLCZ696B2228','CLCZ696B2214','CLCZ696A2201','CLCZ696A2219','CLCZ696A2223','CLCZ696A1306','CLCZ696A2316','CLCZ696A2319','CLCZ696A2315','CLCZ696A2101','CLCZ696A2102','CLCZ696A1101','CLCZ696B2115','CLCZ696B2203','CLCZ696B2126','CLCZ696B2223','CLCZ696B2105','CLCZ696A2117','CLCZ696B2111','CLCZ696B2112','CLCZ696B2116','CLCZ696B2128','CLCZ696A2204','CLCZ696A2205','CLCZ696B2225','CLCZ696B2207','CLCZ696A2222','CLCZ696A2219E1','CLCZ696A1305','CLCZ696B2122','CLCZ696A2119','CLCZ696A2120','CLCZ696B2113','CLCZ696B2125','CLCZ696A2124','CLCZ696B2109','CLCZ696A2126','CLCZ696B2123','CLCZ696A2103','CLCZ696A2114','CLCZ696B2107','CLCZ696D2301','CLCZ696B2317','CLCZ696A2216','CLCZ696A2318','CLCZ696A2224','CLCZ696A2109']
# Farydak = ['CLBH589D2308','CLBH589B2207','CLBH589DUS71','CLBH589B2203','CLBH589E2214','CLBH589B2201','CLBH589B2202','CLBH589B2206','CLBH589B2211','CLBH589B2007','CLBH589A2101','CLBH589A2102','CLBH589B1101','CLBH589B1201','CLBH589B2101','CLBH589B2102','CLBH589B2108','CLBH589B2109','CLBH589B2110','CLBH589B2111','CLBH589X2101','CLBH589X2105','CLBH589B2105']
# Ibrance = ['A5481001','A5481002','A5481003','A5481004','A5481008','A5481009','A5481010','A5481011','A5481012','A5481013','A5481014','A5481015','A5481016','A5481017','A5481018','A5481020','A5481021','A5481022','A5481023','A5481026','A5481036','A5481038','A5481039','A5481040']
# Odomzo = ['CAMN107Y2101','CLDE225A1102','CLDE225A2108','CLDE225A2110','CLDE225A2112','CLDE225A2114','CLDE225A2201','CLDE225B2209','CLDE225C2301','CLDE225X1101','CLDE225X2101','CLDE225X2103','CLDE225X2104','CLDE225X2114','CLDE225X2116','CLDE225X2203','CLDE225XUS02T','CLDE225XUS03T','CAMN107Y2102','CLDE225XUS20']
# Tagrisso = ['D5160C00001','D5160C00002','D5160C00005','D5160C00006','D5160C00007','D5160C00008','D5160C00009','D5160C00010','D5160C00012','D5160C00013','D5160C00014','D5160C00019','D5160C00021','D5160C00003','D5160C00011']
# Tresiba = ['NN1045-3834','NN1050-4008','NN1250-1835','NN1250-1836','NN1250-1876','NN1250-1987','NN1250-1988','NN1250-1989','NN1250-1990','NN1250-1991','NN1250-1992','NN1250-1993','NN1250-1994','NN1250-1995','NN1250-1996','NN1250-1999','NN1250-3561','NN1250-3569','NN1250-3579','NN1250-3580','NN1250-3582','NN1250-3583','NN1250-3585','NN1250-3586','NN1250-3587','NN1250-3643','NN1250-3644','NN1250-3667','NN1250-3668','NN1250-3672','NN1250-3718','NN1250-3724','NN1250-3725','NN1250-3762','NN1250-3763','NN1250-3765','NN1250-3769','NN1250-3770','NN1250-3829','NN1250-3839','NN1250-3846','NN1250-3874','NN1250-3923','NN1250-3943','NN1250-3944','NN1250-3948','NN1250-3995','NN1250-3998','NN1250-3999','NN1250-4000','NN1250-4060','NN1250-4061','NN5401-1718','NN5401-1719','NN5401-1738','NN5401-1740','NN5401-1788','NN5401-1790','NN5401-1791','NN5401-1792','NN5401-1959','NN5401-1977','NN5401-1978','NN5401-1979','NN5401-1980','NN5401-1981','NN5401-1982','NN5401-1983','NN5401-1985','NN1250-3538','NN5401-3539','NN5401-3570','NN5401-3590','NN5401-3592','NN5401-3593','NN5401-3594','NN5401-3597','NN5401-3645','NN1250-3678','NN5401-3726','NN5401-3816','NN5401-3844','NN5401-3857','NN5401-3896','NN5401-3940','NN5401-3941','NN5401-3996','NN5401-4003','NN9068-3632','NN9068-3697','NN9068-3851','NN9068-3912','NN9068-3951','NN9068-3952','NN9068-4119','EX1250-4080']
# Yondelis = ['ET743-SAR-3007','ET743-STS-201','ET743-SAR-3002','ET-A-013-01','ET743-OVC-1001','ET743-OVC-1002','ET-B-005-98','ET-B-008-98','ET-B-017-99','10045030','ET-B-016-99','ET-B-028-06','ET-C-002-07','EORTC-62091','ET743-SAR-2005','ET-B-011-00','ET-B-020-99','ET743-SAR-3006','ET743-OVC-1003','10045020','ET-A-010-01','ET-A-002-95','ET743-OVA-1002','ET743-OVA-1003','ET-B-010-99','ET-A-006-00','ET743-USA-11','OVA-301']
# Zurampic =['RDEA594-101','RDEA594-102','RDEA594-103','RDEA594-104','RDEA594-105','RDEA594-106','RDEA594-107','RDEA594-108','RDEA594-109','RDEA594-110','RDEA594-111','RDEA594-112','RDEA594-113','RDEA549-114','RDEA594-115','RDEA594-116','RDEA594-117','RDEA594-118','RDEA594-120','RDEA594-121','RDEA594-122','RDEA594-123','RDEA594-125','RDEA594-126','RDEA594-127','RDEA594-128','RDEA594-129','RDEA594-130','RDEA594-131','RDEA594-132','RDEA594-201','RDEA594-202','RDEA594-203','RDEA594-203','RDEA594-204','RDEA594-301','RDEA594-302','RDEA594-303','RDEA594-304','RDEA594-305','RDEA594-306','RDEA594-307']

##

def ceil(n):   # This function is used for page number calculation.
    res = int(n)
    return res if res == n or n < 0 else res+1


list1 = [x.strip(' ') for x in list1]
len1 = len(list1)-1
alist = [];



strURL1 = 'https://clinicaltrials.gov/ct2/results?term='
strURL2 = '&Search=Searchdisplayxml=true'
for indic1 in list1:
  strURL = "https://clinicaltrials.gov/ct2/results?term=" + indic1 + "&displayxml=true"
  req = urlopen(strURL)
  root = ET.parse(req).getroot()
  search_count = int(root.attrib['count'])
  total_pages = ceil(search_count / 20)
  count = 1

  for i in range(1, total_pages + 1):
   strURL3 = "https://clinicaltrials.gov/ct2/results?term="+indic1+"&pg="+str(i)+"&displayxml=true"

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