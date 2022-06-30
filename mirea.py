import requests
from bs4 import BeautifulSoup

university = 'Прикладная математика и информатика (ИИИ)'
url = 'https://priem.mirea.ru/accepted-entrants-list/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
directions = soup.find('div', class_='rates').find('table', id='ratesTable')
print(directions)
