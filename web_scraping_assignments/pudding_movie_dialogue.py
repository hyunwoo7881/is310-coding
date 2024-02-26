from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

movies=pd.read_csv("cleaned_pudding_data.csv")

with open("pudding_movie_dialogue.csv", 'w', newline=' ', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Movie Title", "First 1000 Characters"])

    for index,row in movies.iterrows():
        url=row["link"]
        response = requests.get(url)
        volume_response = requests.get(url)
        volume_soup = BeautifulSoup(volume_response.text, "html.parser")
        script = volume_soup.get_text()

        first_1000_chars = script[:1000]
        
        writer.writerow([row["title"], first_1000_chars])

