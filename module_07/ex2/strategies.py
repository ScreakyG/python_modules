from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        return True


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> None:
        try:
            print(creature.attack())
        except AttributeError as error:
            print(error)

    def is_valid(self, creature: Creature) -> bool:
        return True

class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):       
            
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())

        else:
            raise Exception(f"Invalid Creature '{creature._name}' for this aggressive strategy")

    def is_valid(self, creature: Creature) -> bool:
            return isinstance(creature, TransformCapability)

class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            
            print(creature.attack())
            print(creature.heal())

        else:
            raise Exception(f"Invalid Creature '{creature._name}' for this defensive strategy")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)