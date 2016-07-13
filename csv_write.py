import csv

__author__ = 'puruppathak'

import csv
import sys
import bs4
import lxml
import urllib.request
import re

list1 = ['CAMN107Y2101', 'CLDE225A1102','CLDE225A2112','CLDE225A1102','CLDE225A1102','CLDE225A2112','CLDE225A2201'];
len1 = len(list1)-1
alist = [];
X = [1,2,3]
Y = [4,5,6]
list01=[]
strURL1 = 'https://clinicaltrials.gov/ct2/results?term='
strURL2 = '&Search=Searchdisplayxml=true'
for indic1 in list1:


  strURL3 = strURL1 + indic1 + strURL2
#req = urllib.request.urlopen('https://clinicaltrials.gov/show/NCT01487096?displayxml=true')
  req = urllib.request.urlopen(strURL3)


  xml = bs4.BeautifulSoup(req, 'xml')

  for item in xml.findAll('nct_id'):



    #var1=item.text
    if item.text!="":
     for i in range(0,len1):

      alist.append(item.text)
      #print (alist)
    else:
        break
strURL11 = 'https://clinicaltrials.gov/show/'
strURL21 = '?displayxml=true'
for indic11 in alist:


  strURL31 = strURL11 + indic11 + strURL21
#req = urllib.request.urlopen('https://clinicaltrials.gov/show/NCT01487096?displayxml=true')
  req = urllib.request.urlopen(strURL31)


  xml = bs4.BeautifulSoup(req, 'xml')



  for item in xml.findAll('org_study_id'):
    NewItem1 = item.text


    for i in range(0,len1):
      list01.insert(i,NewItem1)
      #print (list01)

f = open('mydata2.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('Title 1', 'Title 2', 'Title 3') )
    mylist = list(set(list01))
    #for i1 in list11:
    for i,j,k in zip(mylist, mylist, mylist):

         writer.writerow( (i, j , k) )
finally:
    f.close()

