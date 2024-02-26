import requests
import apikey

api_key = "427acc009fde01c9f13d9c57c986d71a"

apikey.save("dpla_key", api_key)

dpla_api_key = apikey.load('dpla_key')
url = "https://api.dp.la/v2/items?q=kittens&api_key="

response = requests.get(url + dpla_api_key)

print(response.json()["docs"][0])