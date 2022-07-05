from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
import time

url = 'https://pk.mipt.ru/bachelor/competition-list/'
snils = '171-981-748 05 '
admission_condition = 'Общий конкурс'
direction = '01.03.02 Прикладная математика и информатика'
competitive_group = 'ФПМИ Прикладная математика и информатика'
basis_of_learning = "Бюджетное обучение"
order_of_admission = "включая"
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


def get_html():
    return BeautifulSoup(browser.page_source, 'lxml')


def get_content(html, snils):
    applicants = []
    items_applicants = html.find('tbody').find_all('tr')
    for item in items_applicants:
        a = []
        for elem in item.find_all('td'):
            a.append(elem.get_text(strip=True))
        applicants.append({
            'num': a[0],
            'reception_category': a[1],
            'snils': a[2],
            'individual_achievements': a[7],
            'sum_of_points': a[8],
            'type_of_vi': a[9],
            'original': a[10],
            'consent_to_enrollment': a[11],
            'the_need_for_a_hostel': a[12]
        })

    for elem in applicants:
        if snils == elem['snils']:
            for i in elem:
                print(f'{i}: {elem[i]}')
            break
    else:
        print('There is no such person on the list. Check the entered data.')


def parse():
    try:
        browser.get(url)
        # find_element(By.CLASS_NAME, 'btn btn-block btn-primary').click()

        browser.find_elements(by=By.XPATH,
                              value='//option[@value="1"]')[0].click()  # условия поступления
        browser.find_elements(by=By.XPATH,
                              value='//option[@value="1"]')[1].click()  # направления

        browser.find_element(by=By.XPATH,
                             value='//option[@value="423"]').click()  # конкурсная группа
        # browser.find_element(by=By.XPATH,
        #                      value='//input[@id="competition_list_agreement"]').click()
        browser.find_elements(by=By.XPATH,
                              value='//option[@value="1"]')[2].click()  # основа обучения
        browser.find_element(by=By.XPATH,
                             value='//option[@value="include"]').click()  # включение приказа о зачислении

        browser.find_element(by=By.XPATH,
                             value='//div[@class="btn btn-block btn-primary"]').click()  # кнопка "поступить"
        time.sleep(10)
        # get_content(get_html(), snils)

    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()


if __name__ == '__main__':
    parse()
