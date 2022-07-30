from typing import List
from classes.element import Element
from classes.options import Options


class Preferences:
    import_settings: str
    options: Options
    elements: List[Element]

    def __init__(self, import_settings: str, options: Options, elements: List[Element]) -> None:
        self.import_settings = import_settings
        self.options = options
        self.elements = elements
