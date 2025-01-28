from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_google_homepage():
    # Configurar opciones para headless (opcional en CI/CD)
    c_options = Options()
    #c_options.add_argument("--headless")
    c_options.add_argument("--no-sandbox")
    c_options.add_argument("--disable-dev-shm-usage")

    # Crear el driver usando WebDriverManager
    driver = webdriver.Chrome(options=c_options)

    # Abrir Google y verificar el título
    driver.get("https://www.google.com")
    assert "Google" in driver.title

    # Cerrar el navegador
    driver.quit()
