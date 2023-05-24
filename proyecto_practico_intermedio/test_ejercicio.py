from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

URL = "https://laboratorio.qaminds.com/"


class TestProyectoPractico:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)
        self.wait_driver = WebDriverWait(self.driver, 5)

    def __find_click_element(self, by: By,value:str):
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By,value:str):
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __find_text(self, by: By,value:str, text:str):
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def test_ejercicio02(self):
        # Escribir Display
        search_input = self.__find_click_element(By.XPATH, "//input[@placeholder='Search']")
        assert search_input.is_displayed() and search_input.is_enabled(), "El cuadro de texto debe ser visible y habilitado"
        search_input.send_keys("Display")
        time.sleep(1)

        #Click lupa
        search_input_btn = self.__find_click_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
        assert search_input_btn.is_displayed() and search_input_btn.is_enabled(), "El boton de busqueda debe ser visible y habilitado"
        search_input_btn.click()
        time.sleep(1)

        #verificar leyenda sobre no hay productos
        self.__find_text(By.XPATH, "//p[contains(text(),'There is no product that matches the search criter')]","There is no product that matches the search criteria.")
        time.sleep(1)

        #click en checkbox buscar por descripción
        search_description = self.__find_click_element(By.ID,"description")
        assert search_description.is_displayed() and search_description.is_enabled(),"debe mostrarse el checkbox y estar habilitado"
        search_description.click()
        time.sleep(1)

        #click en el boton de busqueda
        search_btn = self.__find_click_element(By.ID, "button-search")
        search_btn.click()
        time.sleep(1)

        #elementos encontrados
        self.__find_text(By.CSS_SELECTOR,"div[id='content'] div:nth-child(1) div:nth-child(1) div:nth-child(2) div:nth-child(1) h4:nth-child(1) a:nth-child(1)","Apple Cinema 30")
        self.__find_text(By.CSS_SELECTOR,"body > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(8) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h4:nth-child(1) > a:nth-child(1)","iPod Nano")
        self.__find_text(By.CSS_SELECTOR,"body div[id='product-search'] div[class='row'] div[class='row'] div:nth-child(3) div:nth-child(1) div:nth-child(2) div:nth-child(1) h4:nth-child(1) a:nth-child(1)","iPod Touch")
        self.__find_text(By.CSS_SELECTOR,"body > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(8) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h4:nth-child(1) > a:nth-child(1)","MacBook Pro")
        time.sleep(1)

    def test_ejercicio03(self):
        #Click en boton Desktop
        desktop_btn = self.__find_click_element(By.XPATH, "//a[normalize-space()='Desktops']")
        desktop_btn.click()
        time.sleep(1)
        #element = self.driver.find_element(By.XPATH, "//a[normalize-space()='Desktops']")
        #select = Select(element)
        #select.select_by_visible_text("Mac (1)")
        #Selecciona porducto Mac
        mac_btn = self.__find_click_element(By.XPATH,"//a[normalize-space()='Mac (1)']")
        product = self.__find_click_element(By.XPATH,"//div[@class='caption']//h4")
        assert product.is_displayed(),"El producto es visible"
        mac_btn.click()
        time.sleep(1)
        #Agregar producto al carrito
        btn_cart = self.__find_click_element(By.XPATH,"//div[@class='product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12']//button[1]")
        btn_cart.click()
        time.sleep(1)
        #Verifica el valor en el carrito
        self.__find_text(By.XPATH,"//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']","1 item(s) - $122.00")

    def test_ejercicio04(self):
        #valor $
        self.__find_text(By.XPATH, "//strong[normalize-space()='$']", "$")
        time.sleep(1)
        # Escribir Samsung
        search_input = self.__find_click_element(By.XPATH, "//input[@placeholder='Search']")
        assert search_input.is_displayed() and search_input.is_enabled(), "El cuadro de texto debe ser visible y habilitado"
        search_input.send_keys("Samsung SyncMaster 941BW")
        time.sleep(1)

        # Click lupa
        search_input_btn = self.__find_click_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
        assert search_input_btn.is_displayed() and search_input_btn.is_enabled(), "El boton de busqueda debe ser visible y habilitado"
        search_input_btn.click()
        time.sleep(1)

        #Value $ samsung
        self.__find_text(By.CSS_SELECTOR, ".price","$242.00")
        time.sleep(1)

        #Mod Valor Currency
        currency = self.__find_click_element(By.XPATH,"//button[@class='btn btn-link dropdown-toggle']")
        currency.click()
        euro = self.__find_click_element(By.XPATH, "//li[1]//button[1]")
        euro.click()
        time.sleep(1)
        #Value € samsung
        self.__find_text(By.CSS_SELECTOR, ".price", "189.87€")
        time.sleep(1)


    def teardown_method(self):
        self.driver.quit()