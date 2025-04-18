from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project")
from base.base import Base

class Smartphones_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # locators
    smartphone_element = '/html/body/main/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[10]'
    add_smartphone_to_cart_button = '/html/body/main/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[10]/div/div[6]/button[1]'
    cart_button = '/html/body/header/div[2]/div/div[4]/div/div[4]/div/div/a'
    smartphone_title = '/html/body/div[2]/main/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[1]/a'

    # getters
    def get_smartphone_element(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphone_element)))
    def get_add_smartphone_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_smartphone_to_cart_button)))
    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))
    def get_smartphone_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphone_title)))

    # actions
    def click_add_smartphone_to_cart_button(self):
        self.get_add_smartphone_to_cart_button().click()
        print("Click add_smartphone_to_cart_button")
    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart_button")

    # methods
    def add_smartphone_to_cart(self):
        element = self.get_smartphone_element()
        self.actions.move_to_element(element).perform()
        self.click_add_smartphone_to_cart_button()
        self.click_cart_button()
        self.check_locator_text(self.get_smartphone_title(), "Смартфон Samsung Galaxy S25 12 ГБ/512 ГБ, Мятный")