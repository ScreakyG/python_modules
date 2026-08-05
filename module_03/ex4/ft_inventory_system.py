#!/usr/bin/env python3

import sys

d: dict = {}

def parse_arg(arg: str) -> None:
    arg_splitted = arg.split(":")

    if len(arg_splitted) != 2:
        print(f"Error - invalid parameter '{arg}'")
        return

    try:
        item_name = arg_splitted[0]
        quantity = int(arg_splitted[1])
        
    except ValueError as error:
        print(f"Quantity error for '{arg_splitted[1]}': {error}")
        
    else:
        if item_name in d:
            print(f"Redundant item '{item_name}' - discarding")
        else:
            d[item_name.strip()] = quantity

def fill_dictionaire(argvs: list[str]) -> None:
    for item in argvs:
        parse_arg(item)

def display_inventory() -> None:
    print(f"Got inventory: {d}")

    item_list: list[str] = []
    items_total_quantity: int = 0
    
    for key, value in d.items():
        item_list.append(key)
        items_total_quantity += value
        
    print("Item list:", item_list)
    print(f"Total quantity of the {len(item_list)} items: {items_total_quantity}")

    most_abundant_quantity = 0
    most_abundant_name = ''

    least_abundant_quantity = float("inf")
    least_abundant_name = ''
    
    for key, value in d.items():
        print(f"Item {key} represents {round( value * 100 / items_total_quantity, 1)}%")

        if value > most_abundant_quantity:
            most_abundant_name = key
            most_abundant_quantity = value

        if value < least_abundant_quantity:
            least_abundant_name = key
            least_abundant_quantity = value


    print(f"Item most abundant: {most_abundant_name} with quantity {most_abundant_quantity}")
    print(f"Item least abundant: {least_abundant_name} with quantity {least_abundant_quantity}")

    d.update({'magic_item': 1})
    print("Updated inventory:", d)
    
def main() -> None:
    print("=== Inventory System Analysis ===")

    if len(sys.argv) < 2:
        print("usage: python3 ft_inventory_systempy <item_name>:<item_quantity>")
        return

    fill_dictionaire(sys.argv[1:])
    display_inventory()
 
if __name__ == '__main__':
    main()