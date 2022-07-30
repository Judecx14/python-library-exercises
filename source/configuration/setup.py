import json
from typing import List
from types import SimpleNamespace
from selenium import webdriver
from selenium.webdriver.common.by import By
from classes.element import Element
from classes.preferences import Preferences
from constants.drivers import Drivers
from constants.modes import Modes


class Settings:
    __JSON_FILE_PATH = "source/assets/settings.json"
    __EXECUTABLE_PATH = 'C:/bin/chromedriver.exe'
    __preferences: Preferences
    driver: webdriver
    mode: By
    not_mode: bool = False
    maximize: bool
    url: str
    wait_time: float
    elements: List[Element]

    def __init__(self) -> None:
        self.__load_preferences()
        self.__set_preferences()

    def __load_preferences(self) -> None:
        file = open(self.__JSON_FILE_PATH, "r")
        temp_preferences = json.loads(
            file.read(), object_hook=lambda d: SimpleNamespace(**d))
        file.close()
        if not temp_preferences.import_settings:
            self.__preferences = temp_preferences
        else: 
            path = temp_preferences.import_settings
            file = open(path, "r")
            self.__preferences = json.loads(
                file.read(), object_hook=lambda d: SimpleNamespace(**d))
            file.close()

    def __set_preferences(self) -> None:
        self.__set_driver(self.__preferences.options.driver)
        self.__set_mode(self.__preferences.options.mode)
        self.url = self.__preferences.options.url
        self.elements = self.__preferences.elements
        self.wait_time = float(self.__preferences.options.wait)
        if self.__preferences.options.maximize == "true":
            self.maximize = True

    def __set_driver(self, driver: str) -> None:
        if driver == Drivers.CHROME.value:
            self.driver = webdriver.Chrome(
                executable_path=self.__EXECUTABLE_PATH)
        elif driver == Drivers.CHROMIUM.value:
            self.driver = webdriver.ChromiumEdge()
        elif driver == Drivers.EDGE.value:
            self.driver = webdriver.Edge()
        elif driver == Drivers.FIREFOX.value:
            self.driver = webdriver.Firefox()
        elif driver == Drivers.IE.value:
            self.driver = webdriver.Ie()
        elif driver == Drivers.SAFARI.value:
            self.driver = webdriver.Safari()
        else:
            self.driver = webdriver.Chrome(
                executable_path=self.__EXECUTABLE_PATH)

    def __set_mode(self, mode: str) -> None:
        if mode == Modes.ID.value:
            self.mode = By.ID
        elif mode == Modes.NAME.value:
            self.mode = By.NAME
        elif mode == Modes.CLASS_NAME.value:
            self.mode = By.CLASS_NAME
        elif mode == Modes.XPATH.value:
            self.mode = By.XPATH
        elif mode == Modes.ALL.value:
            self.not_mode = True
        else:
            self.mode = By.ID
