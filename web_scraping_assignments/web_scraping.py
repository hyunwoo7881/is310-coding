from bs4 import BeautifulSoup
import requests
import csv

response = requests.get("https://humanist.kdl.kcl.ac.uk/")

soup = BeautifulSoup(response.text, features='html.parser')

links = soup.find_all('a')


with open("humanist_volumes.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Link','Volume Text'])
    for link in links:
        if "Archives" in link.get('href'):
            print(link.get_text())
            volume_url = "https://humanist.kdl.kcl.ac.uk" + link.get('href')
            volume_response = requests.get(volume_url)
            volume_soup = BeautifulSoup(volume_response.text, "html.parser")
            print(volume_soup.get_text())