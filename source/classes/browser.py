from typing import List
from time import sleep
from selenium.webdriver.common.by import By
from classes.element import Element
from configuration.setup import Settings
from constants.actions import Actions


class Browser:
    settings = Settings()

    def __init__(self) -> None:
        self.driver = self.settings.driver
        self.url = self.settings.url
        self.elements = self.settings.elements
        self.data_elements = []
        self.wait_time = self.settings.wait_time
        self.set_mode()
        self.set_window_size()

    def set_mode(self) -> None:
        if self.settings.not_mode == False:
            self.mode = self.settings.mode

    def set_window_size(self) -> None:
        if self.settings.maximize:
            self.driver.maximize_window()

    def open(self) -> None:
        self.driver.get(self.url)

    def find_elements(self) -> None:
        if self.settings.not_mode == True:
            self.find_elements_without_mode()
        else:
            self.find_elements_with_mode()
        

    def find_elements_without_mode(self):
        for element in self.elements:
            temp_element = self.driver.find_element(*self.set_find_by(element))
            self.set_action(element, temp_element)

    def set_find_by(self, element: Element) -> tuple:
        if element.find.id:
            return By.ID, element.find.id
        elif element.find.name:
            return By.NAME, element.find.name
        elif element.find.classname:
            return By.CLASS_NAME, element.find.classname
        elif element.find.xpath:
            return By.XPATH, element.find.xpath

    def set_action(self, element: Element, temp_element: any) -> None:
        if element.action.type == Actions.CLICK.value:
            temp_element.click()
            sleep(self.wait_time)
        elif element.action.type == Actions.WRITE.value:
            temp_element.send_keys(element.action.value)
        elif element.action.type == Actions.READ.value:
            self.data_elements.append(temp_element.text)

    def find_elements_with_mode(self):
        pass

    def get_data_elements(self) -> List[str]:
        return self.data_elements

    def close(self) -> None:
        self.driver.close()
