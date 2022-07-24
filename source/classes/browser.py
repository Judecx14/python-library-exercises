from typing import List
from time import sleep
from selenium.webdriver.common.by import By
from classes.element import Element
from configuration.setup import Settings
from constants.actions import Actions


class Browser:
    __settings = Settings()
    __driver: any 
    __url: str
    __mode: any
    __elements: List[Element]
    __data_elements: List[str]
    __wait_time: float

    def __init__(self) -> None:
        self.__driver = self.__settings.driver
        self.__url = self.__settings.url
        self.__mode = By.ID
        self.__elements = self.__settings.elements
        self.__data_elements = []
        self.__wait_time = self.__settings.wait_time
        self.__set_mode()
        self.__set_window_size()
   

    def __set_mode(self) -> None:
        if self.__settings.not_mode == False:
            self.__mode = self.__settings.mode

    def __set_window_size(self) -> None:
        if self.__settings.maximize:
            self.__driver.maximize_window()

    def open(self) -> None:
        self.__driver.get(self.__url)

    def find_elements(self) -> None:
        self.__reset_data_elements()
        if self.__settings.not_mode == True:
            self.__find_elements_without_mode()
        else:
            self.__find_elements_with_mode()
        

    def __find_elements_without_mode(self):
        for element in self.__elements:
            temp_element = self.__driver.find_element(*self.__set_find_by(element))
            self.__set_action(element, temp_element)

    def __set_find_by(self, element: Element) -> tuple:
        if element.find.id:
            return By.ID, element.find.id
        elif element.find.name:
            return By.NAME, element.find.name
        elif element.find.classname:
            return By.CLASS_NAME, element.find.classname
        elif element.find.xpath:
            return By.XPATH, element.find.xpath

    def __set_action(self, element: Element, temp_element: any) -> None:
        if element.action.type == Actions.CLICK.value:
            temp_element.click()
            sleep(self.__wait_time)
        elif element.action.type == Actions.WRITE.value:
            temp_element.send_keys(element.action.value)
        elif element.action.type == Actions.READ.value:
            self.__data_elements.append(temp_element.text)


    def __find_elements_with_mode(self):
        for element in self.__elements:
            temp_element = self.__driver.find_element(self.__mode, self.__set_find_by(element)[1])
            self.__set_action(element, temp_element)

    def get_data_elements(self) -> List[str]:
        return self.__data_elements

    def __reset_data_elements(self) -> None:
        self.__data_elements = []

    def close(self) -> None:
        self.__driver.close()
