import csv
import datetime
import calendar
import re
from collections import defaultdict

__author__ = 'Puru Pathak'

f=open('EAP1.csv', 'rU')
csv_f = csv.reader(f)

#csv_f = csv.reader((line.replace('\0','') for line in f), delimiter=",")
#csv_f = csv.reader(f)

month_dict = {'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

#for i in range(1, 13, 1):


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


print "number of trials analyzed is " + str(len(allTrials)-1)
"""
for row in allTrials:
    if("expanded" in str(row[13]).lower() or "expanded" in str(row[2]).lower()  or "expanded" in str(row[21]).lower() or "expanded" in str(row[3]).lower() or "expanded" in str(row[4]).lower() or "expanded" in str(row[5]).lower() or "expanded" in str(row[6]).lower() or "expanded" in str(row[7]).lower() or "expanded" in str(row[8]).lower() or "expanded" in str(row[9]).lower() or "expanded" in str(row[10]).lower() or "expanded" in str(row[11]).lower() or "expanded" in str(row[12]).lower() or "expanded" in str(row[14]).lower() or "expanded" in str(row[15]).lower() or "expanded" in str(row[16]).lower() or "expanded" in str(row[17]).lower() or "expanded" in str(row[18]).lower() or "expanded" in str(row[19]).lower()):
        registered_trials.append(row)
print "number of expanded access trials "+str(len(registered_trials))

"""
for row in allTrials:
    if("expanded" not in str(row[13]).lower() and "expanded" not in str(row[2]).lower()  and "expanded" not in str(row[21]).lower() and "expanded" not in str(row[3]).lower() and "expanded" not in str(row[4]).lower() and "expanded" not in str(row[5]).lower() and "expanded" not in str(row[6]).lower() and "expanded" not in str(row[7]).lower() and "expanded" not in str(row[8]).lower() and "expanded" not in str(row[9]).lower() and "expanded" not in str(row[10]).lower() and "expanded" not in str(row[11]).lower() and "expanded" not in str(row[12]).lower() and "expanded" not in str(row[14]).lower() and "expanded" not in str(row[15]).lower() and "expanded" not in str(row[16]).lower() and "expanded" not in str(row[17]).lower() and "expanded" not in str(row[18]).lower() and "expanded" not in str(row[19]).lower()):
        registered_trials.append(row)
print "number of non expanded access trials "+str(len(registered_trials)-1)




for row in allTrials:
    if("expanded" not in str(row[13]).lower() and "compassionate" not in str(row[13]).lower() and "compassionate" not in str(row[2]).lower() and "compassionate" not in str(row[21]).lower() and "expanded" not in str(row[2]).lower()  and "expanded" not in str(row[21]).lower() and "expanded" not in str(row[3]).lower() and "expanded" not in str(row[4]).lower() and "expanded" not in str(row[5]).lower() and "expanded" not in str(row[6]).lower() and "expanded" not in str(row[7]).lower() and "expanded" not in str(row[8]).lower() and "expanded" not in str(row[9]).lower() and "expanded" not in str(row[10]).lower() and "expanded" not in str(row[11]).lower() and "expanded" not in str(row[12]).lower() and "expanded" not in str(row[14]).lower() and "expanded" not in str(row[15]).lower() and "expanded" not in str(row[16]).lower() and "expanded" not in str(row[17]).lower() and "expanded" not in str(row[18]).lower() and "expanded" not in str(row[19]).lower()):
        published_trials.append(row)
print "number of non expanded access and non compassionate care trials "+str(len(published_trials)-1)

for row in published_trials:
    print row[1]
