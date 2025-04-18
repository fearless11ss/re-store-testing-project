from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project")
from base.base import Base

class Smartphones_and_gadgets_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # locators
    smartphones_button = '/html/body/main/div[3]/div/div[1]/div/a'

    # getters
    def get_smartphones_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphones_button)))

    # actions
    def click_smartphones_button(self):
        self.get_smartphones_button().click()
        print("Click smartphones_button")

    # methods
    def select_smartphones(self):
        element = self.get_smartphones_button()
        self.actions.move_to_element(element).perform()
        self.click_smartphones_button()