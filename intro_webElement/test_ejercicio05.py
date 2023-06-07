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

        iphone_link =self.driver.find_element(By.XPATH, "//a[normalize-space()='iPhone']")
        assert iphone_link.text == "iPhone", "El link debe contener el nombre Iphone"
        self.__find_text(By.XPATH,"//body//div[@id='common-home']//div[@class='row']//div[@class='row']//div[2]//div[1]//div[2]//p[2]","$123.20")

        apple_Cinema_link = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) div:nth-child(1) div:nth-child(2) h4:nth-child(1) a:nth-child(1)")
        assert apple_Cinema_link.text == 'Apple Cinema 30"', "El link debe contener el nombre Apple Cinema 30"
        self.__find_text(By.XPATH, "//span[normalize-space()='$110.00']", "$110.00")

        canon_link = self.driver.find_element(By.XPATH, "//a[normalize-space()='Canon EOS 5D']")
        assert canon_link.text == "Canon EOS 5D", "El link debe contener el nombre Canon EOS 5D"
        self.__find_text(By.XPATH, "//span[normalize-space()='$98.00']", "$98.00")



    def teardown_method(self):
        self.driver.quit()