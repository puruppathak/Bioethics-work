

from Bio import Entrez
Entrez.email = "puruppathak@gmail.com"     # Always tell NCBI who you are
handle = Entrez.egquery(term="aubagio")
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
     if row["DbName"]=="pubmed":
         print(row["Count"])

handle = Entrez.esearch(db="pubmed", term="aubagio", retmax=463)
record = Entrez.read(handle)
idlist = record["IdList"]
#print(idlist)         

from Bio import Medline
handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",
                           retmode="text")
records = Medline.parse(handle)

records = list(records)

for record in records:
 #print("title:", record.get("AB", "?"))
 #print("authors:", record.get("AU", "?"))
 #print("source:", record.get("SO", "?"))
 print("")


## Testing searching 

search_author = "sclerosis"

for record in records:
 if not "AB" in record:
  continue
 if search_author in record["AB"]:
    print("Result found %s found: %s" % (search_author, record["PMID"]))




