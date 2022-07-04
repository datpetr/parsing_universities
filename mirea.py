import requests
from bs4 import BeautifulSoup

URL_main_page = 'https://priem.mirea.ru/accepted-entrants-list/'

'''
dict_of_directions = {
    '01.03.02 Прикладная математика и информатика (ИИИ)': 'ИИИ1',
    '01.03.04 Прикладная математика (ИИТ)': 'ИИТ1',
    '01.03.05 Статистика (ИТУ)': 'ИТУ1',
    '02.03.02 Фундаментальная информатика и информационные технологии (ИКБ)': 'ИКБ1',
    '04.03.01 Химия (ИТХТ)': 'ИТХТ1',
    '05.03.03 Картография и геоинформатика (ИРИ)': 'ИРИ1',
    '09.03.01 Информатика и вычислительная техника (ИИИ)': 'ИИИ2',
    '09.03.01 Информатика и вычислительная техника (ИИТ)': 'ИИТ2',
    '09.03.02 Информационные системы и технологии (ИКБ)': 'ИКБ2',
    '09.03.02 Информационные системы и технологии (ИРИ)': 'ИРИ2',
    '09.03.02 Информационные системы и технологии - Компьютерный дизайн (ИПТИП)': 'ИПТИП1',
    '09.03.02 Информационные системы и технологии - Фулстек разработка (ИПТИП)': 'ИПТИП2',
    '09.03.03 Прикладная информатика (ИИТ)': 'ИИТ3',
    '09.03.04 Программная инженерия (ИИТ)': 'ИИТ4',
    '10.03.01 Информационная безопасность (ИКБ)': 'ИКБ3',
    '10.05.01 Компьютерная безопасность (ИИИ)': 'ИИИ3',
    '10.05.02 Информационная безопасность телекоммуникационных систем (ИИИ)': 'ИИИ4',
    '10.05.03 Информационная безопасность автоматизированных систем (ИКБ)': 'ИКБ4',
    '10.05.04 Информационно-аналитические системы безопасности (ИКБ)': 'ИКБ5',
    '10.05.05 Безопасность информационных технологий в правоохранительной сфере (ИКБ)': 'ИКБ6',
    '11.03.01 Радиотехника (ИРИ)': 'ИРИ3',
    '11.03.02 Инфокоммуникационные технологии и системы связи (ИРИ)': 'ИРИ4',
    '11.03.03 Конструирование и технология электронных средств (ИРИ)': 'ИРИ5',
    '11.03.04 Электроника и наноэлектроника (ИПТИП)': 'ИПТИП3',
    '11.05.01 Радиоэлектронные системы и комплексы (ИРИ)': 'ИРИ6',
    '12.03.01 Приборостроение (ИКБ)': 'ИКБ7',
    '12.03.04 Биотехнические системы и технологии (ИИИ)': 'ИИИ5',
    '12.03.05 Лазерная техника и лазерные технологии (ИПТИП)': 'ИПТИП4',
    '12.05.01 Электронные и оптико-электронные приборы и системы специального назначения (ИПТИП)': 'ИПТИП5',
    '15.03.01 Машиностроение (ИПТИП)': 'ИПТИП6',
    '15.03.04 Автоматизация технологических процессов и производств (ИИИ)': 'ИИИ6',
    '15.03.06 Мехатроника и робототехника (ИИИ)': 'ИИИ7',
    '18.03.01 Химическая технология (ИТХТ)': 'ИТХТ2',
    '19.03.01 Биотехнология (ИТХТ)': 'ИТХТ3',
    '20.03.01 Техносферная безопасность (ИТХТ)': 'ИТХТ4',
    '22.03.01 Материаловедение и технологии материалов (ИПТИП)': 'ИПТИП7',
    '27.03.01 Стандартизация и метрология (ИПТИП)': 'ИПТИП8',
    '27.03.03 Системный анализ и управление (ИИИ)': 'ИИИ8',
    '27.03.05 Инноватика (ИТУ)': 'ИТУ2',
    '28.03.01 Нанотехнологии и микросистемная техника (ИПТИП)': 'ИПТИП9',
    '29.03.04 Технология художественной обработки материалов (ИПТИП)': 'ИПТИП10',
    '38.03.03 Управление персоналом (ИТУ)': 'ИТУ3',
    '38.03.05 Бизнес-информатика (ИТУ)': 'ИТУ4',
    '38.05.01 Экономическая безопасность (ИКБ)': 'ИКБ8',
    '40.03.01 Юриспруденция (ИТУ)': 'ИТУ5',
    '40.05.01 Правовое обеспечение национальной безопасности (ИКБ)': 'ИКБ9',
    '46.03.02 Документоведение и архивоведение (ИТУ)': 'ИТУ6',
    '54.03.01 Дизайн (ИПТИП)': 'ИПТИП11'
}
'''

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': '*/*'
}


def pushing(item, info):  # getting data from the table
    return item.find('td', class_=f'{info}').get_text(strip=True)


def get_html(url, params=None):
    return requests.get(url, headers=HEADERS, params=params)  # a function that returns the html code of the page


def get_urls(name):
    url = ''
    if name == 'ИИИ1':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416774837808438'
    elif name == 'ИИТ1':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416794849881398'
    elif name == 'ИТУ1':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416806591835446'
    elif name == 'ИКБ1':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416814830497078'
    elif name == 'ИТХТ1':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416824219446582'
    elif name == 'ИРИ1':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1714956668866964790'
    elif name == 'ИИИ2':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417222681472310'
    elif name == 'ИИТ2':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712416831985200438'
    elif name == 'ИКБ2':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417235799158070'
    elif name == 'ИРИ2':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417616938708278'
    elif name == 'ИПТИП1':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417608956947766'
    elif name == 'ИПТИП2':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1714956156281072950'
    elif name == 'ИИТ3':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417600979381558'
    elif name == 'ИИТ4':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417591424757046'
    elif name == 'ИКБ3':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417582796025142'
    elif name == 'ИИИ3':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417574615035190'
    elif name == 'ИИИ4':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417567593770294'
    elif name == 'ИКБ4':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417559840599350'
    elif name == 'ИКБ5':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417552558239030'
    elif name == 'ИКБ6':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417545906072886'
    elif name == 'ИРИ3':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417535526219062'
    elif name == 'ИРИ4':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417522705280310'
    elif name == 'ИРИ5':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417515145047350'
    elif name == 'ИПТИП3':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417506900094262'
    elif name == 'ИРИ6':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417497502756150'
    elif name == 'ИКБ7':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417490279116086'
    elif name == 'ИИИ5':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417482846809398'
    elif name == 'ИПТИП4':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417475758435638'
    elif name == 'ИПТИП5':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417468490755382'
    elif name == 'ИПТИП6':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417460785818934'
    elif name == 'ИИИ6':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417451560447286'
    elif name == 'ИИИ7':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417442958978358'
    elif name == 'ИТХТ2':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417432656719158'
    elif name == 'ИТХТ3':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417423412473142'
    elif name == 'ИТХТ4':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417415126625590'
    elif name == 'ИПТИП7':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417406008208694'
    elif name == 'ИПТИП8':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417396699999542'
    elif name == 'ИИИ8':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417388938439990'
    elif name == 'ИТУ2':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417380017155382'
    elif name == 'ИПТИП9':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417372125572406'
    elif name == 'ИПТИП10':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417363256716598'
    elif name == 'ИТУ3':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417335499861302'
    elif name == 'ИТУ4':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1714957070230400310'
    elif name == 'ИКБ8':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417306852764982'
    elif name == 'ИТУ5':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417297168117046'
    elif name == 'ИКБ9':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417286227275062'
    elif name == 'ИТУ6':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417275185769782'
    elif name == 'ИПТИП11':
        url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1712417265428770102'
    return url


def get_content(html, name_of_direction, snils):
    res = get_html(get_urls(name_of_direction))
    soup = BeautifulSoup(res.content, 'html.parser')
    items_abitur = soup.find('table', class_='namesTable').find_all('tr')
    data_based = soup.find('p', class_='lastUpdate').get_text(strip=True)  # when was the database update
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
    info = users[0]
    users = users[1:]
    user_info = [elem for elem in users if snils in elem['fio']]
    if len(user_info) == 0:
        print('There is no such person on the list. Check the entered data.')
    else:
        return user_info


def parse(snils, name_of_direction):  # a function that checks the status of a page
    html = get_html(URL_main_page)
    get_content(html.text, name_of_direction, snils)


print(parse('158-316-679-92', 'ИИИ1'))