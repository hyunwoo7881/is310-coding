from bs4 import BeautifulSoup
import requests
import csv

url = "https://humanist.kdl.kcl.ac.uk/Archives/"

response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")

volume_links = soup.find_all('a', href=True)

with open("web_scraped_humanist_listserv.csv", 'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Volume', 'First 10000 characters','Year'])

    for link in volume_links:
        volume_url = "https://humanist.kdl.kcl.ac.uk" + link.get('href')
        
        if link.get('href').endswith("/Converted_Text/"):
            volume_response = requests.get(volume_url)
            volume_soup = BeautifulSoup(volume_response.text,'html.parser')
            
            text_link = volume_soup.find('a', text="Plain Text")
            if text_link:
                text_url = "https://humanist.kdl.kcl.ac.uk" + text_link['href']
                text_response = requests.get(text_url)
                
                if text_response.headers.get('Content-Type') == 'text/plain':
                    text = text_response.text
                    text_cleaned = BeautifulSoup(text, "html.parser").get_text()
                    first_10000_chars = text_cleaned[:10000]

                    year = link['href'].split('/')[-2]

                    writer.writerow([link.get_text(), first_10000_chars, year])
print("CSV file saved successfully")