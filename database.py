import pandas as pd

class PokemonDatabase:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    def get_pokemon_by_name(self, name):
        # Ensure the column name is correctly referenced
        pokemon = self.df[self.df['Name'].str.lower() == name.lower()]
        return pokemon.to_dict(orient='records')

    def get_pokemon_by_type(self,p_type):
        pokemon = self.df[(self.df['Type 1'].str.lower() == p_type.lower()) | (self.df['Type 2'].str.lower() == p_type.lower()) ]
        return pokemon.to_dict(orient='records')
    
    def add_pokemon(self, pokemon_data):
        new_pokemon = pd.DataFrame([pokemon_data])
        self.df = pd.concat([self.df, new_pokemon], ignore_index=True)
        self.df.to_csv('Data\pokemon_data.csv', index=False)

    def total_pokemon(self):
        return len(self.df)