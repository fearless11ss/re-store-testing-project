from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project")
from base.base import Base

class Apple_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # locators
    mac_button = '/html/body/main/div[3]/div/div[1]'

    # getters
    def get_mac_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mac_button)))

    # actions
    def click_mac_button(self):
        self.get_mac_button().click()
        print("Click mac_button")

    # methods
    def select_mac_page(self):
        element = self.get_mac_button()
        self.actions.move_to_element(element).perform()
        self.click_mac_button()