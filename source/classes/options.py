class Options:
    driver: str
    mode: str
    maximize: bool
    url: str
    wait: float

    def __init__(self, driver: str, mode: str, maximize: bool, url: str, wait: float) -> None:
        self.driver = driver
        self.mode = mode
        self.maximize = maximize
        self.url = url
        self.wait = wait
