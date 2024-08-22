from tabulate import tabulate
from image import show_pokemon_image

def search_pokemon_by_name(database, name):
    result = database.get_pokemon_by_name(name)
    if result:
        # Tabulate all key-value pairs for the found Pokémon
        for pokemon in result:  # Iterate over the list of Pokémon dictionaries
            show_pokemon_image(name)
            return(tabulate([pokemon], headers='keys', tablefmt='fancy_grid'))
    else:
        print(f"No Pokémon found with name '{name}'")

def search_pokemon_by_type(database, p_type):
    result = database.get_pokemon_by_type(p_type)
    if result:
        return tabulate(result, headers='keys', tablefmt='fancy_grid')
    return f"no Pokémon found with this type'{p_type}'"

