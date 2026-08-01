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

        self._stats = self.Stats(self)

        print("Created: ", end="")
        self.show()

    @staticmethod
    def check_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0)

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
        self._stats._show_count = self._stats._show_count + 1

    def grow(self) -> None:
        self._height = self._height + self._daily_growth_size
        self._stats._grow_count = self._stats._grow_count + 1

    def age(self, days: int) -> None:
        self._age = self._age + days
        for i in range(days):
            self.grow()
            
        self._stats._age_count = self._stats._age_count + 1

    def simulate_growth(self, days: int) -> None:
        print("=== Garden Plant Growth ===")
        self.show()

        for i in range(days):
            print(f"=== Day {i + 1} ===")
            self.age(1)
            self.show()

    class Stats:
        def __init__(self, plant: "Plant") -> None:
            self._plant = plant
            self._age_count: int = 0
            self._grow_count: int = 0
            self._show_count: int = 0

        def show(self) -> None:
            print(f"[statistics for {self._plant._name.capitalize()}]")
            print(f"{self._grow_count} grow, {self._age_count} age, {self._show_count} show")

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
        self.age(10)
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        
        if self._bloomed == False:
            print(f"{self._name.capitalize()} has not bloomed yet")
        else:
            print(f"{self._name.capitalize()} is blooming beautifully!")

class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self, plant: "Plant") -> None:
            super().__init__(plant)
            self._produce_shade_count = 0

        def show(self) -> None:
            super().show()
            print(f"shade: {self._produce_shade_count}")
            
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
        self._stats._produce_shade_count = self._stats._produce_shade_count + 1

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

class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        daily_growth_size: float,
        color: str
    ) -> None:

        self._seeds = 0        
        super().__init__(name, height, age, daily_growth_size, color)

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42
        self.show()


def display_plant_stats(item: Plant) -> None:
    item._stats.show()

if __name__ == "__main__":

    # print("=== Seed")
    # seed = Seed("Sunflower", 80, 45, 0.1, "yellow")
    # seed.bloom()
    # seed._stats.show()

    # print("=== Anonymous")
    plant = Plant.create_anonymous_plant()
    # plant._stats.show()

    # print ("=== Tree")
    tree = Tree("oak", 200, 365, 1, 5)
    # tree._stats.show()
    # tree.produce_shade()
    # tree._stats.show()

    display_plant_stats(tree)
    display_plant_stats(plant)