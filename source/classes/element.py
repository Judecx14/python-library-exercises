class Action:
    type: str
    value: str

    def __init__(self, type: str, value: str) -> None:
        self.type = type
        self.value = value


class Find:
    id: str
    name: str
    classname: str
    xpath: str

    def __init__(self, id: str, name: str, classname: str, xpath: str) -> None:
        self.id = id
        self.name = name
        self.classname = classname
        self.xpath = xpath


class Element:
    find: Find
    action: Action

    def __init__(self, find: Find, action: Action) -> None:
        self.find = find
        self.action = action
