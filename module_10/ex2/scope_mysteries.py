from collections.abc import Callable

def mage_counter() -> Callable[[], int]:
    counter: int = 0
    def increment() -> int:
        nonlocal counter
        counter += 1
        return counter
    return increment

def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    def accumulated_power(additional_power: int) -> int:
        nonlocal initial_power
        initial_power += additional_power
        return initial_power
    return accumulated_power

def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return apply_enchantment

def memory_vault() -> dict[str, Callable]:
    vault: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        vault[key] = value

    # def recall(key: str) -> str:
    #     return vault.get(key, "Memory not found")

    return {
        "store": store,
        "recall": lambda key: vault.get(key, "Memory not found")
    }

def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell acumulator...")
    add_power = spell_accumulator(5)
    print(f"Base 5, add 10: {add_power(10)}")
    print(f"Base 5, add 20: {add_power(20)}")

    print("\nTesting enchantment factory...")

    fire_enchant = enchantment_factory("Flaming")
    print(fire_enchant("Sword"))

    water_enchant = enchantment_factory("Wet")
    print((water_enchant("Sword")))


    print("\nTesting memory vault...")
    vault_a = memory_vault()
    print("Store 'eau' = 'pluie' in vault_a")
    vault_a['store']("eau", "pluie")

    print(f"Recall 'eau': {vault_a['recall']("eau")} from vault_a")

    vault_b = memory_vault()
    print(f"Recall 'eau': {vault_b['recall']("eau")} from vault_b")

if __name__ == '__main__':
    main()
