# Web crawler designed to fetch data from the ClinicalTrials API using Python
# Algorithm coded and designed by Mr. Puru Pathak.
# This software is a property of Bioethics International. All rights reserved.
# Republication or redistribution of the software content is prohibited.
# Stage 1 software for ClinicalTrials.org


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



# Addyi
# flibanserin
# sprout
# valeant

# Your input Org IDs go here:
list1 = ['CL1-001','CL1-002','CL1-003','CL1-004','CL1-005','CL1-007','CL1-008','CL1-024','CL1-027','CL1-029','CL1-033','CL1-036','CL1-038','CL1-039','CL1-040','CL1-041','CL1-042','CL1-043','CL1-048','CL1-049','CL1-055','CL2-002','CL2-006','CL2-009','CL2-010','CL2-011','CL2-012','CL2-013','CL2-014','CL2-015','CL2-026','CL2-028','CL2-030','CL2-044','CL2-045','CL2-047','CL2-050','CL2-052','CL2-054','CL2-061','CL2-062','CL2-073','CL2-16257-053','CL3-017','CL3-018','CL3-019','CL3-021','CL3-022','CL3-023','CL3-044','CL3-064','CL3-068','CL3-078','CL3-16257-056','CL3-16257-063','CL3-16257-067','CL3-16257-083','NP15364','PKH-001','PKH-002','PKH-003','PKH-004','PKH-005','PKH-006','PKH-007','PKH-008','PKH-009','PKH-010','PKH-012','PKH-013','PKH-014','PKH-015','PKH-017']
# Aubagio =  ['1001','1002','1024','1932','2001','ALI6504','BDR6639','BEQ10169','BEX6038','EFC10531','EFC6049','HWA486-1024','INT10563','INT10564','INT11697','INT11720','INT11932','INT6039','INT6040','LTS6047','LTS6048','LTS6050','PDY6045','PDY6046','PDY11684','PHM0086','PMH0091','POH0290','POH0295','POP11432','POP6505','POP6507','SIM0041','TDR10892','TES10852','EFC6058','EFC6260','EFC10891'];
# Bosulif = ['3160A4-200','3160A4-3000','3160A4-2203','3160A4-1109','3160A4-1115','3160A4-1120','3160A1-103','3160A4-1110','3160A1-100','3160A1-102','3160A4-1112','3160A4-105','3160A4-1111','3160A4-104','3160A4-1114','3160A4-1106','3160A4-1108','3160A6-2207','3160A4-2203']
# Viberzi = ['IBS3001','IBS3002','IBS2001','EDI1002','CPS1009','EDI1001','EDI1003','CPS1005','CPS1007','CPS1011','CPS1012','CPS1008','CPS1006','CPS1010']
# Addyi = ['511.71','511.75','511.147','511.68','511.69','511.70','511.77','511.74','511.84','511.118','511.114','511.133','511.130','511.156','SPR-12-01','SPR-12-02','SPR-12-04','SPR-14-06','511.67','511.86','511.93','511.96','511.111','511.158','SPR-12-03','SPR-14-01','511.9O','U10-2254-01','511.88','511.87','SPR-12-05','511.121','511.144','511.151','511.73','511.85','511.106','511.21','511.44','511.37','511.1','511.2','511.15','511.26','511.105','511.117','511.146','511.3','511.11','511.12','SPR14-06','511.14','511.97']
# Alecensa = ['NP29040','NP28989','NP28990','NP29042','NP28991','NP28761','NP28673','BO28984','AF-001JP','NP28761']
# Avycaz = ['CXL-PK-01','CXL-PK-03','CXL-PK-04','CXL-PK-06','D4280C00001','D4280C00002','D4280C00004','D4280C00005','D4280C00006','D4280C00007','D4280C00008','D4280C00009','D4280C00010','D4280C00011','D4280C00012','D4280C00014','D4280C00018','D4280C00020','D4280C00023','D4281C00001','NXL104/1001','NXL104/1002','NXL104/1003','NXL104/1004','NXL104/2001','NXL104/2002']
# Bridion = ['P06042','P101','19.4.306','19.4.334','P07981','P105','19.4.301','19.4.302','19.4.310','19.4.303','P07982','19.4.110','19.4.112','19.4.113','19.4.114','19.4.115','19.4.116','19.4.313','19.4.316','19.4.318','19.4.324','P06101','19.4.328','19.4.333','19.4.335','P07025','P07044','P07038','INT00103441','19.4.319','19.4.101','19.4.102','19.4.105','19.4.106','19.4.107','19.4.108','19.4.109','19.4.201','19.4.202','19.4.203','19.4.204','19.4.205','19.4.206','19.4.207','19.4.208A','19.4.208B','19.4.209A','19.4.209B','19.4.210','19.4.304','19.4.305','19.4.308','19.4.309','19.4.311','19.4.312']
# Cotellic = ['GO28141','GPO14821','NO25395','MEK4592g','GP28369','GP28370','GP28620','MEK4953g','MEK4954g','MEK4952g']
# Farydak = ['CLBH589D2308','CLBH589B2207','CLBH589DUS71','CLBH589B2203','CLBH589E2214','CLBH589B2201','CLBH589B2202','CLBH589B2206','CLBH589B2211','CLBH589B2007','CLBH589A2101','CLBH589A2102','CLBH589B1101','CLBH589B1201','CLBH589B2101','CLBH589B2102','CLBH589B2108','CLBH589B2109','CLBH589B2110','CLBH589B2111','CLBH589X2101','CLBH589X2105','CLBH589B2105']
# Ibrance = ['A5481001','A5481002','A5481003','A5481004','A5481008','A5481009','A5481010','A5481011','A5481012','A5481013','A5481014','A5481015','A5481016','A5481017','A5481018','A5481020','A5481021','A5481022','A5481023','A5481026','A5481036','A5481038','A5481039','A5481040']
# Kybella = ['1403740','ATX-101-06-03','ATX-101-06-04','ATX-101-07-05','ATX-101-07-07','ATX-101-07-08','ATX-101-08-10','ATX-101-08-11','ATX-101-08-12','ATX-101-09-15','ATX-101-10-16','ATX-101-10-17','ATX-101-10-18','ATX-101-10-19','ATX-101-11-22','ATX-101-11-23','ATX-101-11-24','ATX-101-11-26','ATX-101-12-32','ATX-101-13-27','ATX-101-13-28','ATX-101-13-35','ATX-101-13-36','ATX-101-16-509','ATX-101-11-30','114253']
# Odomzo = ['CAMN107Y2101','CLDE225A1102','CLDE225A2108 ','CLDE225A2110','CLDE225A2112','CLDE225A2114','CLDE225A2201','CLDE225B2209','CLDE225C2301','CLDE225X1101','CLDE225X2101','CLDE225X2103','CLDE225X2104','CLDE225X2114','CLDE225X2116','CLDE225X2203','CLDE225XUS02T','CLDE225XUS03T','CAMN107Y2102','CLDE225XUS20']
# Tagrisso = ['D5160C00001','D5160C00002','D5160C00005','D5160C00006','D5160C00007','D5160C00008','D5160C00009','D5160C00010','D5160C00012','D5160C00013','D5160C00014','D5160C00019','D5160C00021','D5160C00003','D5160C00011']
# ['01-016','ACT6011','ACT12374','BDR10880','BDR11038','BDR11540','BDR11578','BDR12546','BDR12547','BDR6864','BDR6884','BEQ11094','DRI6012','DRI6014','DRI6018','DRI6019','EFC10743','EFC10780','EFC10781','EFC10887','EFC11319','EFC11321','EFC11476','EFC12261','EFC12626','EFC12382','EFC12703','EFC12832','EFC6014','EFC6015','EFC6016','EFC6017','EFC6018','EFC60182','EFC6019','INT10408','INT10409','INT10782','INT10783','INT6052','INT6863','LTS10888','LTS12809','PDY10433','PDY10931','PDY11431','PDY11824','PDY11941','PDY12545','PDY12625','PDY6797','PKD11475','PKD12406','PMH0050','PMH0051','PMR 3102-1','POH0182','POH0268','POH0343','POH0347','POH0348','POH0398','POH0410','POH0384','POP11320','POP11814','POP6053','SYF13476','TDR11215','TDR14311','TDU10121','TES11807','TES6865','EXSCEL','LEADER']
# Zurampic = ['RDEA594-101','RDEA594-102','RDEA594-103','RDEA594-104','RDEA594-105','RDEA594-106','RDEA594-107','RDEA594-108','RDEA594-109','RDEA594-110','RDEA594-111','RDEA594-112','RDEA594-113','RDEA549-114','RDEA594-115','RDEA594-116','RDEA594-117','RDEA594-118','RDEA594-120','RDEA594-121','RDEA594-122','RDEA594-123','RDEA594-125','RDEA594-126','RDEA594-127','RDEA594-128','RDEA594-129','RDEA594-130','RDEA594-131','RDEA594-132','RDEA594-201','RDEA594-202','RDEA594-203','RDEA594-204','RDEA594-301','RDEA594-302','RDEA594-303','RDEA594-304','RDEA594-305','RDEA594-306','RDEA594-307']
# Yondelis = ['ET743-SAR-3007','ET743-STS-201','ET743-SAR-3002','ET-A-013-01','ET743-OVC-1001','ET743-OVC-1002','ET-B-005-98','ET-B-008-98','ET-B-017-99','10045030','ET-B-016-99','ET-B-028-06','ET-C-002-07','EORTC-62091','ET743-SAR-2005','ET-B-011-00','ET-B-020-99','ET743-SAR-3006','ET743-OVC-1003','10045020','ET-A-010-01','ET-A-002-95','ET743-OVA-1002','ET743-OVA-1003','ET-B-010-99','ET-A-006-00','ET743-USA-11','OVA-301']
# Entresto = ['CLCZ696B2314','CLCZ696B2228','CLCZ696B2214','CLCZ696A2201','CLCZ696A2219','CLCZ696A2223','CLCZ696A1306','CLCZ696A2316','CLCZ696A2319','CLCZ696A2315','CLCZ696A2101','CLCZ696A2102','CLCZ696A1101','CLCZ696B2115','CLCZ696B2203','CLCZ696B2126','CLCZ696B2223','CLCZ696B2105','CLCZ696A2117','CLCZ696B2111','CLCZ696B2112','CLCZ696B2116','CLCZ696B2128','CLCZ696A2204','CLCZ696A2205','CLCZ696B2225','CLCZ696B2207','CLCZ696A2222','CLCZ696A2219E1','CLCZ696A1305','CLCZ696B2122','CLCZ696A2119','CLCZ696A2120','CLCZ696B2113','CLCZ696B2125','CLCZ696A2124','CLCZ696B2109','CLCZ696A2126','CLCZ696B2123','CLCZ696A2103','CLCZ696A2114','CLCZ696B2107','CLCZ696D2301','CLCZ696B2317','CLCZ696A2216','CLCZ696A2318','CLCZ696A2224','CLCZ696A2109']
# Daklinza = ['AI443014','AI443102','AI444218','AI444004','AI444005','AI444006','AI444008','AI444009','AI444010','AI444011','AI444012','AI444013','AI444014','AI444020','AI444021','AI444022','AI444024','AI444026','AI444027','AI444031','AI444032','AI444033','AI444034','AI444039','AI444040','AI444042','AI444044','AI444046','AI444052','AI444054','AI444063','AI444064','AI444065','AI444084','AI444099','AI444258','AI444237','AI444215','AI444216','AI446026','AI446028','AI446029','AI447007','AI447009','AI447011','AI447016','AI447017','AI447026','AI447027','AI447028','AI447029','AI447030','AI447031','AI447034','AI447040','AI447043','AI452017','TMC435HPC1005']
# Corlanor = ['CL1-001','CL1-002','CL1-003','CL1-004','CL1-005','CL1-007','CL1-008','CL1-024','CL1-027','CL1-029','CL1-033','CL1-036','CL1-038','CL1-039','CL1-040','CL1-041','CL1-042','CL1-043','CL1-048','CL1-049','CL1-055','CL2-002','CL2-006','CL2-009','CL2-010','CL2-011','CL2-012','CL2-013','CL2-014','CL2-015','CL2-026','CL2-028','CL2-030','CL2-044','CL2-045','CL2-047','CL2-050','CL2-052','CL2-054','CL2-061','CL2-062','CL2-073','CL2-16257-053','CL3-017','CL3-018','CL3-019','CL3-021','CL3-022','CL3-023','CL3-044','CL3-064','CL3-068','CL3-078','CL3-16257-056','CL3-16257-063','CL3-16257-067','CL3-16257-083','NP15364','PKH-001','PKH-002','PKH-003','PKH-004','PKH-005','PKH-006','PKH-007','PKH-008','PKH-009','PKH-010','PKH-012','PKH-013','PKH-014','PKH-015','PKH-017']

#list1 = [x.strip(' ') for x in list1]
len1 = len(list1)-1
alist = [];
strURL1 = 'https://clinicaltrials.gov/ct2/results?term='
strURL2 = '&Search=Searchdisplayxml=true'


# ['NCT00134563','NCT00228163','NCT00475865','NCT00489489','NCT00622700','NCT00751881','NCT00803049','NCT00811395','NCT00883337','NCT01252355','NCT01487096','NCT00261846','NCT00811070','NCT00574873','NCT00195260','NCT00097357','NCT00643201','NCT00412984','NCT00313300','NCT00831441','NCT00457002','NCT00633893','NCT00496769','NCT00376168','NCT00712348','NCT00705939','NCT00962260','NCT01132690','NCT00636610','NCT00739661','NCT00968981','NCT00959647','NCT01209143','NCT01160250','NCT00833417','NCT01174264','NCT00447005','NCT00569946','NCT00094055','NCT00282048','NCT00678392','NCT00835978','NCT00094107','NCT00076011','NCT00094094','NCT00134719','NCT00127855','NCT00129116','NCT00129129','NCT00359983','NCT00614614','NCT00289783','NCT00345579','NCT00345683','NCT00545688','NCT00976989','NCT00058552','NCT01674062','NCT00058539','NCT02004093','NCT00063154','NCT00096993','NCT00567190','NCT01600963','NCT00910871','NCT00449644','NCT00523926','NCT00910806','NCT01287598','NCT00934882','NCT01003015','NCT01096030','NCT01103323','NCT00960258','NCT01318265','NCT01339104','NCT00664326','NCT00892437','NCT00869557','NCT01108510','NCT00708162','NCT01106586','NCT00445146','NCT01363011','NCT00298350','NCT01095796','NCT00413660','NCT00847613','NCT00814307','NCT00856544','NCT00147498','NCT00603512','NCT00687193','NCT00661661','NCT00413699','NCT00976599','NCT01164579','NCT00853385','NCT00550446','NCT01059864','NCT00960440',' NCT00561470','NCT00851084','NCT00574275','NCT00327444','NCT00532155','NCT00519285','NCT00327171','NCT00284141','NCT00396591','NCT00918346','NCT01087671','NCT01026831']

final=['NCT00134563','NCT00228163','NCT00475865','NCT00489489','NCT00622700','NCT00751881','NCT00803049','NCT00811395','NCT00883337','NCT01252355','NCT01487096','NCT00261846','NCT00811070','NCT00574873','NCT00195260','NCT00097357','NCT00643201','NCT00412984','NCT00313300','NCT00831441','NCT00457002','NCT00633893','NCT00496769','NCT00376168','NCT00712348','NCT00705939','NCT00962260','NCT01132690','NCT00636610','NCT00739661','NCT00968981','NCT00959647','NCT01209143','NCT01160250','NCT00833417','NCT01174264','NCT00447005','NCT00569946','NCT00094055','NCT00282048','NCT00678392','NCT00835978','NCT00094107','NCT00076011','NCT00094094','NCT00134719','NCT00127855','NCT00129116','NCT00129129','NCT00359983','NCT00614614','NCT00289783','NCT00345579','NCT00345683','NCT00545688','NCT00976989','NCT00058552','NCT01674062','NCT00058539','NCT02004093','NCT00063154','NCT00096993','NCT00567190','NCT01600963','NCT00910871','NCT00449644','NCT00523926','NCT00910806','NCT01287598','NCT00934882','NCT01003015','NCT01096030','NCT01103323','NCT00960258','NCT01318265','NCT01339104','NCT00664326','NCT00892437','NCT00869557','NCT01108510','NCT00708162','NCT01106586','NCT00445146','NCT01363011','NCT00298350','NCT01095796','NCT00413660','NCT00847613','NCT00814307','NCT00856544','NCT00147498','NCT00603512','NCT00687193','NCT00661661','NCT00413699','NCT00976599','NCT01164579','NCT00853385','NCT00550446','NCT01059864','NCT00960440',' NCT00561470','NCT00851084','NCT00574275','NCT00327444','NCT00532155','NCT00519285','NCT00327171','NCT00284141','NCT00396591','NCT00918346','NCT01087671','NCT01026831']
print(final)
set = set(final)
result = list(set)


strURL11 = 'https://clinicaltrials.gov/show/'
strURL21 = '?displayxml=true'

for indic11 in final:
 strURL31 = strURL11 + indic11 + strURL21

 #  https://clinicaltrials.gov/show/NCT01267084?displayxml=true

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
     party = item.find('enrollment')
     if party is None:
      acronym.append("NULL")
     else:
      NewItem = party.text

    #for i in range(0,len1):
      enrollment.append(NewItem)




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
f = open('NCT_data.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('NCT ID','Brief Title','Condition','Overall status','Enrollment','Intervention name','Acronym','Agency','Gender','Minimum Age','Phase','Agency class','Study type','Study Design','Secondary ID','First received','Start Date','Completion date','Last changed date','Verification date','First received result date','Certificate of Delay/ Disposition Date','PCD','Countries','Removed countries','IS FDA regulated','IS section 801'))
    #mylist = list(set(list01))
    #mylist1 = list(set(list02))
    #mylist2 = list(set(list03))
    #for i1 in list11:
    for i2,i222,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20, i21, i22, i23,i24, i25, i26, i27 in zip(NCTID, Btitle,Condition, OverallStatus,enrollment,Intervention, acronym, agency, gender, MAge, Phase1, AgencyClass, StudyType, StudyDesign, SecID, FirstRecv, SDate, ComplDate, LastChangedDate, VerificationDate, FirstRecvResultDate, FirstRecvResultDispoDate, PCD, Countries, Rm_Countries, IsFDA,Is801):

         writer.writerow( ( i2,i222, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23, i24, i25,i26, i27) )
finally:
    f.close()
