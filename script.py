import requests
import csv
from bs4 import BeautifulSoup

response = requests.get("https://aqueous-dusk-28109.herokuapp.com/champions/")

soup = BeautifulSoup(response.text, 'html.parser')

image_links = soup.find_all('img')

results = [['Champions']]

for link in image_links:
    results.append([link.get('data-lazy')])

with open('test.csv', 'w', newline='') as file:
    write = csv.writer(file)
    write.writerows(results)
