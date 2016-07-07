__author__ = 'puruppathak'

import bs4
import lxml
import urllib.request
import re

list1 = ['NCT01487096', 'NCT00261846'];

strURL1 = 'https://clinicaltrials.gov/show/'
strURL2 = '?displayxml=true'
for indic1 in list1:


  strURL3 = strURL1 + indic1 + strURL2
#req = urllib.request.urlopen('https://clinicaltrials.gov/show/NCT01487096?displayxml=true')
  req = urllib.request.urlopen(strURL3)


  xml = bs4.BeautifulSoup(req, 'xml')

  for item in xml.findAll('nct_id'):

    #print (item["data"])
    #item1 = item.read()
   # y=re.findall('<agency>(.*)</agency>',str(item))
    print (item.text)
    #print (y)
    #print (y[0])




  for item in xml.findAll('agency'):

    #print (item["data"])
    #item1 = item.read()
   # y=re.findall('<agency>(.*)</agency>',str(item))
    print (item.text)
    #print (y)
    #print (y[0])

  for item in xml.findAll('start_date'):

    #print (item["data"])
    #item1 = item.read()
   # y=re.findall('<agency>(.*)</agency>',str(item))
    print (item.text)
    #print (y)
    #print (y[0])
