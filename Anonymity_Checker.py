import requests

res = requests.get('https://ipinfo.io/')
data = res.json()

country = data['country']
timezone = data['timezone']
ip = data['ip']
postal = data['postal']
city = data['city']
region = data['region']
location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]

print("\n Anonymity Checker")
print("\n Tool Designed by aseelps")

print("IP : ", ip)
print("Country : ", country)
print("Region : ", region)
print("City : ", city)
print("Postal : ", postal)
print("Timezone : ", timezone)
print("Latitude : ", latitude)
print("Longitude : ", longitude)

