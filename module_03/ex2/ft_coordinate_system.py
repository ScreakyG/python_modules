#!/usr/bin/env python3
import sys
import math

def get_distance(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as floats in format 'x, y, z': ")
        
        try:
            user_input_coordinates = user_input.split(",")

            if len(user_input_coordinates) != 3:
                raise ValueError("You must provide exactly 3 coordinates: x, y, z")
            
            x = float(user_input_coordinates[0].strip())
            y = float(user_input_coordinates[1].strip())
            z = float(user_input_coordinates[2].strip())
               
        except ValueError as error:
            print("There was an error:", error)

        else:
            return (x, y ,z)
    

def main() -> None:
    print("=== Game Coordinate System ===\n")
    positions: list[tuple[float, float, float]] = []

    # Prompt the user to get base coordinates x, y, z then it returns a tuple from it
    print("Get a first set of coordinates")
    position = get_player_pos()
    x, y, z = position
    positions.append(position)
    
    print("Got a first tuple:", position)
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print("Distance to center:", round(get_distance(*positions[0], 0, 0, 0), 4))

    # Prompt the user to get a second sets of coordinate
    print("\nGet a second set of coordinates")
    position2 = get_player_pos()
    x2, y2, z2 = position2
    positions.append(position2)
    
    print("Got a second tuple:", position2)
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    print("Distance between the 2 sets of coordinates:", round(get_distance(*positions[1], *positions[0]), 4))
if __name__ == '__main__':
    main()
