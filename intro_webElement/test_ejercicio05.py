import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "/Users/aaronbrn/Documents/PythonSelenium2023/drivers/chromedriver"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_open(self):
        macbook_link = self.driver.find_element(By.XPATH, "//a[normalize-space()='MacBook']")
        assert macbook_link.text == "MacBook", "El link debe contener el nombre MacBook"
        cost_macbook = self.driver.find_element(By.XPATH, "//body//div[@id='common-home']//div[@class='row']//div[@class='row']//div[1]//div[1]//div[2]")
        assert cost_macbook.text == "Ex Tax: $500.00","Valor"

    def teardown_method(self):
        self.driver.quit()