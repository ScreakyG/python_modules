#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_test.py <file>")
        return

    print("=== Cyber Archives Recovery ===\n")

    print(f"Accesing file '{sys.argv[1]}'")
    try:
        file: typing.IO[str] = open(sys.argv[1], "r")

        print("---\n")
        print(file.read())
        print("\n---")

        file.close()
        print(f"=== File '{sys.argv[1]}' closed.")
    except OSError as error:
        print(f"Error opening file '{sys.argv[1]}:'", error)
    

if __name__ == '__main__':
    main()