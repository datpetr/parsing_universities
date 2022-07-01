
import requests
from bs4 import BeautifulSoup

direction = 'Прикладная математика и информатика (ИИИ)'
URL = 'https://priem.mirea.ru/accepted-entrants-list/'


HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Accept': '*/*'
    }


def get_html(url, params=None):
    return requests.get(url, headers=HEADERS, params=params)


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    directions = soup.find('div', class_='rates', id='rates')
    print(directions)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


# soup = BeautifulSoup(URL, 'lxml')
# directions = soup.find('div', class_='rates').find('table', id='ratesTable')
# print(directions)
parse()
