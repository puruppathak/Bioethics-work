import csv
import datetime
import calendar
import re
from collections import defaultdict
import operator

#f=repr(open('Aubagio_11.11.14.xlsx', 'rU'))
isDrugFDA = True


isManufacturedInUS = False
isExportedToUS = False
isTrialUnderFDA = True
isExpandedAccess = False
enroll=[]
Eapplicable=[]
ReportPool=[]
published=[]
available_trials=[]
pub1=[]
pub2=[]


f=open('trial.csv', 'rU')
csv_f = csv.reader(f)

#csv_f = csv.reader((line.replace('\0','') for line in f), delimiter=",")
#csv_f = csv.reader(f)

month_dict = {'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

for i in range(1, 2, 1):
    next(csv_f, None)
zero_stage_cleared = []
first_stage_cleared = []
second_stage_cleared = []
third_stage_cleared = []
fourth_stage_cleared = []
fifth_stage_cleared = []
trialsForReporting = []
timelyReportedTrials = []
drugOn=[]

name1 = raw_input("What's the drug name? ")


trialStartDate = None
trialEndDate = None

for row in csv_f:
    if(row[0]!=''):
        zero_stage_cleared.append(row)


for row in zero_stage_cleared:
    if(name1.lower() in str(row[0]).lower()):
        drugOn.append(row)



for row in drugOn:

        enroll.append(row)






##

for row in enroll:
    if((row[17] != "")):
        reportingDateMatch = re.search(r'(\d+)[/-](\d+)[/-](\d+)', row[17], re.M|re.I)
        if(reportingDateMatch):
            reportingDateMonth = reportingDateMatch.group(1)
            reportingDateYear = str(reportingDateMatch.group(3))
            reportingDateDay= str(reportingDateMatch.group(2))


            if(len(str(reportingDateYear)) == 4 ):
                trialReportingDate = datetime.date(int(reportingDateYear), int(reportingDateMonth), int(reportingDateDay))

            elif(len(str(reportingDateYear)) == 2 ):
                if(int(reportingDateYear) <=  50):
                    trialReportingDate = datetime.date(int(str(20)+reportingDateYear), int(reportingDateMonth), int(reportingDateDay))
                else:
                    trialReportingDate = datetime.date(int(str(19)+reportingDateYear), int(reportingDateMonth), int(reportingDateDay))
            else:
                trialReportingDate = datetime.date(int(str(200)+reportingDateYear), int(reportingDateMonth), day = int(reportingDateDay))
        #print "report date is " + str(trialReportingDate)
            #print(trialReportingDate)
            if(trialReportingDate<datetime.date(2015, 2, 1)):
             #print(trialReportingDate)
             Eapplicable.append(row)
            else:
             print ('trial  ' + str(row[3]) + " is not timely registered, so excluded")



print("Total trials analysed are ->"+str(len(Eapplicable)))



##
#print(datetime.date(2015, 2, 1))


for row in Eapplicable:         # Reporting check
    if((row[16] != "")):
        ReportPool.append(row)


print("Total trials reported are ->"+str(len(ReportPool)))



## Publishing check
'''
for row in Eapplicable:
    if((row[20] != "" or row[21]!="")):
        reportingDateMatch = re.search(r'(\d+)[/-](\d+)[/-](\d+)', row[20], re.M|re.I)
        reportingDate1Match = re.search(r'(\d+)[/-](\d+)[/-](\d+)', row[21], re.M | re.I)

        if(reportingDateMatch):
            reportingDateMonth = reportingDateMatch.group(1)
            reportingDateYear = str(reportingDateMatch.group(3))
            reportingDateDay= str(reportingDateMatch.group(2))


            if(len(str(reportingDateYear)) == 4 ):
                trialReportingDate = datetime.date(int(reportingDateYear), int(reportingDateMonth), int(reportingDateDay))

            elif(len(str(reportingDateYear)) == 2 ):
                if(int(reportingDateYear) <=  50):
                    trialReportingDate = datetime.date(int(str(20)+reportingDateYear), int(reportingDateMonth), int(reportingDateDay))
                else:
                    trialReportingDate = datetime.date(int(str(19)+reportingDateYear), int(reportingDateMonth), int(reportingDateDay))
            else:
                trialReportingDate = datetime.date(int(str(200)+reportingDateYear), int(reportingDateMonth), day = int(reportingDateDay))
        #print "report date is " + str(trialReportingDate)

        if (reportingDate1Match):
                reportingDate1Month = reportingDate1Match.group(1)
                reportingDate1Year = str(reportingDate1Match.group(3))
                reportingDate1Day = str(reportingDate1Match.group(2))

                if (len(str(reportingDate1Year)) == 4):
                    trialReporting1Date = datetime.date(int(reportingDate1Year), int(reportingDate1Month),
                                                       int(reportingDate1Day))

                elif (len(str(reportingDate1Year)) == 2):
                    if (int(reportingDate1Year) <= 50):
                        trialReporting1Date = datetime.date(int(str(20) + reportingDate1Year), int(reportingDate1Month),
                                                           int(reportingDate1Day))
                    else:
                        trialReporting1Date = datetime.date(int(str(19) + reportingDate1Year), int(reportingDate1Month),
                                                           int(reportingDate1Day))
                else:
                    trialReporting1Date = datetime.date(int(str(200) + reportingDate1Year), int(reportingDate1Month),
                                                       day=int(reportingDate1Day))
                    # print "report date is " + str(trialReportingDate)
                    # print(trialReportingDate)
            #print(trialReportingDate)
        if(trialReportingDate or trialReporting1Date):
           if(trialReportingDate<datetime.date(2015, 2, 1) or trialReporting1Date<datetime.date(2015, 2, 1) ):
             published.append(row)
           else:
             print ('trial  ' + str(row[3]) + " is not timely reported, so excluded")


'''
##


for row in Eapplicable:
    if((row[20] != "")):
        reportingDateMatch = re.search(r'(\d+)[/-](\d+)[/-](\d+)', row[20], re.M|re.I)
        if(reportingDateMatch):
            reportingDateMonth = reportingDateMatch.group(1)
            reportingDateYear = str(reportingDateMatch.group(3))
            reportingDateDay= str(reportingDateMatch.group(2))



            trialReportingDate = datetime.date(int(reportingDateYear), int(reportingDateMonth), int(reportingDateDay))


            if(trialReportingDate<datetime.date(2016, 2, 2)):
             #print(trialReportingDate)
             pub1.append(row)
            else:
             print ('trial  ' + str(row[3]) + " is not timely published(Row 1), so excluded")



##
'''
for row in enroll:
    if((row[20] != "")):
        reportingDateMatch = re.search(r'(\d+)[/-](\d+)[/-](\d+)', row[20], re.M|re.I)
        if(reportingDateMatch):
            reportingDateMonth = reportingDateMatch.group(1)
            reportingDateYear = str(reportingDateMatch.group(3))
            reportingDateDay= str(reportingDateMatch.group(2))


            if(len(str(reportingDateYear)) == 4 ):
                trialReportingDate = datetime.date(int(reportingDateYear), int(reportingDateMonth), int(reportingDateDay))

            elif(len(str(reportingDateYear)) == 2 ):
                if(int(reportingDateYear) <=  50):
                    trialReportingDate = datetime.date(int(str(20)+reportingDateYear), int(reportingDateMonth), int(reportingDateDay))
                else:
                    trialReportingDate = datetime.date(int(str(19)+reportingDateYear), int(reportingDateMonth), int(reportingDateDay))
            else:
                trialReportingDate = datetime.date(int(str(200)+reportingDateYear), int(reportingDateMonth), day = int(reportingDateDay))
        #print "report date is " + str(trialReportingDate)
            #print(trialReportingDate)
            if(trialReportingDate<datetime.date(2016, 2, 1)):
             #print(trialReportingDate)
             pub1.append(row)
            else:
             print ('trial  ' + str(row[3]) + " is not timely published(Row 1), so excluded")

'''
for row in Eapplicable:
    if((row[21] != "")):
        reportingDateMatch = re.search(r'(\d+)[/-](\d+)[/-](\d+)', row[21], re.M|re.I)
        if(reportingDateMatch):
            reportingDateMonth = reportingDateMatch.group(1)
            reportingDateYear = str(reportingDateMatch.group(3))
            reportingDateDay= str(reportingDateMatch.group(2))



            trialReportingDate = datetime.date(int(reportingDateYear), int(reportingDateMonth), int(reportingDateDay))


            if(trialReportingDate<datetime.date(2016, 2, 2)):
             pub2.append(row)
            else:
             print ('trial  ' + str(row[3]) + " is not timely published(Row 2), so excluded")




for row in enroll:
    if ((row in pub1) or (row in pub2)):
        published.append(row)

print("Total published trials are ->"+str(len(published)))


for row in published:

    print(row[3])



for row in enroll:
    if ((row in ReportPool) or (row in published)):
        available_trials.append(row)



'''
for row in available_trials:

    print(row[3])Lynparza
'''
print("Total available trials are ->"+str(len(available_trials)))




