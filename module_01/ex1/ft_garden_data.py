#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, "
            f"{self.age} days old"
        )


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("rose", 25, 30)
    plant2 = Plant("sunflower", 80, 45)
    plant3 = Plant("cose", 15, 120)

    plant1.show()
    plant2.show()
    plant3.show()
