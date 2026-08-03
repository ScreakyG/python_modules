#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
    

class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)

def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
            
    print(f"Watering {plant_name.capitalize()}: [OK]")

def test_valid_plants() -> None:
    print("Testing valid plants..")
    print("Opening watering system")
    
    water_plant("Tomato")
    water_plant("Lettuce")
    water_plant("Carrots")
    
def test_invalid_plants() -> None:
    print("Testing invalid plants..")
    print("Opening watering system")
    
    water_plant("Tomato")
    water_plant("lettuce")

def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    try:
        test_valid_plants()
        print()
        test_invalid_plants()
    except PlantError as error:
        print("Caught PlantError:", error)
        print("..ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")
        print("Cleanup always happens, even with errors!")

if __name__ == '__main__':
    test_watering_system()