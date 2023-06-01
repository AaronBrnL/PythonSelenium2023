import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "/Users/aaronbrn/Documents/PythonSelenium2023/drivers/chromedriver"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(5)
        self.wait_driver = WebDriverWait(self.driver, 8)
        self.driver.maximize_window()
        self.driver.get(URL)

    def __find_text(self, by: By,value:str, text:str):
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))
    def test_open(self):
        macbook_link = self.driver.find_element(By.XPATH, "//a[normalize-space()='MacBook']")
        assert macbook_link.text == "MacBook", "El link debe contener el nombre MacBook"
        self.__find_text(By.XPATH, "//body//div[@id='common-home']//div[@class='row']//div[@class='row']//div[1]//div[1]//div[2]","$602.00")


    def teardown_method(self):
        self.driver.quit()