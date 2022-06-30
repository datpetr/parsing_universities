import requests
from bs4 import BeautifulSoup
import pandas as pd

def pushing(item, info): # getting data from the table
    return item.find('td', class_=f'{info}').get_text(strip=True)

def urls(name):
    # ИИИ_1 - ПМИ, ИИИ_2 - ИВТ
    # ИИТ_1 - ПМИ, ИИТ_2 - ИВТ
    names = {
        'ИИИ_1':'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416774837808438',
        'ИИТ_1': 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416794849881398',
        'ИТУ': 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416806591835446',
        'ИКБ': 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416814830497078',
        'ИТХТ': 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416824219446582',
        'ИРИ': 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1714956668866964790',
        'ИИИ_2': 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417222681472310',
        'ИИТ_2': 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416831985200438'
    }




def parse(url):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.content, 'html.parser')
    items_abitur = soup.find('table', class_='namesTable').find_all('tr')
    data_based = soup.find('p', class_='lastUpdate').get_text(strip=True) # когда было обновление базы
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


parse('https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416774837808438')