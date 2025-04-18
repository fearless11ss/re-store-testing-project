from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project")
from base.base import Base
import time

class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # locators
    checkout_button = '//button[@id="cartButton"]'

    # getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # actions
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout_button")

    # methods
    def checkout(self):
        self.click_checkout_button()
        time.sleep(7)
        self.take_screenshot()