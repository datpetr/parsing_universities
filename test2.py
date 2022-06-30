import requests
from bs4 import BeautifulSoup

dict_admission_condition = {
    '1': 'Общий конкурс',
    '2': 'Бюджет. Без вступительных испытаний',
    '3': 'Целевая квота',
    '4': 'Особая квота (инвалиды, сироты и пр.)',
    '5': 'В рамках квоты правительства РФ',
    '6': "Контракт. Без вступительных испытаний"
}

print('Условие поступления:' '\n'
      '\t' '- Общий конкурс: 1' '\n'
      '\t' '- Бюджет. без вступительных: 2' '\n'
      '\t' '- Целевая квота: 3' '\n'
      '\t' '- Особая квота: 4' '\n'
      '\t' '- В рамках квота: 5' '\n'
      '\t' '- Контракт: 6' '\n')

input_data_admission_condition = input('Введите нужный индекс: ')


print('\n' 'Направления:' '\n'
      '\t' '- ПМИ: 1' '\n'
      '\t' '- ПМФ: 2' '\n'
      '\t' '- ИВТ: 3' '\n'
      '\t' '- ЭН: 4' '\n'
      '\t' '- ТФ: 5' '\n'
      '\t' '- САУ: 6' '\n'
      '\t' '- КБ: 7' '\n')

input_data_direction = input('Введите нужный индекс: ')


print('\n' 'Основа обучения:' '\n'
      '\t' '- Контракт: 1' '\n'
      '\t' '- Бюджет: 2' '\n')

input_data_competitive_group = input('Введите нужный индекс: ')


print('\n' 'Включенные в приказ о зачислении:' '\n'
      '\t' '- Включая: 1' '\n'
      '\t' '- Исключая: 2' '\n'
      '\t' '- Только: 3' '\n')

input_data_order_of_admission = input('Введите нужный индекс: ')

url = 'https://pk.mipt.ru/bachelor/competition-list/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find('span', class_='logo-text')
print(quotes.text.strip())
