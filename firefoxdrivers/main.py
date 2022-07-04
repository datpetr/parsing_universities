from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


url = 'https://lk.abitur.mtuci.ru/staticPage.php?page_name=spiski&ysclid=l56mnhda9t439607663'
options = webdriver.FirefoxOptions()
options.add_argument('user-agent=HelloWorld')
browser = webdriver.Firefox(executable_path='/home/master/PycharmProjects/'
                                            'parsing_universities/firefoxdrivers/'
                                            'geckodriver',
                            options=options)


try:
    browser.get(url)
    browser.find_element(By.LINK_TEXT, 'Информатика и вычислительная техника').click()
    time.sleep(10)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    print(soup)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
