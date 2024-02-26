import requests
import json

url = "https://swapi.dev/api/"

response = requests.get(url)
data = response.json()

with open('star_wars.json','w') as f:
    json.dump(data, f, indent=4)
    

films_url = data["films"]
films_response = requests.get(films_url)
films_data = films_response.json()
with open('films','w') as f:
    json.dump(films_data, f, indent=4)

#print(films_data["results"][0])


people_url = data["people"]
people_response = requests.get(people_url)
people_data = people_response.json()
with open('people','w') as f:
    json.dump(people_data,f, indent=4)

people_names = [person["name"] for person in people_data["results"]]

with open('people_names.json','w') as f:
    json.dump(people_names, f, indent=4)

print(people_names)