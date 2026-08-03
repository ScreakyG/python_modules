#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        daily_growth_size: float
    ) -> None:
        
        self.name = name
        self.height = height
        self.age = age
        self.daily_growth_size = daily_growth_size

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{round(self.height, 1)}cm, "
            f"{self.age} days old"
        )

    def grow(self) -> None:
        self.height = self.height + self.daily_growth_size

    def increase_age(self, days: int) -> None:
        self.age = self.age + days

    def simulate_growth(self, simulation_time: int) -> None:
        print("=== Garden Plant Growth ===")
        self.show()
        
        for i in range(1, simulation_time + 1):
            print(f"=== Day {i} ===")
            self.increase_age(1)
            self.grow()
            self.show()

if __name__ == "__main__":
    plant1 = Plant("rose", 25, 30, 2.32)
    plant1.simulate_growth(10)