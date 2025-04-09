from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_google_homepage():
    # Configurar opciones para headless (opcional en CI/CD)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Crear el driver usando WebDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Abrir Google y verificar el título
    driver.get("https://www.google.com")
    assert "Google" in driver.title

    # Cerrar el navegador
    driver.quit()
