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

def garden_operations(operation: int) -> None:
    if operation == 1:
        raise GardenError()
    elif operation == 2:
        raise PlantError("The tomato plant is wilting!")
    elif operation == 3:
        raise WaterError("Not enough water in the tank!")


def test_custom_error_types() -> None:
    operations_list: list[int] = [1, 2, 3]

    for operation in operations_list:
        try:
            garden_operations(operation)
        except PlantError as error:
            print("Caught PlantError:", error)
        except WaterError as error:
            print("Caught WaterError:", error)  
        except GardenError as error:
            print("Caught GardenError:", error)
        

if __name__ == '__main__':
    test_custom_error_types()