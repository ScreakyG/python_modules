import os
import sys
from dotenv import load_dotenv

def check_env() -> None:
    response = load_dotenv(".env")
    if response == False:
        raise Exception("Could not load env file, please make sure you have a '.env' file at the root of directory and set variables using '.env.example'")
    
    env_variables = ['MATRIX_MODE', 'DATABASE_URL', 'API_KEY', 'LOG_LEVEL', 'ZION_ENDPOINT']

    
    for variable_key in env_variables:
        variable_value = os.getenv(variable_key)

        if variable_value:
            print(f"[OK] {variable_key} is set")
        else:
            print(f"[KO] {variable_key} is missing")



try:
    check_env()

    print("\nORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    print(f"Database: {os.getenv('DATABASE_URL')}")
    
    if os.getenv('API_KEY'):
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthrorized")

    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    print(f"Zion Network: {os.getenv('ZION_ENDPOINT')}")

    print("The Oracle sees all configurations.")

    
except Exception as error:
    print(f"Error: {error}")