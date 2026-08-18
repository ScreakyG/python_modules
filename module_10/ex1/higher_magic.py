from collections.abc import Callable

# === Exercise 1 Test Data ===
# Higher Realm Test Data
# Use these in your test functions:
test_values = [17, 24, 9]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fire(target: str, power: int) -> str:
    return f"Fire attack {target} for {power} HP"

def spell_combiner(spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]) -> Callable[[str, int], tuple[str, str]]:
    def combine(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combine

def power_amplifier(base_spell: Callable[[str, int], str], multiplier: int) -> Callable[[str, int], str]:
    def amplify(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplify

def conditional_caster(condition: Callable[[str, int], bool], spell: Callable[[str, int], str]) -> Callable[[str, int], str]:
    def authorized_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return authorized_spell


def spell_sequence(spells: list[Callable[[str, int], str]]) -> Callable[[str, int], list[str]]:
    def cast_sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return cast_sequence

def main():
    print("Testing spell combiner...")
    combined = spell_combiner(fire, heal)
    print(f"Created 'spell_combiner' function with 'fire', 'heal' as parameters that returns a new function 'combine': {combined}")
    print(f"Using 'combine' function with <target> and <power> params result: {combined("Dragon", 17)}")

    print()
    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fire, 3)
    print(f"Original spell: {fire("Dragon", 10)}")
    print(f"Amplified spell: {mega_fireball("Dragon", 10)}")

    print()
    print("Testing conditional caster...")
    new_spell = conditional_caster(condition=lambda target, power: target != "Dragon" and power > 5, spell=fire)
    print(f"Using with a valid condition: {new_spell("Wizard", 10)}")
    print(f"Using with a invalid condition: {new_spell("Dragon", 10)}")

    print()
    print("Testing sequence caster...")
    sequence = [fire, heal]
    test = spell_sequence(sequence)
    print(test("Dragon", 10))

if __name__ == '__main__':
    main()
