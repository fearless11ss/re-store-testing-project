import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

    # check url
    def check_url(self, url):
        current_url = self.driver.current_url
        assert url == current_url
        print(f"Good current url: {url}")
    
    # check text in locator
    def check_locator_text(self, locator, text):
        locator_value = locator.text
        assert text == locator_value
        print(f"Good value of locator: {text}")
    
    # take screenshot
    def take_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        screenshot_name = 'screenshot'+now_date+'.png'
        self.driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\Программирование\\re_store testing project\\screen\\'+screenshot_name)