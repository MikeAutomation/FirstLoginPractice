from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseActions:
    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, by_method, locator, text):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by_method, locator))
        )
        field.clear()
        field.send_keys(text)

    def click_element(self, by_method, locator):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by_method, locator))
        )
        button.click()
