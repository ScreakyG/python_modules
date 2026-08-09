#!/usr/bin/env python3

import sys


def secure_archive(filename: str, operation: str, additional_content: str) -> tuple[bool, str]:

    try:
        match operation:
            case "r":
                with open(filename, "r") as f:
                    return (True ,f.read())
                    
            case "w":
                with open(filename, "w") as f:
                    f.write(additional_content)
                    return (True, additional_content)
    
            case _:
                return (False, "Unkown operation")
                
    except OSError as error:
        return (False, str(error))
        

def main() -> None:
    result = secure_archive(sys.argv[1], sys.argv[2], sys.argv[3])
    print(result)

if __name__ == "__main__":
    main()