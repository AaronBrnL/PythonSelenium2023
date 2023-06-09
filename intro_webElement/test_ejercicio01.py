import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_search_iphone(self):
        # Escribir Iphone
        search_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        assert search_input.is_displayed() and search_input.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        search_input.send_keys("Iphone")

        # Dar click en buscar
        search_btn = self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
        assert search_btn.is_displayed() and search_btn.is_enabled(), "El boton de busqueda tiene que estar visible y habilitado"
        search_btn.click()



        # Verificar resultados
        iphone_img = self.driver.find_element(By.XPATH, "//img[@title='iPhone']")
        assert iphone_img.is_displayed(), "La imagen de Iphone tiene que estar en el DOM"


    def teardown_method(self):
        self.driver.quit()