



from Bio import Entrez

# Getting all possible PubMed IDs
import csv

##
# Belsomra patients = ['31','28','40','22','20','32','254','18','10','781','17','6','12','16','14','53','73','24','75','1022','1019','25']
# Belsomra NCTs = ['NCT00792298','NCT01021813','NCT01043926','NCT01059851','NCT01097616','NCT01097629','NCT01293006','NCT01311882','NCT01300455']
# Belsomra search = Suvorexant
# Cerdelga search = ELIGLUSTAT TARTRATE
# Cerdelga patients = ['40','160','26','171','22','24','74','10','5','36','25','28','14','29','47']
# Cerdelga NCTs = ['NCT00891202','NCT00943111','NCT00358150','NCT01074944','NCT01452542','NCT01357811','NCT01659944']

##
Sponsor=[]
startDate=[]
VI=[]
final=[]
NCT=[]
PMID=[]
PubD=[]
ABs=[]
list1=['Suvorexant']
available_trials1=[]
available_trials2=[]

Entrez.email = "puruppathak@gmail.com"     # Always tell NCBI who you are
for i in list1:
 handle = Entrez.egquery(term=i)
 record = Entrez.read(handle)
 for row in record["eGQueryResult"]:
   if row["DbName"]=="pubmed":
     print(row["Count"])





for i in list1:
 handle = Entrez.esearch(db="pubmed", term=i, retmax=1000000)
 record = Entrez.read(handle)
 idlist = record["IdList"]
 final.append(idlist)
#print(final)
final3=sum(final, [])

from Bio import Medline
handle = Entrez.efetch(db="pubmed", id=final3, rettype="medline",
                           retmode="text")
records = Medline.parse(handle)

records = list(records)


for record in records:
    if not "PMID" in record:
        PMID.append("NULL")
    else:
      idlist = record["PMID"]
      PMID.append(idlist)
    if not "AB" in record:
        ABs.append("NULL")
    else:
        idlist1 = record["AB"]
        ABs.append(idlist1)
    if not "DP" in record:
        PubD.append("NULL")
    else:
        idlist2 = record["DP"]
        PubD.append(idlist2)
    if not "SI" in record:
        NCT.append("NULL")
    else:
        idlist3 = record["SI"]
        NCT.append(idlist3)
    if not "AD" in record:
        Sponsor.append("NULL")
    else:
        idlist4 = record["AD"]
        Sponsor.append(idlist4)



print("Length is:"+str(len(PMID))+" " + str(len(ABs)))




## Writing to csv

f = open('PubMedData.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('PubMed ID','Date','Abstract','NCT','Sponsor'))
    #mylist = list(set(list01))
    #mylist1 = list(set(list02))
    #mylist2 = list(set(list03))
    #for i1 in list11:
    for i1,i2,i3,i4,i5 in zip(PMID,PubD,ABs,NCT,Sponsor):

         writer.writerow( (i1,i2,i3,i4,i5) )
finally:
    f.close()






f=open('PubMedData.csv', 'rU')
csv_f = csv.reader(f)


#name1 = input("How many patients? ")
#name2 = input("Some more ")
#name3 = input("What's the sponsor's name?(If nothing, please enter NULL) ")
#name4 = input("Is there any other name for the sponsor(If not, please enter NULL)? ")



#patients=['31','28']
allTrials = []
first_stage_cleared = []
registered_trials = []
published_trials = []
reported_trials = []
timely_reported_trials = []
available_trials = []
patients=['31','28','40','22','20','32','254','18','10','781','17','6','12','16','14','53','73','24','75','1022','1019','25']

for row in csv_f:
    if(row[1] != ""):
        allTrials.append(row)

    for i in patients:
        for row in allTrials:
            if (i in str(row[2]).lower()):
                registered_trials.append(row)

#print ("number of trials analyzed is " + str(len(allTrials)-1))



#Stage1File = input("What would like to name the output file as?(Eg: xyz.csv) ")

for row in registered_trials:
    if("merck" in row[4].lower()):
        available_trials1.append(row)




NCTs= ['NCT00792298','NCT01021813','NCT01043926','NCT01059851','NCT01097616','NCT01097629','NCT01293006','NCT01311882','NCT01300455']
NCT_check=[]

for i in NCTs:
  for row in allTrials:
    if (i in str(row[3])):
        NCT_check.append(row)


for row in allTrials:
    if ((row in available_trials1) or (row in NCT_check)):
        available_trials2.append(row)




f = open('pubmed_filtered_3.csv', 'wt')
try:
    writer = csv.writer(f)
    writer.writerow(('PubMed ID','Date','Abstract','NCT','Sponsor'))

    for i1 in (available_trials2):

         writer.writerow( (i1) )
finally:
    f.close()



