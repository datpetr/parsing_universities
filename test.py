from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

url = 'https://lk.abitur.mtuci.ru/staticPage.php?page_name=spiski&ysclid=l56mnhda9t439607663'
snils = '171-800-133 31'
# useragent = UserAgent()
options = webdriver.FirefoxOptions()
browser = webdriver.Firefox(executable_path='/home/master/PycharmProjects/'
                                            'parsing_universities/firefoxdrivers/'
                                            'geckodriver')


def pushing(item, info):  # getting data from the table
    return item.find('td', class_=f'{info}').get_text(strip=True)


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
        browser.find_element(By.LINK_TEXT, 'Информатика и вычислительная техника').click()
        get_content(get_html(), snils)
    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()


if __name__ == '__main__':
    parse()