from abc import ABC, abstractmethod


class Jarat(ABC):
    @abstractmethod
    def tostring(self):
        pass