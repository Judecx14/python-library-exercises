from time import sleep
from typing import List
from classes.browser import Browser
from matplotlib import pyplot as plt


class Chart():
    __data: List[any]
    __browser: Browser
    __ptl: any

    def __init__(self) -> None:
        self.__data = []
        self.__browser = Browser()
        self.__ptl = plt

    def get_data(self, quantity_of_readings: int = 4, wait: float = 5.0) -> None:
        self.__browser.open()
        for _ in range(quantity_of_readings):
            self.__browser.find_elements()
            self.__data.append(self.__browser.get_data_elements())
            sleep(wait)
        for i in self.__data:
            print(i)

    def create_chart(self) -> None:
        x = [i for i in range(len(self.__data))]
        y = [i[0] for i in self.__data]
        print(x, y)
        self.__ptl.bar(x, y)
        self.__ptl.show()

    def create_file_csv(self) -> None:
        pass
