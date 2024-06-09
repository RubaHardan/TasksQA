from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class WebActions:
    def __init__(self, driver_init):
        self.driver_init = driver_init

    def navigate_to_homepage(self, xpath):
        self.driver_init.get('https://magento.softwaretestingboard.com/')
        self.driver_init.maximize_window()
        element = self.driver_init.find_element(By.XPATH, xpath)
        element.send_keys(Keys.ENTER)