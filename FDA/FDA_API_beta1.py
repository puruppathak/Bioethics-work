

import requests
from urllib.request import urlopen
#return requests.get(url).json()
import json
strURL = "https://api.fda.gov/drug/label.json?search=%22daklinza%22"
#strURL = "https://api.fda.gov/drug/event.json?limit=1"

generic_name = []
values = []

response = urlopen(strURL).read().decode('utf8')
result = json.loads(response)


rmddata = result['results'][0]['indications_and_usage'][0]

print(rmddata)

