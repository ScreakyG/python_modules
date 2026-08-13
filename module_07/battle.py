import ex0

flame_factory = ex0.FlameFactory()
aqua_factory = ex0.AquaFactory()

def factory_tester(factory_object: ex0.CreatureFactory) -> None:
    print("Testing factory")

    base_creature = factory_object.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory_object.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack(), end="\n")
    
factory_tester(flame_factory)
print()
factory_tester(aqua_factory)