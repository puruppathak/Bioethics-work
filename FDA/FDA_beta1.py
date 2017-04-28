
import re
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
 Sentence.append(tuple)
 tuple1 = re.findall(r'[A-Z0-9-]+',str(tuple))
 #tuple11 = re.findall(r'Phase [0-9]+', str(tuple))

 """

 for tuple2 in tuple1:
  if len(tuple2) > 4:
   #print(tuple2)
   IDlist.append(tuple2)


 for tuple3 in tuple11:
  if len(tuple3) > 2:
   #print(tuple2)
   Phase.append(tuple3)
"""

"""
 for line in Sentence:
  tuple11 = re.findall(r'Phase [0-9]+',str(line))
 #for tuple21 in tuple11:
 #print(tuple11)
  if tuple11 is None:
   Phase.append("NULL")
  else:
    #NewItem = tuple11.text
    Phase.append(tuple11)
"""

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
