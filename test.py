import requests
from bs4 import BeautifulSoup

direction = 'Прикладная математика и информатика (ИИИ)'
URL_main_page = 'https://priem.mirea.ru/accepted-entrants-list/'


HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36',
        'Accept': '*/*'
    }


def pushing(item, info): # getting data from the table
    return item.find('td', class_=f'{info}').get_text(strip=True)


def get_html(url, params=None):
    return requests.get(url, headers=HEADERS, params=params)


def get_urls(name):
    if name == 'ИИИ':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416774837808438'
    if name == 'ИИТ':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416794849881398'


def get_content(html):
    soup_main_page = BeautifulSoup(html, 'lxml')
    directions = soup_main_page.find('div', class_='rates', id='rates')

    res = get_html('https://priem.mirea.ru/accepted-entrants-list/'
                   'personal_code_rating.php?competition'
                   '=1712416774837808438')
    soup = BeautifulSoup(res.content, 'html.parser')
    items_abitur = soup.find('table', class_='namesTable').find_all('tr')
    data_based = soup.find('p', class_='lastUpdate').get_text(strip=True)  # когда было обновление базы
    # all_points = soup.find('p', class_='text-align: center').get_text(strip=True)
    users = []

    for item in items_abitur:
        users.append({
            'num': pushing(item, 'num'),
            'fio': pushing(item, 'fio'),
            'accepted': pushing(item, 'accepted'),
            'original': pushing(item, 'original'),
            'campus': pushing(item, 'campus'),
            'marks': pushing(item, 'marks'),
            'achievments': pushing(item, 'achievments'),
            'sum': pushing(item, 'sum')
        })
    print(users)


def parse():
    html = get_html(URL_main_page)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
