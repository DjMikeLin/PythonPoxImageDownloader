import requests
import csv
from bs4 import BeautifulSoup

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = [[soup.find('main').find('form').get('action')[1:].capitalize()]]
    image_links = soup.find_all('img')
    for link in image_links:
        temp = [link.find_parent('div').find('div').find('p').text[6:]]
        temp.append(link.get('data-lazy'))
        results.append(temp)
    
    return results

types = ['champions']#, 'spells', 'relics', 'equipments', 'abilities']

final_set = []
for type in types:
    final_set.append(get_links("https://aqueous-dusk-28109.herokuapp.com/{}/".format(type)))
    
with open('test.csv', 'w', newline='') as file:
    write = csv.writer(file)
    write.writerows(final_set)
