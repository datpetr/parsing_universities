import requests
from bs4 import BeautifulSoup

url = 'https://pk.mipt.ru/bachelor/list/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='text')
print(quotes)
