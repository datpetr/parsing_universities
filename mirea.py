
import requests
from bs4 import BeautifulSoup

direction = 'Прикладная математика и информатика (ИИИ)'
URL = 'https://priem.mirea.ru/accepted-entrants-list/'


HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36',
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
