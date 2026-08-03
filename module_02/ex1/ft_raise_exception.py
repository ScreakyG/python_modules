#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    converted = int(temp_str)
    if converted > 40:
        raise ValueError(f"{converted}°C is too hot for plants (max 40°C)")
    elif converted < 0:
        raise ValueError(f"{converted}°C is too cold for plants (min 0°C)")
    
    return (converted)
    
        
def test_temperature() -> None:
    print("== Garden Temperature ==", end="\n\n")

    tests_data: list[str] = ["25", "abc", "100", "-50"]

    for test in tests_data:
        try:
            print(f"Input data is '{test}'")
            input_conversion = input_temperature(test)
            print(f"Temperature is now {input_conversion}°C")

        except ValueError as error:
            print("Caught input_temperature error:", error)
        finally:
            print()

    print("All tests completed - program didn't crash!")

if __name__ == '__main__':
    test_temperature()