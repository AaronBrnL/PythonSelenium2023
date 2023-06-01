import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "/Users/aaronbrn/Documents/PythonSelenium2023/drivers/chromedriver"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(5)
        self.wait_driver = WebDriverWait(self.driver, 8)
        self.driver.maximize_window()
        self.driver.get(URL)

    def __find_clickeable_element(self, by: By,value:str):
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By,value:str):
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __wait_until_disappears(self, by: By, value: str):
        self.wait_driver.until(EC.invisibility_of_element((by, value)))

    def __find_text(self, by: By,value:str, text:str):
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def test_download_and_close(self):
        btn_autocloseSucces = self.__find_clickeable_element(By.XPATH,"//button[@id='autoclosable-btn-success']")
        assert btn_autocloseSucces.is_displayed() and btn_autocloseSucces.is_enabled(), "El boton close debe estar visible y habilitado"
        btn_autocloseSucces.click()
        alert_message = self.__find_visible_element(By.XPATH,"//div[@class='row']//div[@class='col-md-6']")
        assert alert_message.is_displayed() and alert_message.is_enabled(), "El boton close debe estar visible y habilitado"
        self.__find_text(By.XPATH,"//div[@class='alert alert-success alert-autocloseable-success']","I'm an autocloseable success message. I will hide in 5 seconds.")
        time.sleep(6)
        #self.__not_visible_element(By.XPATH, "//div[@class='row']//div[@class='col-md-6']")




    def teardown_method(self):
        self.driver.quit()