#!/usr/bin/env python3

import random

# Creer un set avec set() ou alors avec accolades : var = {'item1', 'item2'}
achievements_set = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',
    'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer', 'Untouchable']




def gen_player_achievements() -> set:
    achievement_count_picker = random.randint(1, len(achievements_set))

    # Sample pick randomly 'nbr' unique items for the list
    random_achievements = random.sample(achievements_set, achievement_count_picker)

    # Create a set from this list
    player_achievements_set = set(random_achievements)

    return player_achievements_set
    
def main() -> None:
    print("=== Achivement Tracker System ===\n")
    
    players: list[str] = ['Alice', 'Bob', 'Charlie', 'Dylan']
    players_achievements: list[set] = []

    # Generate random sets for each player and store them
    for player in players:
        player_generated_achievements = gen_player_achievements()
        print(f"Player {player}: {player_generated_achievements}")
        players_achievements.append(player_generated_achievements)

    # '*' va venir "deplier" tout les items de mon sets pour les mettres en parametre de union()
    distinct_achivements_set = set.union(*players_achievements)
    print(f"\nAll distinct achievements: {distinct_achivements_set}")

    common_achivements_set = set.intersection(*players_achievements)
    print(f"\nCommon achievements: {common_achivements_set}")

    i: int = 0
    while i < len(players):
        other_players_achievements = (players_achievements[:i] + players_achievements[i + 1:])
        player_unique_achievements = players_achievements[i].difference(*other_players_achievements)        
        print(f"Only {players[i]} has: {player_unique_achievements}")

        i = i + 1

    print()
    
    j: int = 0
    while j < len(players):
        other_players_achievements = (players_achievements[:j] + players_achievements[j + 1:])
        
        player_missing_achievements = set.difference(set(achievements_set), players_achievements[j])

        print(f"{players[j]} is missing: {player_missing_achievements}")
        
        j = j + 1
        

if __name__ == '__main__':
    main()