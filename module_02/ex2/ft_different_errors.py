#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None | str:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            (10 / 0)
        case 2:
            f = open("demofile.txt", "r")
        case 3:
            10 + "10"
        case _:
            return "Operation completed succesfully"

def test_error_types() -> None:
    operations_list: list[int] = [0, 1, 2, 3, 4]

    for operation in operations_list:
        try:
            print(f"Testing operation {operation}...")
            response = garden_operations(operation)
        except ValueError as error:
            print("Caught ValueError:", error)
        except ZeroDivisionError as error:
            print("Caught ZeroDivisionError:", error)
        except FileNotFoundError as error:
            print("Caught FileNotFoundError:", error)
        except TypeError as error:
            print("Caught TypeError:", error)
        else:
            print(response)
        finally:
            print()

    print("All error types tested successfully!")

if __name__ == '__main__':
    test_error_types()