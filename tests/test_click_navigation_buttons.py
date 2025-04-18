from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project")
from pages.main_page import Main_page
from pages.smartphones_and_gadgets_page import Smartphones_and_gadgets_page
from pages.smartphones_page import Smartphones_page
from pages.cart_page import Cart_page

def test_click_service_centers_page(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service('C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project\\utilities\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)

    print("Test click_service_centers_page")
    mp = Main_page(driver)
    mp.go_to_service_centers_page()

    driver.quit()

def test_click_magazines_list_page(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service('C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project\\utilities\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)
    
    print("Test click_magazines_list_page")
    mp = Main_page(driver)
    mp.go_to_magazines_list_pages()

    driver.quit()