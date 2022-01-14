#Covit-19 in Chile

import requests

url = 'https://corona.lmao.ninja/v2/countries/Chile?yesterday&strict&query%20'

assetInfo        = requests.get(url).json()

# print(assetInfo)
def fn(val):
    return f"{val:,}".replace(",",".")


print(f"País        -   {assetInfo['country']}")
print(f"Casos       -   {fn(assetInfo['todayCases'])} / {fn(assetInfo['cases'])}")
print(f"Muertes     -   {fn(assetInfo['todayDeaths'])} / {fn(assetInfo['deaths'])}")
print(f"Recuperados -   {fn(assetInfo['todayRecovered'])} / {fn(assetInfo['recovered'])}")