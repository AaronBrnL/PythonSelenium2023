#ir a la pagina https://laboratorio.qaminds.com/
#Srcipt
#a Seleccione la opcion Tablets
#b Deberá aparecer un item con titulo: Samsung Galaxy Tab 10.1
#c Seleccionar dicho item
#d Verificar que:
#El costo del item es de ¢241.99
#Puede agergarlo a una wish list
#Puede agregarlo al Carrito

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "/Users/aaronbrn/Documents/PythonSelenium2023/drivers/chromedriver"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"
class TestSamsungLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(URL)

    def test_search_tablets(self):
        #Busca el boton Table y le da click
        #Seleccione la opcion Tablets
        tablet_btn = self.driver.find_element(By.XPATH, "//a[normalize-space()='Tablets']")
        assert tablet_btn.is_displayed() and tablet_btn.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        tablet_btn.click()


        #Busca Samsung Galaxy Tab 10.1
        #Debera aparecer un item con titulo: Samsung Galaxy Tab 10.1
        name_product = self.driver.find_element(By.XPATH, "//a[normalize-space()='Samsung Galaxy Tab 10.1']")
        assert name_product.is_displayed(), "El producto debe estar visible"
        assert name_product.text == "Samsung Galaxy Tab 10.1", "El producto debe tener el titulo Samsung Galaxy Tab 10.1"
        #Selecciona el item
        name_product.click()

        #Verifique que:
        #El costo del item es de $241.99
        cost_product = self.driver.find_element(By.XPATH, "//h2[normalize-space()='$241.99']")
        assert cost_product.is_displayed(), "El producto debbe estar visible"
        assert cost_product.text == "$241.99", "El producto debe tener el costo de $241.99"
        #Puede agregarlo a una Wishlist
        btn_wishlist = self.driver.find_element(By.XPATH, "//div[@id='product-product']//div[@class='btn-group']//button[1]")
        assert btn_wishlist.is_displayed() and btn_wishlist.is_enabled(), "El boton para agregar a la Wishlist debe estar visible y hablitado"
        btn_wishlist.click()
        time.sleep(1)
        alert_wishlist = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
        assert alert_wishlist.is_displayed(), "Se debe mostrar una alerta de inicio de sesión"
        create_an_account_alert = self.driver.find_element(By.XPATH, "//a[normalize-space()='create an account']")
        assert create_an_account_alert.text == "create an account", "La alerta debe mencionar que primero inicies sesión"

        #Puede agregarlo al carrito
        btn_cart = self.driver.find_element(By.XPATH, "//button[@id='button-cart']")
        assert btn_cart.is_displayed() and btn_cart.is_enabled(), "El boton para agregar al Carrito debe estar visible y habilitado"
        btn_cart.click()
        time.sleep(1)
        btn_cart_items = self.driver.find_element(By.XPATH, "//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
        assert btn_cart_items.is_displayed() and btn_cart_items.is_enabled(), "El boton para ver el Carrito debe estar visible y habilitado"
        assert btn_cart_items.text == "1 item(s) - $241.99"
        btn_cart_items.click()

        #time.sleep(5)

        pass

    def teardown_method(self):
        self.driver.quit()