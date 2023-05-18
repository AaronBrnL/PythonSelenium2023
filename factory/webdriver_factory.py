from selenium.webdriver.remote.webdriver import WebDriver

from config.config_handler import ConfigHandler
from config.config_model import DriverType, ConfigData
from factory.chrome_factory import create_driver as create_chrome_driver
from factory.firefox_factory import create_driver as create_firefox_driver


def get_driver(overwrite_config_path: str = None) -> WebDriver:
    """Get driver based on driver type.

    :param overwrite_config_path: User custom configuration file
    :return: Web driver instance
    """
    config_handler = ConfigHandler(overwrite_config_path)
    config = config_handler.load_config()
    return __get_driver(config)


def __get_driver(config: ConfigData) -> WebDriver:
    if type(config.get_driver_type()) is not DriverType:
        raise TypeError(f"Cannot create driver, invalid type provided: {type(config.get_driver_type())}")
    if config.get_driver_type() == DriverType.CHROME:
        driver = create_chrome_driver(config)
    elif config.get_driver_type() == DriverType.FIREFOX:
        driver = create_firefox_driver(config)
    else:
        raise NotImplementedError(f"Driver type not supported: {config.get_driver_type().name}")
    __apply_config(driver, config)
    return driver


def __apply_config(driver: WebDriver, config: ConfigData):
    driver.implicitly_wait(config.get_implicit_wait())
    if config.is_maximize():
        driver.maximize_window()


