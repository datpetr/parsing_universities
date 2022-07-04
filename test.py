# from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# useragent = UserAgent()
url = 'https://lk.abitur.mtuci.ru/staticPage.php?page_name=spiski&ysclid=l56mnhda9t439607663'
snils = '160-219-038 23'
type_of_learning = 'Очное обучение'
budget_or_not_budget = 'Бюджетная основа'
name_of_direction = 'Инфокоммуникационные технологии и системы связи (СиСС)'
options = webdriver.FirefoxOptions()

browser = webdriver.Firefox(executable_path='/home/master/PycharmProjects/'
                                            'parsing_universities/firefoxdrivers/'
                                            'geckodriver')

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
        if snils in elem['snils']:
            for i in elem:
                print(f'{i}: {elem[i]}')
            break
    else:
        print('There is no such person on the list. Check the entered data.')


def parse():
    try:
        browser.get(url)
        # print(get_html())
        browser.find_element(By.LINK_TEXT, name_of_direction).click()
        get_content(get_html(), snils)
    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()


parse()
