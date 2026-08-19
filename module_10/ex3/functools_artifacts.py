from collections.abc import Callable
import functools
import operator
from typing import Any

def spell_reducer(spells: list[int], operation: str) -> int:
    if not len(spells):
        return 0

    match(operation):
        case 'add':
            return functools.reduce(operator.add, spells)
        case 'multiply':
            return functools.reduce(operator.mul, spells)
        case 'min':
            return functools.reduce(min, spells)
        case 'max':
            return functools.reduce(max, spells)
        case _:
            print(f"Operation '{operation}' does not exists")
            return 0


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]) -> dict[str, Callable[[str], str]]:
    return {
        "fire": functools.partial(base_enchantment, power=50, element="fire"),
        "ice": functools.partial(base_enchantment, power=50, element="ice"),
        "grass": functools.partial(base_enchantment, power=50, element="grass")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
            return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(arg: Any) -> str:
        return "Unkown spell type"

    @dispatcher.register(int)
    def _(arg: int) -> str:
        return (f"Damage spell: {arg} damage")

    @dispatcher.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @dispatcher.register(list)
    def _(arg: list[str]) -> str:
        return f"Multi-cast: {len(arg)}, {arg}"

    return dispatcher




def main():

    print("\nTest spell reduceer...")
    print(f"Sum: {spell_reducer([1,2,3], "add")}")
    print("Product:", spell_reducer([4,4], "multiply"))
    print("Min:", spell_reducer([4,1,10], "min"))
    print("Max:", spell_reducer([4,1,10], "max"))

    print("Test partial enchanter...")
    enchants = partial_enchanter(lambda power, element, target: f"Enchant {target} using {power} power with {element} element")

    print(enchants.get("fire")(target="Wizard"))
    print(enchants.get("ice")(target="Wizard"))
    print(enchants.get("grass")(target="Wizard"))

    print("\nTest memoized fibonacci...")
    print("Fib(5): ", memoized_fibonacci(5))
    print("Fib(5) stats:", memoized_fibonacci.cache_info())
    print("Fib(5)", memoized_fibonacci(5))
    print("Fib(5) stats:", memoized_fibonacci.cache_info())
    memoized_fibonacci.cache_clear()

    print("\nTest spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(1))
    print(dispatcher('fireball'))
    print(dispatcher(['fireball', 'ice', 'water']))
    print(dispatcher(1.0))

if __name__ == '__main__':
    main()
