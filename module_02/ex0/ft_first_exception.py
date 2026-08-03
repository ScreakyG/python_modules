#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    converted = int(temp_str)
    return (converted)
        
def test_temperature() -> None:
    print("== Garden Temperature ==", end="\n\n")

    tests_data: list[str] = ["25", "abc", "42"]

    for test in tests_data:
        try:
            print(f"Input data is '{test}'")
            input_conversion = input_temperature(test)
            print(f"Temperature is now {input_conversion}°C")

        except ValueError as error:
            print("Conversion failed:", error)
        finally:
            print("\n")

    print("All tests completed - program didn't crash!")

if __name__ == '__main__':
    test_temperature()