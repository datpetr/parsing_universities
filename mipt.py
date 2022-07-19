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

# dict_competitive_group = {
#     'ФПМИ Прикладная математика и информатика': 423,
#     "ФПМИ Экономика и ERP": 424,
#     "ФПМИ Прикладная математика и информатика Иностранные граждане": 425,
#     "Computer science for foreign citizens": 426,
#     'Computer science': 427,
#     "В рамках квоты правительства РФ (направление ПМИ)": 458,
#     "ФПМИ Прикладная математика и информатика (Предприятия Минпромторга)": 699,
#     'ФПМИ Прикладная математика и информатика (ПАО "ГАЗПРОМ НЕФТЬ")': 700
# }

dict_competitive_group = {
    'ФПМИ Прикладная математика и информатика': 423,
    "ФПМИ Экономика и ERP": 424,
    "ФПМИ Прикладная математика и информатика Иностранные граждане": 425,
    "Computer science for foreign citizens": 426,
    'Computer science': 427,
    "В рамках квоты правительства РФ (направление ПМИ)": 458,
    "ФПМИ Прикладная математика и информатика (Предприятия Минпромторга)": 699,
    'ФПМИ Прикладная математика и информатика (ПАО "ГАЗПРОМ НЕФТЬ")': 700,
    'ФРКТ Радиотехника и компьютерные технологии': 428,
    'ФРКТ Радиотехника и компьютерные технологии Иностранные граждане': 429,
    'ЛФИ Общая и прикладная физика': 430,
    'ЛФИ Общая и прикладная физика Иностранные граждане': 431,
    'ФАКТ Авиационные технологии': 434,
    'ФАКТ Геокосмические науки и технологии': 435,
    'ФАКТ Аэрокосмические технологии Иностранные граждане': 436,
    'ФЭФМ Физика перспективных технологий': 437,
    'ФЭФМ Физика перспективных технологий Иностранные граждане': 438,
    'ФПМИ Прикладная математика и компьютерные технологии (ПМФ)': 440,
    'ФПМИ Прикладная математика и компьютерные технологии Иностранные граждане': 441,
    'ФБМФ Биофизика и биоинформатика': 443,
    'ФБМФ Биофизика и биоинформатика Иностранные граждане': 444,
    'ИНБИКСТ Конвергентные НБИК-технологии и мегасайенс': 445,
    'В рамках квоты правительства РФ (направление ПМФ)': 459,
    'ФБВТ Управление инновациями в бизнесе (ПМФ)': 686,
    'ФРКТ Радиотехника и компьютерные технологии (Предприятия Минпромторга)': 701,
    'ФАКТ Авиационные технологии (Предприятия Минпромторга)': 702,
    'ФАКТ Геокосмические науки и технологии (Предприятия Минпромторга)': 703,
    'ФАКТ Геокосмические науки и технологии (Предприятия Роскосмоса)': 704,
    'ФЭФМ Физика перспективных технологий (Предприятия Минпромторга)': 705,
    'ФПМИ Прикладная математика и компьютерные технологии (ПМФ) (Предприятия Минпромторга)': 706,
    'ФБМФ Биофизика и биоинформатика (ГК Ростех)': 707,
    'ФАКТ Компьютерное моделирование': 446,
    'ФАКТ Компьютерное моделирование Иностранные граждане': 447,
    'ФПМИ Системное программирование и прикладная математика': 448,
    'ФПМИ Системное программирование и прикладная математика Иностранные граждане': 449,
    'В рамках квоты правительства РФ (направление ИВТ)': 460,
    'ФПМИ Прикладная математика и компьютерные технологии (ИВТ)': 610,
    'ВШПИ Программная инженерия (грантовые места, аналогичные бюджетным)': 687,
    'ФАКТ Компьютерное моделирование (Предприятия Роскосмоса)': 708,
    'ФАКТ Компьютерное моделирование (Предприятия Минпромторга)': 709,
    'ФПМИ Прикладная математика и компьютерные технологии (ИВТ) (АО «АТОМТЕХЭНЕРГО»)': 710,
    'ФЭФМ Электроника и наноэлектроника': 618,
    'В рамках квоты Правительства РФ (направление ЭНЭ)': 631,
    'ФАКТ Техническая физика': 450,
    'В рамках квоты правительства РФ (направление ТФ)': 461,
    'ФБМФ Биотехнология': 453,
    'ФБМФ Биотехнология Иностранные граждане': 454,
    'Biomedical engineering for foreign citizens': 455,
    'В рамках квоты правительства РФ (направление БТ)': 462,
    'ФБВТ Управление инновациями в бизнесе (БТ)': 689,
    'ФАКТ Системный анализ и управление': 456,
    'В рамках квоты правительства РФ (направление САУ)': 463,
    'ФБВТ Управление инновациями в бизнесе (САУ)': 688,
    'ФАКТ Системный анализ и управление (Предприятия Минпромторга)': 711,
    'Компьютерная безопасность': 457,
    'ФРКТ Компьютерная безопасность (Предприятия Минпромторга)': 712,
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

snils = '176-727-614 09'
admission_condition = str(dict_admission_condition['Общий конкурс'])
direction = str(dict_direction['10.05.01 Компьютерная безопасность'])
competitive_group = str(dict_competitive_group['Компьютерная безопасность'])
basis_of_learning = str(dict_basis_of_learning["Бюджетное обучение"])
order_of_admission = str(dict_order_of_admission["включая"])

# snils = input('Введите СНИЛС: ')
# admission_condition = str(dict_admission_condition[input('Условия поступления: ')])
# direction = str(dict_direction[input('Направление: ')])
# competitive_group = str(dict_competitive_group[input('Конкурсная группа: ')])
# basis_of_learning = str(dict_basis_of_learning[input('Основа обучения: ')])
# order_of_admission = str(dict_order_of_admission[input('Включенные в приказ о зачислении: ')])


def get_html():
    return BeautifulSoup(browser.page_source, 'lxml')


def pushing(item, info):  # getting data from the table
    if info != '':
        if info == 'sum':
            return item.find_elements('td', class_=f'{info}')[1].get_text(strip=True)
        else:
            return item.find('td', class_=f'{info}').get_text(strip=True) if item.find('td', class_=f'{info}') != 'NoneType' else 'Копия отсутствует'
    # return item.find('td', class_=f'{info}').get_text(strip=True)


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
            'education_document': (a[11] if a[11] != '' else 'Копия отсутствует'),
        })

    # for item in items_applicants:
    #     applicants.append({
    #         'num': pushing(item, '№'),
    #         'priority': pushing(item, 'Приоритет заявления'),
    #         'snils': pushing(item, 'text-center'),
    #         'sum_of_points_with_id': pushing(item, 'sum'),
    #         'education_document': pushing(item, 'education'),
    #     })

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
        # if admission_condition == 1:  # условия поступления
        #     browser.find_elements(by=By.XPATH,
        #                           value='//option[@value="1"]')[0].click()
        # elif admission_condition == 2:
        #     browser.find_elements(by=By.XPATH,
        #                           value='//option[@value="2"]')[0].click()
        # elif admission_condition == 3:
        #     browser.find_elements(by=By.XPATH,
        #                           value='//option[@value="3"]')[0].click()
        # elif admission_condition == 4:
        #     browser.find_elements(by=By.XPATH,
        #                           value='//option[@value="4"]')[0].click()
        # elif admission_condition == 5:
        #     browser.find_elements(by=By.XPATH,
        #                           value='//option[@value="5"]')[0].click()
        # else:
        #     browser.find_elements(by=By.XPATH,
        #                           value=f'//option[@value="{str(admission_condition)}"]')[0].click()
        if admission_condition != '':
            browser.find_elements(by=By.XPATH,
                                  value=f'//option[@value="{admission_condition}"]')[0].click()

        if direction in '12345':
            browser.find_elements(by=By.XPATH,
                                  value=f'//option[@value="{direction}"]')[1].click()
        elif direction in '6729':
            browser.find_elements(by=By.XPATH,
                                  value=f'//option[@value="{direction}"]')[0].click()
        # if direction == 1:  # направления
        #     browser.find_elements(by=By.XPATH,
        #                           value='//option[@value="1"]')[1].click()
        # elif direction == 2:
        #     browser.find_elements(by=By.XPATH,
        #                           value='//option[@value="2"]')[1].click()
        # elif direction == 4:
        #     browser.find_elements(by=By.XPATH,
        #                           value='//option[@value="4"]')[1].click()
        # elif direction == 5:
        #     browser.find_elements(by=By.XPATH,
        #                           value='//option[@value="5"]')[1].click()
        # else:
        #     browser.find_elements(by=By.XPATH,
        #                           value=f'//option[@value="{str(direction)}"]')[1].click()

        browser.find_element(by=By.XPATH,  # конкурсная группа
                             value=f'//option[@value="{competitive_group}"]').click()
        # browser.find_element(by=By.XPATH,
        #                      value='//input[@id="competition_list_agreement"]').click()

        # if basis_of_learning == 1:  # основа обучения
        #     browser.find_elements(by=By.XPATH,
        #                           value='//option[@value="1"]')[2].click()
        # elif basis_of_learning == 2:
        #     browser.find_elements(by=By.XPATH,
        #                           value='//option[@value="2"]')[2].click()

        browser.find_elements(by=By.XPATH,  # основа обучения
                              value=f'//option[@value="{basis_of_learning}"]')[2].click()

        if order_of_admission != '':  # включение приказа о зачислении
            browser.find_element(by=By.XPATH,
                                 value=f'//option[@value="{order_of_admission}"]').click()

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
