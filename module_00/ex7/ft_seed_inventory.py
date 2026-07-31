def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    format_unit: str = ""
    
    try:
        match unit:
            case "packets":
                format_unit = f"{quantity} packets available"
            case "grams":
                format_unit = f"{quantity} grams total"
            case "area":
                format_unit = f"covers {quantity} square meters"
            case _:
                raise ValueError("Unknown unit type")
        print(f"{seed_type.capitalize()} seeds: {format_unit}")
        
    except ValueError as error:
        print(error)
