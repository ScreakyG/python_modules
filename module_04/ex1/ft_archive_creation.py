#!/usr/bin/env python3

import sys
import typing


def read_file(file: typing.IO[str]) -> str:
    print("---\n")
    file_str = file.read()
    print(file_str)
    print("\n---")

    return file_str

def append_to_file(file_content: str) -> None:
    print("Transform data:")
    print("---\n")

    rows: list[str] = file_content.split("\n")
    
    for row in rows:
        print(f"{row}#")
    print("\n---")

    transformed_rows = [
        row + "#"
        for row in rows
    ]

    transformed_content = "\n".join(transformed_rows)
    
    save_file_path = input("Enter new file name (or empty):")
    if len(save_file_path) == 0:
        print("Not saving data.")
        return
        
    try:
        print(f"Saving data to '{save_file_path}'")
        
        f = open(save_file_path, "w")
        f.write(transformed_content)
        f.close()

        print(f"Data saved in file '{save_file_path}'")
    except OSError as error:
        print(f"Error writing to file '{save_file_path}:'", error)

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_test.py <file>")
        return

    print("=== Cyber Archives Recovery ===\n")

    print(f"Accesing file '{sys.argv[1]}'")
    try:
        file: typing.IO[str] = open(sys.argv[1], "r")
        
        file_content = read_file(file)
        file.close()
        print(f"=== File '{sys.argv[1]}' closed.")
        
        append_to_file(file_content)
        
    except OSError as error:
        print(f"Error opening file '{sys.argv[1]}:'", error)
    

if __name__ == '__main__':
    main()