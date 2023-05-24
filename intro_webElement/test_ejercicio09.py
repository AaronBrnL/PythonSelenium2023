import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "/Users/aaronbrn/Documents/PythonSelenium2023/drivers/chromedriver"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(5)
        self.wait_driver = WebDriverWait(self.driver, 120)
        self.driver.maximize_window()
        self.driver.get(URL)

    def __find_clickeable_element(self, by: By,value:str):
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By,value:str):
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __find_text(self, by: By,value:str, text:str):
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def test_download_and_close(self):
        download_btn = self.__find_clickeable_element(By.XPATH,"//button[@id='downloadButton']")
        download_btn.click()
        self.__find_text(By.XPATH, "//div[@class='progress-label']", "Complete!")
        close_btn = self.__find_visible_element(By.XPATH,"//button[normalize-space()='Close']")
        assert close_btn.is_displayed() and close_btn.is_enabled(), "El boton close debe estar visible y habilitado"

    def teardown_method(self):
        self.driver.quit()