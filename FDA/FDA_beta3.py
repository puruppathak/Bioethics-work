
import re
import csv
#txt = "VER001-12 was a Phase 1 study of the safety, tolerability and pharmacokinetics of dalbavancin in individuals with impaired hepatic function. In this study individuals received a 1000 mg IV dose of dalbavancin on Day 1, and a 500 mg IV dose on Day 8. Subjects were housed in the site’s Phase 1 clinical trials unit on Days -1 through completion of all assessments on Day 2 (i.e., 2 nights). Subjects did not stay overnight in the unit subsequent to the second dose. Subjects were to return periodically at scheduled visits for examination, solicitation of adverse events, and phlebotomy for pharmacokinetic data and laboratory safety testing, including serum chemistry.An integral part of the study was the inclusion of a control group of individuals with normal hepatic function. Subject 12001004 was a 43 year old male who served as a healthy control. On screening, he reported no significant past medical history. His only recent prior medication was Alka-Seltzer Plus for symptoms of an upper respiratory infection. This individual was noted to have abnormal tests of hepatic function as part of his Day 60 laboratory data, including an ALT value of 2525 IU/L. Unfortunately this was not initially noted to be abnormal, as the site mistakenly thought these data were from a hepatically impaired subject and therefore not unusual."

f = open("123.txt")
filetext=f.read()

IDlist=[]
Sentence=[]
Phase=[]
#txt1="I like to eat apple. Me too. Let's go buy some apples."
define_words = 'study'
#print (re.findall(r"([^.]*?%s[^.]*\.)" % define_words,txt)  )

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


print(IDlist)

for item in IDlist:
 for item1 in item:
  #print(item1)
  if len(item1)<4:
   nested_remove(IDlist,str(item1))




print(IDlist)



print(Sentence)

print(Phase)
print(len(IDlist))
print(len(Phase))



allTrials=[]
cleaned_trials=[]



f = open('FDA_data.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('Org ID','Phase','Sentence'))
    #mylist = list(set(list01))
    #mylist1 = list(set(list02))
    #mylist2 = list(set(list03))
    #for i1 in list11:
    for i1,i2,i3 in zip(IDlist,Phase,Sentence):
         writer.writerow( (i1,i2,i3) )
finally:
    f.close()



f=open('FDA_data.csv', 'rU')
csv_f = csv.reader(f)

for row in csv_f:
    if(len(row[1])>5):
        allTrials.append(row)


for row in allTrials:
    if ("NULL" not in row[0]):
        cleaned_trials.append(row)



f = open('FDA_cleaned.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow(('Org ID','Phase','Sentence'))

    for i1 in (cleaned_trials):

         writer.writerow( (i1) )
finally:
    f.close()

