from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project")
from pages.main_page import Main_page
from pages.smartphones_and_gadgets_page import Smartphones_and_gadgets_page
from pages.smartphones_page import Smartphones_page
from pages.cart_page import Cart_page
from pages.apple_page import Apple_page
from pages.mac_page import Mac_page

def test_buy_samsung_galaxy_s25_12_256_mint(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service('C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project\\utilities\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)

    mp = Main_page(driver)
    mp.select_smartphones_and_gadgets()

    sgp = Smartphones_and_gadgets_page(driver)
    sgp.select_smartphones()

    sp = Smartphones_page(driver)
    sp.add_smartphone_to_cart()

    cp = Cart_page(driver)
    cp.checkout()

    driver.quit()

def test_buy_macbook(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service('C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project\\utilities\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)
    
    mp = Main_page(driver)
    mp.select_apple_button()

    ap = Apple_page(driver)
    ap.select_mac_page()

    mac_page = Mac_page(driver)
    mac_page.select_macbook()

    cp = Cart_page(driver)
    cp.checkout()

    driver.quit()