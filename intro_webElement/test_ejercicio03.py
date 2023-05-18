import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "/Users/aaronbrn/Documents/PythonSelenium2023/drivers/chromedriver"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/index.php?route=account/login"


class TestInvalidLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_open(self):
        #Input Email
        assert self.driver.current_url == "https://laboratorio.qaminds.com/index.php?route=account/login", "URL tiene que ser para login"
        input_email = self.driver.find_element(By.XPATH, "//input[@id='input-email']")
        assert input_email.is_displayed() and input_email.is_enabled(), "El input para Email debe estar visible y habilitado"
        input_email.send_keys("jessarn18@gmail.com")
        #Input Password
        input_pwd = self.driver.find_element(By.XPATH, "//input[@id='input-password']")
        assert input_pwd.is_displayed() and input_pwd.is_enabled(), "El input para password debe estar visible y habilitado"
        input_pwd.send_keys("selenium")
        time.sleep(1)
        #Click in login
        btn_login = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        assert btn_login.is_displayed() and btn_login.is_enabled(), "El boton para hacer login debe estar visible y habilitado"
        btn_login.click()
        time.sleep(2)
        #assert alert login
        alert_login = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
        assert alert_login.is_displayed(), "Se debe visualizar la alerta de login incorrecto"
    def teardown_method(self):
        self.driver.quit()