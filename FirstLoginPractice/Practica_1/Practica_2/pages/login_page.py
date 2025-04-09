from Practica_1.Practica_2.utils.base_functions import BaseActions
from selenium.webdriver.common.by import By

class LoginPage(BaseActions):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.email_field = (By.NAME, "Email")
        self.password_field = (By.NAME, "Password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, email, password):
        self.enter_text(*self.email_field, email)
        self.enter_text(*self.password_field, password)
        self.click_element(*self.login_button)