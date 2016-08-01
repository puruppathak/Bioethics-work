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
Intervention=[]
acronym=[]
alist2=[]
FDAOrg=[]
Rm_Countries=[]
FirstRecvResultDispoDate=[]


# Your input Org IDs go here:
list1 = ['1001','1002','1024','1932','2001','ALI6504','BDR6639','BEQ10169','BEX6038','EFC10531','EFC6049','HWA486-1024','INT 10564','INT10563','INT10564','INT11697','INT11720','INT11932','INT6039','INT6040','LTS6047','LTS6048','LTS6050','PDY6045','PDY6046','PDY11684','PHM0086','PMH0091','POH0290','POH0295','POP11432','POP6505','POP6507','SIM0041','TDR10892','TES10852','EFC6058','EFC6260','EFC10891']
# Aubagio =  ['1001','1002','1024','1932','2001','ALI6504','BDR6639','BEQ10169','BEX6038','EFC10531','EFC6049','HWA486-1024','INT10563','INT10564','INT11697','INT11720','INT11932','INT6039','INT6040','LTS6047','LTS6048','LTS6050','PDY6045','PDY6046','PDY11684','PHM0086','PMH0091','POH0290','POH0295','POP11432','POP6505','POP6507','SIM0041','TDR10892','TES10852','EFC6058','EFC6260','EFC10891'];
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
# Odomzo = ['CAMN107Y2101','CLDE225A1102','CLDE225A2108','CLDE225A2110','CLDE225A2112','CLDE225A2114','CLDE225A2201','CLDE225B2209','CLDE225C2301','CLDE225X1101','CLDE225X2101','CLDE225X2103','CLDE225X2104','CLDE225X2114','CLDE225X2116','CLDE225X2203','CLDE225XUS02T','CLDE225XUS03T','CAMN107Y2102','CLDE225XUS20']
# Belsomra = ['P001','P002','P003','P004','P005','P006','P007','P008','P009','P010','P011','P012','P013','P015','P016','P017','P018','P020','P021','P022','P023','P024','P025','P026','P027','P028','P029','P032','P035','P036','P038','P039','P040','P041','P042','P055','P056']
# Cerdelga = ['GZGD02507','GZGD02607','GZGD00304','GZGD03109','GZGD03811','GZGD00404','GZGD00103','GZGD00204','GZGD02107','GZGD01707','GZGD01807','GZGD02007','GZGD02407','GZGD01907','GZGD03610','GZGD04112','GZGD02707','GZGD03310','GZGD08311','GZGD01708','GZGD02807']
# Dalvance = ['VER001-4','VER001-5','VER001-11','VER001-8','VER001-9','VER001-16','DUR001-301','DUR001-302','VER001-1','VER001-2','VER001-3','VER001-10','VER001-12','VER001-13','VER001-15','VER001-19','A8841004','DUR001-101','DUR001-102','DUR001-103','DUR001-104','VER001-06','']
# Esbriet = ['PIPF-016','PIPF-004','PIPF-006','SP3','Marnac Study 96-06','Raghu','PIPF-001','97-HG-0085','SP2','PIPF-005','PIPF-007','PIPF-008','PIPF-009','PIPF-010','PIPF-011','PIPF-002','PIPF-012','PIPF-003','PIPF-017','Study 031']
# Farxiga = ['D1690C00001','D1690C00004','D1690C00005','D1690C00006','D1690C00010','D1690C00012','D1690C00016','D1690C00017','D1690C00018','D1690C00019','D1691C00003','D1692C00002','D1692C00005','D1692C00006','D1692C00012','D1693C00001','D1693C00002','D1693C00005','MB102001','MB102002','MB102003','MB102004','MB102005','MB102006','MB102007','MB102008','MB102009','MB102010','MB102013','MB102014','MB102016','MB102017','MB102019','MB102020','MB102021','MB102025','MB102026','MB102027','MB102029','MB102030','MB102032','MB102034','MB102035','MB102036','MB102037','MB102045','MB102049','MB102054','MB102055','MB102057','MB102058','MB102059','MB102062','MB102066','MB102072','MB102073','MB102074','MB102077','MB102088','MB102090','MB102091','MB102093','MB102104']
# Harvoni = ['CO-US-337-0116','CO-US-337-0117','CO-US-337-1116','GS-US-169-015','GS-US-248-0102','GS-US-248-0104','GS-US-248-0117','GS-US-248-0120','GS-US-248-0121','GS-US-248-0122','GS-US-248-0123','GS-US-248-0124','GS-US-248-0125','GS-US-248-0131','GS-US-248-0132','GS-US-256-0101','GS-US-256-0102','GS-US-256-0108','GS-US-256-0110','GS-US-256-0124','GS-US-256-0129','GS-US-256-0148','GS-US-334-0101','GS-US-334-0107','GS-US-334-0108','GS-US-334-0110','GS-US-334-0111','GS-US-334-0124','GS-US-334-0126','GS-US-334-0146','GS-US-337-0101','GS-US-337-0102','GS-US-337-0108','GS-US-337-0109','GS-US-337-0113','GS-US-337-0115','GS-US-337-0118','GS-US-337-0121','GS-US-337-0122','GS-US-337-0123','GS-US-337-0124','GS-US-337-0125','GS-US-337-0127','GS-US-337-0128','GS-US-337-0131','GS-US-337-0133','GS-US-337-1116','GS-US-337-1118','GS-US-344-0101','GS-US-344-0102','GS-US-344-0108','GS-US-344-0109','P2938-0212','P2938-0515','P7977-0111','P7977-0221','P7977-0312','P7977-0422','P7977-0523','P7977-0613','P7977-0724','P7977-0915','P7977-1231','P7977-1318','P7977-1819','P7977-2025','NIAID-13-I-0159','BP-US-337-1115']
# Invokamet = ['DIA2001','DIA2003','DIA3006','DIA3009','DIA3002','DIA3012','DIA3015','DIA3008','DIA3010','DIA3014','DIA1046','DIA1050','DIA1051','DIA1038','DIA3004','DIA3011','DIA1056','DIA4002','DIA1036','DIA1037','DIA1032','DIA1001','DIA1002','DIA1003','DIA1007','DIA1008','DIA1019','DIA1023','DIA1030','TA7284-02','OBE2001','DIA3005','TA-7284-05','TA-7284-06','TA-7284-07','TA-7284-08','TA-7284-10','NAP1004','NAP1002','DIA1028','DIA1045','DIA1047']
# Jublia = ['DPSI-IDP-108-P1-03','DPSI-IDP-108-P1-02','DPSI-IDP-108-P1-01','DPSI-IDP-108-P1-04','DPSI-IDP-108-P2-01','DPSI-IDP-108-P3-01','DPSI-IDP-108-P3-02','KP-103-02','KP-103-03']
# Movantik = ['D3820C00004','D3820C00005','D3820C00007','D3820C00008','07-IN-NX003a','D3820C00006','D3820C00018','D3820C00025','D3820C00020','D3820C00012','D3820C00009','D3820C00010','D3820C00032','D3820C00011','D3820C00015','05-IN-OX001','08-PNL-04','D3820C00014','07-IN-NX002','D3820C00001']
# Otezla = ['CC-10004-PSA-001','CC-10004-PSA-002','CC-10004-PSA-003','CC-10004-PSA-004','CC-10004-PSA-005','CC-10004-PSOR-001','CC-10004-PSOR-003','CC-10004-PSOR-004','RA-002','BCT-001','ASTH-001','CC-10004-RA-001','CC-10004-BA-001','CC-10004-BA-002','CC-10004-PK-001','CC-10004-PK-007','CC-10004-PK-002','CC-10004-CP-012','CC-10004-CP-022','CC-10004-PK-005','CC-10004-CP-025','CC-10004-CP-020','CC-10004-PK-010','CC-10004-CP-011','CC-10004-CP-019','CC-10004-CP-018','CC-10004-CP-024','CC-10004-PK-008','CC-10004-PSOR-005','CC-10004-PSOR-008','CC-10004-PSOR-009','PSOR-005-E-LTE','RA-005','PSOR-005-E']
# Sivextro = ['TR701-101','TR701-102','TR701-103','TR701-105','TR701-106','TR701-107','TR701-108','TR701-109','TR701-110','TR701-111','TR701-114','TR701-115','TR701-119','TR701-123','TR701-124','TR701-104','TR701-126','TR701-112','TR701-113','16101','16102']
# Xigduo XR = ['MB102092','MB102100','MB102060','MB102065','MB102071','MB102034','MB102021','MB102014','D1690C00004','D1690C00012','D1690C00006','D1690C00010','D1690C00018','D1690C00019','MB102073','MB102077','MB102013','MB102055','D1691C00007','D1693C00005','MB102091','MB102129','CV181168','CV181169','D1693C00001','MB102026','']
# Xtoro = ['C-10-007','C-10-022','C-10-018','C-10-019','C-13-026']
# Zerbaxa = ['CXA-101-01','CXA-201-01','CXA-ELF-10-03','CXA-MD-11-07','CXA-101-02','CXA-201-02','CXA-REN-11-01','CXA-DDI-12-10','CXA-QT-10-02','CXA-101-03','CXA-IAI-10-01','CXA-cUTI-10-04','CXA-cIAI-10-09','CXA-NP-11-08','']
# Zontivity = ['P04737','P04736','P05185','P05183','P03462','P03449','P03450','P07969','P03448','P06453','P03447','P06452','P03464','P03465','P03629','P03458','P06560','P04132','P05361','P06558','P03445','P07045','P03454','P06559','P05005','P04772','P03573','P04637']
# Zydelig = ['101-01','101-05','101-06','313-0111','313-0117','313-0126','313-0130','339-0101','101-02','101-07','101-08','101-09','101-11','312-0116','101-04','313-0112','313-0118','312-0115','312-0117','312-0119','313-0124','313-0125','101-10','101-99']
# Zykadia = ['X2101','X1101','A2201','A2203','A2303','X2102','A2301','A2402','X2103','A2105','A2101','A2104','A2106']
# Viekira = ['Human factor study','M10-687','M10-749','M10-798','M11-030','M11-388','M11-389','M11-602','M11-603','M11-646','M11-652','M12-024','M12-116','M12-186','M12-187','M12-189','M12-193','M12-196','M12-198','M12-199','M12-200','M12-201','M12-202','M12-204','M12-205','M12-215','M12-221','M12-536','M12-680','M12-683','M12-746','M12-997','M12-998','M12-999','M13-013','M13-098','M13-099','M13-100','M13-102','M13-103','M13-104','M13-329','M13-330','M13-331','M13-386','M13-389','M13-391','M13-392','M13-393','M13-394','M13-491','M13-492','M13-506','M13-782','M13-783','M13-961','M14-002','M14-004','M14-027','M14-103','M14-196','M14-226','M14-227','M14-324','M14-325','M14-490','']
# Lynparza =



list1 = [x.strip(' ') for x in list1]
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
     if y:
      alist.append(y)
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





final2=sum(alist2, [])



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



print(FDAOrg)
f = open('Full_temp_data.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('Org ID', 'NCT ID','Brief Title','Condition','Overall status','Intervention name','Acronym','Agency','Gender','Minimum Age','Phase','Agency class','Study type','Study Design','Secondary ID','First received','Start Date','Completion date','Last changed date','Verification date','First received result date','Certificate of Delay/ Disposition Date','PCD','Countries','Removed countries','IS FDA regulated','IS section 801'))
    #mylist = list(set(list01))
    #mylist1 = list(set(list02))
    #mylist2 = list(set(list03))
    #for i1 in list11:
    for i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20, i21, i22, i23,i24, i25, i26, i27 in zip(OrgID, NCTID, Btitle,Condition, OverallStatus,Intervention, acronym, agency, gender, MAge, Phase1, AgencyClass, StudyType, StudyDesign, SecID, FirstRecv, SDate, ComplDate, LastChangedDate, VerificationDate, FirstRecvResultDate, FirstRecvResultDispoDate, PCD, Countries, Rm_Countries, IsFDA,Is801):

         writer.writerow( (i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23, i24, i25,i26, i27) )
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
    if (name1.lower() in str(row[5]).lower() or name2.lower() in str(row[5]).lower() or name3.lower() in str(row[7]).lower() or name4.lower() in str(row[7]).lower()):
        registered_trials.append(row)
print ("number of valid trials "+str(len(registered_trials)))
for row in registered_trials:
    print (row[1])





Stage1File = input("What would like to name the output file as?(Eg: xyz.csv) ")


f = open(Stage1File, 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('Org ID', 'NCT ID','Brief Title','Condition','Overall status','Intervention','Acronym','Agency','Gender','Minimum Age','Phase','Agency class','Study Type','Study Design','Secondary ID','First received','Start Date','Completion date','Last changed date','Verification date','First received result date','Certificate of Delay/ Disposition Date','PCD','Countries','IS FDA regulated','IS section 801'))

    for i1 in (registered_trials):

         writer.writerow( (i1) )
finally:
    f.close()



