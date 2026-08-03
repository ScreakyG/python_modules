#!/usr/bin/env python3

def print_plant_infos() -> None:
    name: str = "Rose"
    height: int = 25
    age: int = 30
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age}days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    print_plant_infos()
    print("\n=== End of Program ===")
