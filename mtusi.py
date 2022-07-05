# from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# useragent = UserAgent()
url = 'https://lk.abitur.mtuci.ru/staticPage.php?page_name=spiski&ysclid=l56mnhda9t439607663'
snils = '183-443-824 81'
type_of_learning = 'Заочное обучение'
budget_or_not_budget = 'Бюджетная основа'
name_of_direction = 'Информационные системы и технологии'
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
        if snils == elem['snils']:
            for i in elem:
                print(f'{i}: {elem[i]}')
            break
    else:
        print('There is no such person on the list. Check the entered data.')


def parse():
    try:
        browser.get(url)
        # time.sleep(10)
        if type_of_learning == 'Очное обучение':
            if budget_or_not_budget == 'Бюджетная основа':
                if name_of_direction == 'Автоматизация технологических процессов и производств':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()
                elif name_of_direction == 'Инфокоммуникационные технологии и системы связи (РиТ)':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()
                elif name_of_direction == 'Инфокоммуникационные технологии и системы связи (СиСС)':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()
                elif name_of_direction == 'Информатика и вычислительная техника':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()
                elif name_of_direction == 'Информационная безопасность':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()
                elif name_of_direction == 'Информационная безопасность телекоммуникационных систем (специалитет)':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()
                elif name_of_direction == 'Информационные системы и технологии':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()
                elif name_of_direction == 'Прикладная информатика':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()
                elif name_of_direction == 'Прикладная математика':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()
                elif name_of_direction == 'Радиотехника':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()
                elif name_of_direction == 'Управление в технических системах':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()
                elif name_of_direction == 'Фундаментальные информатика и информационные технологии':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()

            elif budget_or_not_budget == 'Полное возмещение затрат (платное обучение)':
                if name_of_direction == 'Автоматизация технологических процессов и производств':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Инфокоммуникационные технологии и системы связи (РиТ)':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Инфокоммуникационные технологии и системы связи (СиСС)':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Информатика и вычислительная техника':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Информационная безопасность':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Информационная безопасность телекоммуникационных систем (специалитет)':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Информационные системы и технологии':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Прикладная информатика':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Прикладная математика':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Радиотехника':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Управление в технических системах':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Фундаментальные информатика и информационные технологии':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Экономика':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()

        elif type_of_learning == 'Заочное обучение':
            if budget_or_not_budget == 'Бюджетная основа':
                if name_of_direction == 'Автоматизация технологических процессов и производств':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[2].click()
                elif name_of_direction == 'Инфокоммуникационные технологии и системы связи':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()
                elif name_of_direction == 'Информационные системы и технологии':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[2].click()
                elif name_of_direction == 'Управление в технических системах':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[2].click()

            elif budget_or_not_budget == 'Полное возмещение затрат (платное обучение)':
                if name_of_direction == 'Автоматизация технологических процессов и производств':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[3].click()
                elif name_of_direction == 'Инфокоммуникационные технологии и системы связи':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[1].click()
                elif name_of_direction == 'Информационные системы и технологии':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[3].click()
                elif name_of_direction == 'Управление в технических системах':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[3].click()
                elif name_of_direction == 'Информатика и вычислительная техника (ускоренная форма)':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[0].click()

        elif type_of_learning == 'Очно-заочное обучение':
            if budget_or_not_budget == 'Бюджетная основа':
                if name_of_direction == 'Информатика и вычислительная техника':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[2].click()

            elif budget_or_not_budget == 'Полное возмещение затрат (платное обучение)':
                if name_of_direction == 'Информатика и вычислительная техника':
                    browser.find_elements(By.LINK_TEXT, name_of_direction)[3].click()

        get_content(get_html(), snils)

    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()


if __name__ == '__main__':
    parse()
