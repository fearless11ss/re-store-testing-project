from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project")
from base.base import Base

class Mac_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # locators
    macbook_element = '(//a[@href="/catalog/MW1K3/"])[2]'
    add_macbook_to_cart = '/html/body/main/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div[6]/div/div[6]/button[1]'
    cart_button = '/html/body/header/div[2]/div/div[4]/div/div[4]/div/div/a'
    macbook_title = '/html/body/div[2]/main/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[1]/a'


    # getters
    def get_macbook_element(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.macbook_element)))
    def get_add_macbook_to_cart(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_macbook_to_cart)))
        except TimeoutException:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[6]/div/div[6]/button[1]')))
    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))
    def get_macbook_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.macbook_title)))

    # actions
    def click_add_macbook_to_cart(self):
        self.get_add_macbook_to_cart().click()
        print("Click add_macbook_to_cart")
    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart_button")
    

    # methods
    def select_macbook(self):
        element = self.get_macbook_element()
        self.actions.move_to_element(element).perform()
        element = self.get_add_macbook_to_cart()
        self.actions.move_to_element(element).perform()
        self.click_add_macbook_to_cart()
        self.click_cart_button()
        self.check_locator_text(self.get_macbook_title(), 'Apple MacBook Air 15" (M4, 10C CPU/10C GPU, 2025), 16 ГБ, 512 ГБ SSD, «сияющая звезда»')