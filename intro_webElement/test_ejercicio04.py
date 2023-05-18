import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "/Users/aaronbrn/Documents/PythonSelenium2023/drivers/chromedriver"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class TestSelectOptiom:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_open(self):
        btn_laptop = self.driver.find_element(By.XPATH,"//a[@class='dropdown-toggle'][normalize-space()='Laptops & Notebooks']")
        assert btn_laptop.is_displayed() and btn_laptop.is_enabled(), "El Boton de laptos debe estar visible y habilitado"
        btn_laptop.click()
        btn_windows = self.driver.find_element(By.XPATH, "//a[normalize-space()='Windows (0)']")
        assert btn_windows.is_displayed() and btn_windows.is_enabled(), "El boton de windows debe estar visible y habilitado"
        btn_windows.click()
        message_empty = self.driver.find_element(By.XPATH, "//p[normalize-space()='There are no products to list in this category.']")
        assert message_empty.text == "There are no products to list in this category.", "debe haber una leyenda que indique que no hay productos"
        btn_continue = self.driver.find_element(By.XPATH, "//a[normalize-space()='Continue']")
        time.sleep(2)
        assert message_empty.is_displayed() and message_empty.is_enabled(), "el boton continuar debe estar visible y habilitado"
        btn_continue.click()
        time.sleep(2)
        element_in_home = self.driver.find_element(By.XPATH, "//h3[normalize-space()='Featured']")
        assert element_in_home.text == "Featured", "Al inicio debe haber un encabezado con el titulo Featured"




    def teardown_method(self):
        self.driver.quit()