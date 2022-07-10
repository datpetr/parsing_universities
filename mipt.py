from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

url = 'https://pk.mipt.ru/bachelor/competition-list/'
options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) "
                                                     "Gecko/20100101 Firefox/103.0")
browser = webdriver.Firefox(executable_path='/home/master/PycharmProjects/'
                                            'parsing_universities/firefoxdrivers/'
                                            'geckodriver',
                            options=options
                            )

dict_admission_condition = {
    'Общий конкурс': 1,
    'Бюджет. Без вступительных испытаний': 2,
    'Целевая квота': 3,
    'Особая квота (инвалиды, сироты и пр.)': 4,
    'В рамках квоты правительства РФ': 5,
    "Контракт. Без вступительных испытаний": 8
}

dict_direction = {
    '01.03.02 Прикладная математика и информатика': 1,
    '03.03.01 Прикладные математика и физика': 2,
    '09.03.01 Информатика и вычислительная техника': 3,
    '16.03.01 Техническая физика': 4,
    '19.03.01 Биотехнология': 5,
    '27.04.03 Системный анализ и управление': 6,
    '10.05.01 Компьютерная безопасность': 7,
    '11.03.04 Электроника и наноэлектроника': 29
}

dict_competitive_group = {
    'ФПМИ Прикладная математика и информатика': 423,
    "ФПМИ Экономика и ERP": 424,
    "ФПМИ Прикладная математика и информатика Иностранные граждане": 425,
    "Computer science for foreign citizens": 426,
    'Computer science': 427,
    "В рамках квоты правительства РФ (направление ПМИ)": 458,
    "ФПМИ Прикладная математика и информатика (Предприятия Минпромторга)": 699,
    'ФПМИ Прикладная математика и информатика (ПАО "ГАЗПРОМ НЕФТЬ")': 700
}

dict_basis_of_learning = {
    "Контрактное обучение": 1,
    "Бюджетное обучение": 2
}

dict_order_of_admission = {
    "включая": "include",
    "исключая": "exclude",
    "только": "only"
}

dict_translate_for_output = {
    'num': '№',
    'priority': 'Приоритет',
    'snils': 'СНИЛС',
    'sum_of_points_with_id': 'Cумма баллов с ид',
    'education_document': 'Документ об оброзовании'
}

# snils = '171-981-748 05'
# admission_condition = dict_admission_condition['Общий конкурс']
# direction = dict_direction['01.03.02 Прикладная математика и информатика']
# competitive_group = dict_competitive_group['ФПМИ Прикладная математика и информатика']
# basis_of_learning = dict_basis_of_learning["Бюджетное обучение"]
# order_of_admission = dict_order_of_admission["включая"]

snils = input('Введите СНИЛС: ')
admission_condition = dict_admission_condition[input('Условия поступления: ')]
direction = dict_direction[input('Направление: ')]
competitive_group = dict_competitive_group[input('Конкурсная группа: ')]
basis_of_learning = dict_basis_of_learning[input('Основа обучения: ')]
order_of_admission = dict_order_of_admission[input('Включенные в приказ о зачислении: ')]


def get_html():
    return BeautifulSoup(browser.page_source, 'lxml')


def get_content(html, snils):
    applicants = []
    items_applicants = html.find('tbody', 'entrant-list-body').find_all('tr')

    for item in items_applicants:
        a = []
        for elem in item.find_all('td'):
            a.append(elem.get_text(strip=True))

        applicants.append({
            'num': a[0],
            'priority': a[1],
            'snils': a[2],
            'sum_of_points_with_id': a[8],
            'education_document': a[11],
        })

    for elem in applicants:
        if snils == elem['snils']:
            for i in elem:
                print(f'{dict_translate_for_output[i]}: {elem[i]}')
            break
    else:
        print('There is no such person on the list. Check the entered data.')


def parse():
    try:
        browser.get(url)
        # find_element(By.CLASS_NAME, 'btn btn-block btn-primary').click()
        if admission_condition == 1:  # условия поступления
            browser.find_elements(by=By.XPATH,
                                  value='//option[@value="1"]')[0].click()
        elif admission_condition == 2:
            browser.find_elements(by=By.XPATH,
                                  value='//option[@value="2"]')[0].click()
        elif admission_condition == 3:
            browser.find_elements(by=By.XPATH,
                                  value='//option[@value="3"]')[0].click()
        elif admission_condition == 4:
            browser.find_elements(by=By.XPATH,
                                  value='//option[@value="4"]')[0].click()
        elif admission_condition == 5:
            browser.find_elements(by=By.XPATH,
                                  value='//option[@value="5"]')[0].click()
        else:
            browser.find_elements(by=By.XPATH,
                                  value=f'//option[@value="{str(admission_condition)}"]')[0].click()

        if direction == 1:  # направления
            browser.find_elements(by=By.XPATH,
                                  value='//option[@value="1"]')[1].click()
        elif direction == 2:
            browser.find_elements(by=By.XPATH,
                                  value='//option[@value="2"]')[1].click()
        elif direction == 4:
            browser.find_elements(by=By.XPATH,
                                  value='//option[@value="4"]')[1].click()
        elif direction == 5:
            browser.find_elements(by=By.XPATH,
                                  value='//option[@value="5"]')[1].click()
        else:
            browser.find_elements(by=By.XPATH,
                                  value=f'//option[@value="{str(direction)}"]')[1].click()

        browser.find_element(by=By.XPATH,
                             value=f'//option[@value="{competitive_group}"]').click()  # конкурсная группа
        # browser.find_element(by=By.XPATH,
        #                      value='//input[@id="competition_list_agreement"]').click()

        if basis_of_learning == 1:  # основа обучения
            browser.find_elements(by=By.XPATH,
                                  value='//option[@value="1"]')[2].click()
        elif basis_of_learning == 2:
            browser.find_elements(by=By.XPATH,
                                  value='//option[@value="2"]')[2].click()

        browser.find_element(by=By.XPATH,
                             value=f'//option[@value="{order_of_admission}"]').click()  # включение приказа о зачислении

        browser.find_element(by=By.XPATH,
                             value='//div[@class="btn btn-block btn-primary"]').click()  # кнопка "поступить"
        time.sleep(1)
        get_content(get_html(), snils)

    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()


if __name__ == '__main__':
    parse()