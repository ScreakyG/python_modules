import ex0
import ex1

healing_factory = ex1.HealingCreatureFactory()
transform_factory = ex1.TransformCreatureFactory()

def factory_tester(factory_object: ex0.CreatureFactory) -> None:
    if (factory_object.__class__.__name__) == "TransformCreatureFactory":    
        print("Testing Creature with transform capability")
    
        base_creature = factory_object.create_base()
        print(base_creature.describe())
        print(base_creature.attack())
        print(base_creature.transform())
        print(base_creature.attack())
        print(base_creature.revert())

        print()

        evolved_creature = factory_object.create_evolved()
        print(evolved_creature.describe())
        print(evolved_creature.attack())
        print(evolved_creature.transform())
        print(evolved_creature.attack())
        print(evolved_creature.revert())

    else:
        print("Testing Creature with healing capability")
        
        base_creature = factory_object.create_base()
        print(base_creature.describe())
        print(base_creature.attack())
        print(base_creature.heal())

        print()

        evolved_creature = factory_object.create_evolved()
        print(evolved_creature.describe())
        print(evolved_creature.attack())
        print(evolved_creature.heal())

factory_tester(healing_factory)
print()
factory_tester(transform_factory)
