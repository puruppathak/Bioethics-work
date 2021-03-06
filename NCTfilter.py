__author__ = 'puruppathak'


import csv
import datetime
import calendar
import re
from collections import defaultdict

__author__ = 'Puru Pathak'

f=open('data_Erivedge.csv', 'rU')
csv_f = csv.reader(f)



month_dict = {'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

#for i in range(1, 13, 1):
#    next(csv_f, None)

name1 = input("What's the drug name? ")
name2 = input("What's another drug name? ")
name3 = input("What's the sponsor's name? ")
name4 = input("Is there any other name for the sponsor(If not, please enter the same sponsor name)? ")




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






f = open('Erivedge.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('Org ID', 'NCT ID','Brief Title','Condition','Overall status','Intervention','Acronym','Agency','Gender','Minimum Age','Phase','Agency class','Study Type','Study Design','Secondary ID','First received','Start Date','Completion date','Last changed date','Verification date','First received result date','Certificate of Delay/ Disposition Date','PCD','Countries','IS FDA regulated','IS section 801'))

    for i1 in (registered_trials):

         writer.writerow( (i1) )
finally:
    f.close()
