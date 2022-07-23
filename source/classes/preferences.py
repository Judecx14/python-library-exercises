from typing import List
from classes.element import Element
from classes.options import Options


class Preferences:
    options: Options
    elements: List[Element]

    def __init__(self, options: Options, elements: List[Element]) -> None:
        self.options = options
        self.elements = elements
