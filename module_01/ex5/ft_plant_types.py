#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        daily_growth_size: float
    ) -> None:

        self._name = name
        self._height = 25.0
        self._age = 30
        
        self.set_height(height)
        self.set_age(age)
        self._daily_growth_size = daily_growth_size

        print("Created: ", end="")
        self.show()

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self._name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)

    def show(self) -> None:
        print(
            f"{self._name.capitalize()}: "
            f"{round(self._height, 1)}cm, "
            f"{self._age} days old"
        )

    def grow(self) -> None:
        self._height = self._height + self._daily_growth_size

    def age(self, days: int) -> None:
        self._age = self._age + days
        for i in range(days):
            self.grow()

    def simulate_growth(self, days: int) -> None:
        print("=== Garden Plant Growth ===")
        self.show()

        for i in range(days):
            print(f"=== Day {i + 1} ===")
            self.age(1)
            self.show()


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        daily_growth_size: float,
        color: str,
    ) -> None:
        
        self._color = color
        self._bloomed = False
        super().__init__(name, height, age, daily_growth_size)


    def bloom(self) -> None:
        print(f"[asking {self._name.capitalize()} to bloom]")
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        
        if self._bloomed == False:
            print(f"{self._name.capitalize()} has not bloomed yet")
        else:
            print(f"{self._name.capitalize()} is blooming beautifully!")

class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        daily_growth_size: float,
        trunk_diameter: float
    ) -> None:
        
        self._trunk_diameter = trunk_diameter
        super().__init__(name, height, age, daily_growth_size)

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.capitalize()} to produce shade]")
        print(f"Tree {self._name.capitalize()} now produces a shade of {self._height}cm long and {self._trunk_diameter}cm wide")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}")
        

class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        daily_growth_size: float,
        harvest_season: str,
    ) -> None:
        
        self._harvest_season = harvest_season
        self._nutritional_value = 0
        super().__init__(name, height, age, daily_growth_size)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season.capitalize()}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self, days: int) -> None:
        print(f"[make {self._name.capitalize()} grow and age for {days} days]")

        super().age(days)
        self._nutritional_value = self._nutritional_value + (1 * days)

        self.show()

if __name__ == "__main__":
    # flower = Flower("flower", 10, 20, 0.2, "red")
    # flower.bloom()
    # flower.show()

    tree = Tree("oak", 200, 365, 0.1, 5.0)
    tree.produce_shade()

    # vegetable = Vegetable("tomato", 5.0, 10, 0.1, "april")
    # vegetable.age(10)