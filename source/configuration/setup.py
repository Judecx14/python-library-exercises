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
    json_file_path = "resources/settings.json"
    executable_path = 'C:/bin/chromedriver.exe'
    preferences: Preferences
    driver: webdriver
    mode: By
    not_mode: bool = False
    maximize: bool
    url: str
    wait_time: float
    elements: List[Element]

    def __init__(self) -> None:
        self.load_preferences()
        self.set_preferences()

    def load_preferences(self) -> None:
        file = open(self.json_file_path, "r")
        self.preferences = json.loads(
            file.read(), object_hook=lambda d: SimpleNamespace(**d))
        file.close()

    def set_preferences(self) -> None:
        self.set_driver(self.preferences.options.driver)
        self.set_mode(self.preferences.options.mode)
        self.url = self.preferences.options.url
        self.elements = self.preferences.elements
        self.wait_time = float(self.preferences.options.wait)
        if self.preferences.options.maximize == "true":
            self.maximize = True

    def set_driver(self, driver: str) -> None:
        if driver == Drivers.CHROME.value:
            self.driver = webdriver.Chrome(
                executable_path=self.executable_path)
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
                executable_path=self.executable_path)

    def set_mode(self, mode: str) -> None:
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
