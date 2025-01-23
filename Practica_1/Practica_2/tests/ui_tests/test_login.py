import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from Practica_1.Practica_2.pages.login_page import LoginPage

import time


@pytest.fixture
def driver():
    chrome_options = Options()
    # Crea un directorio temporal único para evitar conflictos
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin%2FProduct%2FCreate")
    return LoginPage(driver)

@allure.feature("Login")
@allure.story("Successful Login")
def test_login_success(driver, login_page):
    with allure.step("Enter valid credentials"):
        login_page.login("admin@yourstore.com", "admin")
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Login Page Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    with allure.step("Verify dashboard title"):
        assert "Just a moment" in driver.title

@allure.story("Rejected Login Wrong User")
def test_login_wruser(driver, login_page):
    login_page.login("admin", "admin")
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Email-error"))
    )
    allure.attach(
            driver.get_screenshot_as_png(),
            name="Faile Login WrUsr Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    assert error_message.text == "Please enter a valid email address."

@allure.story("Rejected Login Empty Values")
def test_login_empty(driver, login_page):
    login_page.login("", "")
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Email-error"))
    )
    allure.attach(
            driver.get_screenshot_as_png(),
            name="Faile LogIn Emptys Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    assert error_message.text == "Please enter your email"