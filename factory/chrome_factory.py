from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config_model import ConfigData


def create_driver(config: ConfigData):
    chrome_service = Service(config.get_drivers_path())
    chrome_options = webdriver.ChromeOptions()
    if config.is_incognito_session():
        chrome_options.add_argument("--incognito")
    if config.is_headless():
        chrome_options.add_argument("--headless")
    return webdriver.Chrome(service=chrome_service, chrome_options=chrome_options)
