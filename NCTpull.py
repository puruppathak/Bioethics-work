__author__ = 'puruppathak'


import bs4
import lxml
import urllib.request
import re



list1 = ['LTS6050','LTS6048'];
len1 = len(list1)-1
alist = [];
strURL1 = 'https://clinicaltrials.gov/ct2/results?term='
strURL2 = '&Search=Searchdisplayxml=true'
for indic1 in list1:


  strURL3 = strURL1 + indic1 + strURL2
#req = urllib.request.urlopen('https://clinicaltrials.gov/show/NCT01487096?displayxml=true')
  req = urllib.request.urlopen(strURL3)


  xml = bs4.BeautifulSoup(req, 'xml')

  for item in xml.findAll('nct_id'):

    #print (item["data"])
    #item1 = item.read()
   # y=re.findall('<agency>(.*)</agency>',str(item))
    print ("NCT ID: "+ item.text)
    var1=item.text
    #print (y)
    #print (y[0])


    for i in range(0,len1):
      alist.insert(i,var1)
      print (alist)


#list1 = ['NCT01487096', 'NCT00261846'];

strURL11 = 'https://clinicaltrials.gov/show/'
strURL21 = '?displayxml=true'
for indic11 in alist:


  strURL31 = strURL11 + indic11 + strURL21
#req = urllib.request.urlopen('https://clinicaltrials.gov/show/NCT01487096?displayxml=true')
  req = urllib.request.urlopen(strURL31)


  xml = bs4.BeautifulSoup(req, 'xml')

  for item in xml.findAll('nct_id'):

    #print (item["data"])
    #item1 = item.read()
   # y=re.findall('<agency>(.*)</agency>',str(item))
    print ("NCT ID: "+ item.text)
    #print (y)
    #print (y[0])



  for item in xml.findAll('agency'):

    #print (item["data"])
    #item1 = item.read()
   # y=re.findall('<agency>(.*)</agency>',str(item))
    print ("SPONSORING AGENCY IS: "+item.text)
    #print (y)
    #print (y[0])

  for item in xml.findAll('start_date'):

    #print (item["data"])
    #item1 = item.read()
   # y=re.findall('<agency>(.*)</agency>',str(item))
    print ("TRIAL START DATE IS: "+item.text)
    #print (y)
    #print (y[0])

  for item in xml.findAll('firstreceived_date'):

    #print (item["data"])
    #item1 = item.read()
   # y=re.findall('<agency>(.*)</agency>',str(item))
    print ("REGISTRATION DATE IS: "+item.text)
    #print (y)
    #print (y[0])

  for item in xml.findAll('primary_completion_date'):

    #print (item["data"])
    #item1 = item.read()
   # y=re.findall('<agency>(.*)</agency>',str(item))
    print ("PRIMARY COMPLETION DATE IS: "+item.text)
    #print (y)
    #print (y[0])


