from enum import Enum


class DriverType(Enum):
    """
    List of valid and accepted drivers types.
    """
    CHROME = "chrome"
    FIREFOX = "firefox"


class ConfigData:
    def __init__(self, config_dict: dict):
        self.__config_dict = config_dict

    def get_driver_type(self) -> DriverType:
        browser_name = self.__config_dict["browser_name"]
        return DriverType(browser_name)

    def get_implicit_wait(self) -> int:
        return self.__config_dict["implicit_wait"]

    def get_drivers_path(self) -> bool:
        return self.__config_dict["drivers_path"]

    def get_headless_resolution(self) -> tuple:
        width = self.__config_dict["headless"]["resolution"]["width"]
        height = self.__config_dict["headless"]["resolution"]["height"]
        return width, height

    def is_maximize(self) -> bool:
        return self.__config_dict["maximize"]

    def is_headless(self) -> bool:
        return self.__config_dict["headless"]["enabled"]

    def is_incognito_session(self) -> bool:
        return self.__config_dict["incognito"]
