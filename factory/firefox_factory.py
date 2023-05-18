from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from config.config_model import ConfigData


def create_driver(config: ConfigData):
    service = Service(config.get_drivers_path())
    ff_options = webdriver.FirefoxOptions()
    ff_profile = webdriver.FirefoxProfile()
    ff_profile.set_preference("browser.privatebrowsing.autostart", config.is_headless())
    ff_options.headless = config.is_headless()
    return webdriver.Firefox(service=service, options=ff_options, firefox_profile=ff_profile)
