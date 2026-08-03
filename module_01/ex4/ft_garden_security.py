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

    def increase_age(self, days: int) -> None:
        self._age = self._age + days

    def simulate_growth(self, simulation_time: int) -> None:
        print("=== Garden Plant Growth ===")
        self.show()

        for i in range(1, simulation_time + 1):
            print(f"=== Day {i} ===")
            self.increase_age(1)
            self.grow()
            self.show()


if __name__ == "__main__":
    rose = Plant("rose", -25, 30, 0.25)
