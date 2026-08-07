#!/usr/bin/env python3

import random

base_name_list: list[str] = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']

def main() -> None:
    print("=== Game Data Alchemist ===\n")

    print("Initial list of players:", base_name_list)
    
    capitalized_names_list: list[str] = [name.capitalize() for name in base_name_list] 
    print("New list with all names capitalized:", capitalized_names_list)

    only_capitalized_names_list: list[str] = [name for name in base_name_list if name == name.capitalize()]
    print("New list of capitalized names only:", only_capitalized_names_list)

    dictionnaire: dict[str, int] = {
        name: random.randint(1, 1000)
        for name in only_capitalized_names_list
    }
    print("Score dict:", dictionnaire)

    average_score: float = round(sum(dictionnaire.values()) / len(dictionnaire), 2)
    print("Score average is", average_score)

    dictionnaire2: dict[str, int] = {
        name: dictionnaire[name]
        for name in only_capitalized_names_list
        if dictionnaire[name] > average_score 
    }
    print("High scores:", dictionnaire2)

if __name__ == '__main__':
    main()