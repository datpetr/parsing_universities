import requests
from bs4 import BeautifulSoup

URL = 'https://priem.mirea.ru/accepted-entrants-list/'
HEADS = [
    {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) '
                      'Gecko/20100101 Firefox/103.0',
        'accept': '*/*'
    }
]


def get_html(url, params=None):
    return requests.get(url, headers=HEADS, params=params)


print(get_html(URL))


def parse():
    html = get_html(URL)
    print(html.status_code)


parse()
