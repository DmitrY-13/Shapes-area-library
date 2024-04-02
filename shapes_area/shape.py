from abc import ABC, abstractmethod


class Shape(ABC):
    @property
    @abstractmethod
    def area(self) -> int | float:
        pass
    