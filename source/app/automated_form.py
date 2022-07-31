from classes.browser import Browser

class Form():

    __browser: Browser

    def __init__(self) -> None:
        self.__browser = Browser()
    
    def open(self) -> None:
        self.__browser.open()
    
    def fill_fields(self) -> None: 
        self.__browser.find_elements()
        self.__browser.close()