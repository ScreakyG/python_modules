from collections.abc import Callable
import functools
from typing import Any
import time

def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power", args[-1])
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper

    return decorator

class MageGuild():
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all((char.isalpha() or char.isspace() for char in name))

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"

def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper():
            attempt_count = 0

            while attempt_count < max_attempts:
                attempt_count += 1

                try:
                    return  func()
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt_count}/{max_attempts})")

            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator

@retry_spell(3)
def testing_invalid_spell():
    raise Exception("My is not working :(")

@retry_spell(3)
def testing_valid_spell():
    return "Waaaaagh spelled !"

@power_validator(10)
def testing_power(spell_name: str, power: int):
    return (f"Using my {spell_name} with power {power}!")


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper():
        # print(f"Casting function: {func.__name__}")

        start_time = time.perf_counter()
        time.sleep(0.12)
        result = func()
        end_time = time.perf_counter()
        elapsed = end_time - start_time

        # .3f signifie , 'f' afficher en float, '.3' pour garder 3 chiffres apres virgule
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper

@spell_timer
def cast_fireball() -> str:
    return "Fireball cast!"



def main():
    print("Testing spell timer...")
    print(f"Casting {cast_fireball.__name__}") # cast_fireball metadata is keeped because of functools.wraps decorator
    print("Result:", cast_fireball())

    print("\nTesting power validator...")
    print(testing_power('Fireball', 20))
    print(testing_power('Fireball', 5))

    print("\nTesting retry spell...")
    print(testing_invalid_spell())
    print(testing_valid_spell())
    print(testing_invalid_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Pedro "))
    print(MageGuild.validate_mage_name("Pedro1"))
    print(MageGuild().cast_spell("Lightning", 15))

if __name__ == '__main__':
    main()
