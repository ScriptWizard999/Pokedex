# Pokédex - A Python GUI Application

![Pokédex GUI](images/pokedex_screenshot.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
  - [Viewing Total Pokémon](#viewing-total-pokémon)
  - [Searching by Name](#searching-by-name)
  - [Searching by Type](#searching-by-type)
  - [Adding a New Pokémon](#adding-a-new-pokémon)
- [Dependencies](#dependencies)
- [Future Enhancements](#future-enhancements)

## Introduction

Pokédex is a Python-based GUI application that allows users to interact with a Pokémon database. The application enables users to view, search, and manage Pokémon data, providing a simple and user-friendly interface. It also supports displaying Pokémon images, searching by name or type, and adding new Pokémon entries.

## Features

- **View Total Pokémon**: Displays the total number of Pokémon in the database.
- **Search by Name**: Allows users to search for Pokémon by their name and display detailed information.
- **Search by Type**: Enables users to search for Pokémon by their type (e.g., Water, Fire) and list all matching entries.
- **Add New Pokémon**: Provides a form to add new Pokémon to the database, including their stats and type information.
- **Image Display**: Shows an image of the Pokémon if available.
- **Customizable Interface**: The GUI features a dark-themed, modern design with customizable fonts and colors.

# Usage
- **Viewing Total Pokémon**:
- Launch the application.
- Click the "View Total Pokémon" button.
- The total number of Pokémon in the database will be displayed in the text area.
- **Searching by Name**:
- Click the "Search by Name" button.
- Enter the Pokémon name in the prompt (e.g., "Pikachu").
- The Pokémon's details, including stats and type, will be displayed in the text area. If an image is available, it will be shown below the text.
- **Searching by Type**:
- Click the "Search by Type" button.
- Enter the Pokémon type (e.g., "Water") in the prompt.
- All Pokémon matching the entered type will be listed in the text area.
- **Adding a New Pokémon**:
- Click the "Add New Pokémon" button.
- Fill out the form with the new Pokémon's details, including Name, Type, Stats, and Generation.
- Click "Save Pokémon" to add the new entry to the database.

# Dependencies:
- Python 3.x
- pandas: For handling CSV data.
- Pillow: For managing and displaying images.
- tabulate: For formatting text output in tables.
- Tkinter: Python's standard GUI package (comes pre-installed with Python).

# Project Structure:
## POKEDEX/
-  ├── data/
-  │ └── pokemon_data.csv # CSV file with Pokémon data
-  ├── images/
-  │ └── (Pokemon images) # Images for each Pokémon, named as pokemon_name.png
-  ├── pokedex_gui.py # The main GUI application script
-  ├── database.py # Module to handle data loading and management
-  ├── search.py # Module to handle search functionality
-  ├── images.py # Module to handle showing image functinality
-  ├── README.md # Documentation

# Future Enhancements
- **Advanced Search Filters**: Implement additional search filters, such as by generation, legendary status, or stat ranges.
- **Pokémon Abilities and Moves**: Extend the database to include Pokémon abilities and moves.
- **GUI Enhancements**: Further improve the GUI with animations, sound effects, and advanced customization options.
- **Data Import/Export**: Add functionality to import/export Pokémon data to/from other formats such as JSON or XML.