from abc import ABC


class Named(ABC):
    __DEFAULT_NAME = "Unnamed"

    def __init__(self, name: str = __DEFAULT_NAME):
        self.__name = name if name != "" else self.__DEFAULT_NAME

    @property
    def Name(self) -> str:
        return self.__name
