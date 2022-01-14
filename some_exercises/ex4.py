import requests
from   requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"

urlbase   = "https://api.carbonintensity.org.uk/intensity/date"
assetInfo = requests.get(urlbase,  headers=headers).json()

for i in assetInfo['data']:
    print(i)