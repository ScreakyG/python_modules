import ex0
import ex1
import ex2

def battle(opponents: list[tuple[ex0.CreatureFactory, ex2.BattleStrategy]]) -> None:
    print(f"{len(opponents)} opponents involved\n")

    i = 0
    while i < len(opponents) - 1:
        j = i + 1        
        while j < len(opponents):
            start_fight(opponents[i], opponents[j])
            j += 1
        i += 1

def start_fight(opponent_a: tuple[ex0.CreatureFactory, ex2.BattleStrategy], opponent_b: tuple[ex0.CreatureFactory, ex2.BattleStrategy]) -> None:
    
    opponent_a_factory, opponent_a_strategy = opponent_a
    opponent_b_factory, opponent_b_strategy = opponent_b

    # Spawn players creatures
    opponent_a_creature = opponent_a_factory.create_base()
    opponent_b_creature = opponent_b_factory.create_base()

    print("* Battle *")
    # Creatures announce themself
    print(opponent_a_creature.describe())
    print("vs.")
    print(opponent_b_creature.describe())
    print("now fight!")

    # Apply player strategy
    try:
        opponent_a_strategy.act(opponent_a_creature)
        opponent_b_strategy.act(opponent_b_creature)
    except Exception as error:
        print(f"Battle error, aborting tournament: {error}")

    print()

print("Tournament 0 (basic)")
print("[ (Flameling+Normal), (Healing+Defensive) ]")
print("*** Tournament ***")
battle(
    [
        (ex0.FlameFactory(), ex2.NormalStrategy()),
        (ex1.HealingCreatureFactory(), ex2.DefensiveStrategy())
    ]
)

print("-------------------------------------------")

print("Tournament 1 (error)")
print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
print("*** Tournament ***")
battle(
    [
        (ex0.FlameFactory(), ex2.AggressiveStrategy()),
        (ex1.HealingCreatureFactory(), ex2.DefensiveStrategy())
    ]
)

print("-------------------------------------------")

print("Tournament 2 (multiple)")
print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
print("*** Tournament ***")
battle(
    [
        (ex0.AquaFactory(), ex2.NormalStrategy()),
        (ex1.HealingCreatureFactory(), ex2.DefensiveStrategy()),
        (ex1.TransformCreatureFactory(), ex2.AggressiveStrategy()),
    ]
)




