import numpy as np
import csv
from re import S
from time import sleep
from typing import List
from classes.browser import Browser
from matplotlib import pyplot as plt


class Chart():
    __data: List[any]
    __browser: Browser
    __plt: any

    def __init__(self) -> None:
        self.__data = []
        self.__browser = Browser()
        self.__plt = plt

    def get_data(self, quantity_of_readings: int = 4, wait: float = 5.0) -> None:
        self.__browser.open()
        for _ in range(quantity_of_readings):
            self.__browser.find_elements()
            self.__data.append(self.__browser.get_data_elements())
            sleep(wait)
        self.__browser.close()

    def create_chart(self, width = 0.25, ylabel = "Scores", title = "Data by reading") -> None:
        fig, ax = self.__plt.subplots()
        x_axis = np.arange(len(self.__data))
        ax.set_xticks(x_axis, ["Reading " + str(i+1) for i in range(len(self.__data))])
        chart_data: List[any] = []
        temp_data = np.array(self.__data)
        for i in range(temp_data.shape[-1]):
            chart_data.append(temp_data[:, i])
        for index, data in enumerate(chart_data):
            temp_rect = ax.bar(
                x_axis + (width*index),
                [float(i.replace(",", "")) for i in data], 
                width,
                label="fact_" + str(index+1)
            )
            ax.bar_label(temp_rect, padding = 3)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.legend()
        fig.tight_layout()
        self.__plt.show()

    def create_file_csv(self) -> None:
        with open("source/assets/data/chart_data.csv", "w", newline = "", encoding = "utf-8") as f:
            writer = csv.writer(f)
            for i, data in enumerate(self.__data):
                writer.writerow(["Reading " + str(i+1)])
                writer.writerow(["fact_" + str(i+1) for i in range(len(data))])
                writer.writerow(data)
                writer.writerow([])
