import PyPDF2

PDFfilename = "Belsomra_MR.pdf" #filename of your PDF/directory where your PDF is stored

pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object

print(pfr)

import requests



PDFfilename = '123.pdf'

fileData = (PDFfilename, open(PDFfilename, 'rb')) #"rb" stands for "read bytes"

files = {'f': fileData}

apiKey = "yaocle8hdkxf"

fileExt = "csv" #format/file extension of final document

postUrl = "https://pdftables.com/api?key={0}&format={1}".format(apiKey, fileExt)
#the .format puts value of apiKey where {0} is, etc

response = requests.post(postUrl, files=files)

response.raise_for_status() # ensure we notice bad responses

downloadDir = "example.csv" #directory where you want your file downloaded to

with open(downloadDir, "wb") as f:
    f.write(response.content) #write data to csv