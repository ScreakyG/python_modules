# === Exercise 0 Test Data ===
# Lambda Sanctum Test Data
artifacts = [{'name': 'Water Chalice', 'power': 94, 'type': 'focus'}, {'name': 'Earth Shield', 'power': 95, 'type': 'weapon'}, {'name': 'Light Prism', 'power': 119, 'type': 'relic'}, {'name': 'Wind Cloak', 'power': 98, 'type': 'relic'}]
mages = [{'name': 'Kai', 'power': 81, 'element': 'water'}, {'name': 'Casey', 'power': 75, 'element': 'lightning'}, {'name': 'Phoenix', 'power': 95, 'element': 'light'}, {'name': 'Sage', 'power': 65, 'element': 'fire'}, {'name': 'Rowan', 'power': 51, 'element': 'earth'}]
spells = ['earthquake', 'heal', 'freeze', 'fireball']

def main():
    artifact_sorter = lambda artifacts: sorted(artifacts, key=lambda item: item['power'])
    power_filter = lambda mages, min_power: list(filter(lambda mage: mage['power'] > min_power, mages))
    spell_transformers = lambda spells: list(map(lambda spell: f"* {spell} *", spells))
    mage_stats = lambda mages: {
        'max_power' : max(mages, key=lambda item: item['power'])['power'],
        'min_power': min(mages,  key=lambda item: item['power'])['power'],
        'avg_power': round(sum(mage['power'] for mage in mages) / len(mages), 2)
    }


    print("Testing artifact sorter...")
    print(f"Before sorting: {[artifact['power'] for artifact in artifacts]}")
    print(f"After sorting: {[artifact['power'] for artifact in artifact_sorter(artifacts)]}")

    print()

    min_power = 80
    print(f"Testing power_filter with min_power={min_power}...")
    print(f"Before filter {[mage['power'] for mage in mages]}")
    print(f"After filter {[mage['power'] for mage in power_filter(mages, min_power)]}")

    print()

    print(f"Testing spell_transformers...")
    print(f"Before filter {spells}")
    print(f"After filter {spell_transformers(spells)}")

    print()
    print("Testing mage_stats...")
    print(mage_stats(mages))

if __name__ == '__main__':
    main()
