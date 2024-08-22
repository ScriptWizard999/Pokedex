import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk
from database import PokemonDatabase
from search import search_pokemon_by_name, search_pokemon_by_type

class PokedexApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokédex")
        self.root.geometry("800x600")
        self.root.config(bg="#f5f107")  # Set background color

        # Custom fonts
        self.title_font = font.Font(family="lberobello serif modern script font", size=40, weight="bold")
        self.label_font = font.Font(family="lberobello serif modern script font", size=28, weight="bold")
        self.button_font = font.Font(family="lberobello serif modern script font", size=10)
        self.text_font = font.Font(family="Courier", size=11, weight="bold")

        self.db = PokemonDatabase('data/pokemon_data.csv')

        # Set up the layout
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        tk.Label(self.root, text="Pokédex", font=self.title_font, fg="#700707", bg="#f5f107").pack(pady=10)

        # Create the menu frame
        menu_frame = tk.Frame(self.root, bg="#f5f107")
        menu_frame.pack(pady=10)

        # Add buttons to the menu frame
        tk.Button(menu_frame, text="View Total Pokémon", font=self.button_font, fg="#EEEEEE", bg="#060d66", command=self.show_total_pokemon).grid(row=0, column=0, padx=10)
        tk.Button(menu_frame, text="Search by Name", font=self.button_font, fg="#EEEEEE", bg="#060d66", command=self.search_by_name).grid(row=0, column=1, padx=10)
        tk.Button(menu_frame, text="Search by Type", font=self.button_font, fg="#EEEEEE", bg="#060d66", command=self.search_by_type).grid(row=0, column=2, padx=10)
        tk.Button(menu_frame, text="Add New Pokémon", font=self.button_font, fg="#EEEEEE", bg="#060d66", command=self.add_pokemon).grid(row=0, column=3, padx=10)

        # Create a text area for output
        self.result_text = tk.Text(self.root, height=500, width=900, wrap=tk.WORD, font=self.text_font, fg="#FFD369", bg="#180578")
        self.result_text.pack(pady=10)

        # Label to display the image
        self.image_label = tk.Label(self.root, bg="#222831")
        self.image_label.pack(pady=10)

    def show_total_pokemon(self):
        total = self.db.total_pokemon()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Total number of Pokémon in Pokédex is: {total}\n")

    def search_by_name(self):
        name = self.simple_input_dialog("Enter Pokémon Name")
        if name:
            # Use the result returned by search_pokemon_by_name to display in the text box
            result = search_pokemon_by_name(self.db, name)
            self.result_text.delete(1.0, tk.END)
            if result:
                self.result_text.insert(tk.END, result)
                self.show_pokemon_image(name)  # Show the image in the GUI
            else:
                self.result_text.insert(tk.END, f"No Pokémon found with the name '{name}'")

    def search_by_type(self):
        p_type = self.simple_input_dialog("Enter Pokémon Type")
        if p_type:
            result = search_pokemon_by_type(self.db, p_type)
            self.result_text.delete(1.0, tk.END)
            if result:
                self.result_text.insert(tk.END, result)
            else:
                self.result_text.insert(tk.END, f"No Pokémon found with the type '{p_type}'")

    def add_pokemon(self):
        # Create a pop-up window to add a new Pokémon
        add_window = tk.Toplevel(self.root)
        add_window.title("New Pokémon Registration")
        add_window.config(bg="#fc1c1c")

        fields = ["Name", "Type 1", "Type 2", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"]
        entries = {}

        for i, field in enumerate(fields):
            tk.Label(add_window, text=field, font=self.label_font, fg="#FFD369", bg="#222831").grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(add_window, font=self.text_font, fg="#FFD369", bg="#393E46")
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = entry

        def save_pokemon():
            pokemon_data = {field: entries[field].get() for field in fields}
            try:
                pokemon_data['Total'] = int(pokemon_data['Total'])
                pokemon_data['HP'] = int(pokemon_data['HP'])
                pokemon_data['Attack'] = int(pokemon_data['Attack'])
                pokemon_data['Defense'] = int(pokemon_data['Defense'])
                pokemon_data['Sp. Atk'] = int(pokemon_data['Sp. Atk'])
                pokemon_data['Sp. Def'] = int(pokemon_data['Sp. Def'])
                pokemon_data['Speed'] = int(pokemon_data['Speed'])
                pokemon_data['Generation'] = int(pokemon_data['Generation'])
                pokemon_data['Legendary'] = pokemon_data['Legendary'].lower() in ['true', '1', 'yes']

                self.db.add_pokemon(pokemon_data)
                messagebox.showinfo("Success", f"{pokemon_data['Name']} added successfully!")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please ensure all numeric fields contain valid numbers.")

        tk.Button(add_window, text="Save Pokémon", font=self.button_font, fg="#EEEEEE", bg="#00ADB5", command=save_pokemon).grid(row=len(fields), columnspan=2, pady=10)

    def simple_input_dialog(self, prompt):
        dialog = tk.Toplevel(self.root)
        dialog.title(prompt)
        dialog.config(bg="#222831")
        tk.Label(dialog, text=prompt, font=self.label_font, fg="#FFD369", bg="#222831").pack(pady=10)
        entry = tk.Entry(dialog, font=self.text_font, fg="#FFD369", bg="#393E46")
        entry.pack(pady=5)
        entry.focus_set()

        def on_submit():
            dialog.result = entry.get()
            dialog.destroy()

        tk.Button(dialog, text="Submit", font=self.button_font, fg="#EEEEEE", bg="#00ADB5", command=on_submit).pack(pady=10)
        self.root.wait_window(dialog)
        return getattr(dialog, 'result', None)

    def show_pokemon_image(self, name):
        image_path = f"images/{name.lower()}.png"
        try:
            img = Image.open(image_path)
            img = img.resize((200, 200), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img  # Keep a reference to avoid garbage collection
        except FileNotFoundError:
            self.image_label.config(image='')
            # messagebox.showwarning("Image Not Found", f"No image found for {name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PokedexApp(root)
    root.mainloop()
