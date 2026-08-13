from abc import ABC, abstractmethod

class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass

class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transform_state = False
        super().__init__()

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
