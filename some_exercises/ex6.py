import os
import requests

url = "https://www.amdoren.com/api/currency.php"


assertInfo = requests.get(url).json()

print(assertInfo)