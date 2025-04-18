from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project")
from base.base import Base

class Main_page(Base):
    url = 'https://re-store.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)


    # locators
    service_centers_button = '/html/body/header/div[1]/div/div/div[2]/div/div[1]/a[2]'
    magazines_list_button = '/html/body/header/div[1]/div/div/div[2]/div/div[1]/a[1]'
    smartphones_and_gadgets_button = '//div[@data-campaign-id="smartfony-i-gadzhety"]'
    apple_button = '//div[@data-campaign-id="apple"]'
    magazines_header = '//h1[@class="h1 shops__title"]'
    service_centers_header = '//h1[@class="nsc-cover__title"]'


    # getters
    def get_smartphones_and_gadgets_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphones_and_gadgets_button)))

    def get_service_centers_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.service_centers_button)))

    def get_magazines_list_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.magazines_list_button)))

    def get_magazines_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.magazines_header)))

    def get_service_centers_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.service_centers_header)))

    def get_apple_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apple_button)))


    # actions
    def click_smartphones_and_gadgets_button(self):
        self.get_smartphones_and_gadgets_button().click()
        print("Click smartphones_and_gadgets_button")

    def click_service_centers_button(self):
        self.get_service_centers_button().click()
        print("Click service_centers_button")

    def click_magazines_list_button(self):
        self.get_magazines_list_button().click()
        print("Click magazines_list_button")

    def click_apple_button(self):
        self.get_apple_button().click()
        print("Click apple_button")


    # methods
    def select_smartphones_and_gadgets(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        element = self.get_smartphones_and_gadgets_button()
        self.actions.move_to_element(element).perform()
        self.click_smartphones_and_gadgets_button()
        self.check_url("https://re-store.ru/smartfony-i-gadzhety/")

    def select_apple_button(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        element = self.get_apple_button()
        self.actions.move_to_element(element).perform()
        self.click_apple_button()
        self.check_url("https://re-store.ru/apple/")

    def go_to_service_centers_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_service_centers_button()
        self.check_locator_text(self.get_service_centers_header(), "Сервисные центры\nrestore:care")

    def go_to_magazines_list_pages(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_magazines_list_button()
        self.check_locator_text(self.get_magazines_header(), "Магазины restore: в Москве")