from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    validity = "VALID"
    allowed_ingredients = dark_spell_allowed_ingredients()

    try:
        for ingredient in ingredients.split(","):
            allowed_ingredients.index(ingredient)
            
    except Exception as error:
        validity = "INVALID"
    
    return (validity)