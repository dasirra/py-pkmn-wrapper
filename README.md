# PokéAPI Wrapper

A minimal Python wrapper for the PokéAPI with Pokémon visualization capabilities.

## Installation

```bash
pip install pokeapi-wrapper
```

## Usage

```python
from pokeapi_wrapper import PokeAPI

# Initialize the API client
api = PokeAPI()

# Get a Pokémon and display its information with ASCII art
pikachu = api.get_pokemon("pikachu")
pikachu.show_pokemon()

# Get a Pokémon by name
print(f"Name: {pikachu.name}")
print(f"ID: {pikachu.id}")
print(f"Height: {pikachu.height/10} m")  # Height is in decimeters
print(f"Weight: {pikachu.weight/10} kg")  # Weight is in hectograms

# Get types
for type_info in pikachu.types:
    print(f"Type: {type_info.type['name']}")

# Get abilities
for ability_info in pikachu.abilities:
    hidden_text = " (hidden)" if ability_info.is_hidden else ""
    print(f"Ability: {ability_info.ability['name']}{hidden_text}")

# Display colored ASCII art of the Pokémon
ascii_art = pikachu.get_ascii_sprite(width=60, colored=True)
print(ascii_art)

# Display non-colored ASCII art
bw_ascii_art = pikachu.get_ascii_sprite(width=60, colored=False)
print(bw_ascii_art)

# Display shiny version
shiny_ascii_art = pikachu.get_ascii_sprite(width=60, shiny=True)
print(shiny_ascii_art)

# Display back view
back_ascii_art = pikachu.get_ascii_sprite(width=60, back=True)
print(back_ascii_art)

# Get a Pokémon by ID
charizard = api.get_pokemon(6)
print(f"Name: {charizard.name}")

# Get a list of Pokémon
pokemon_list = api.get_pokemon_list(limit=5)
print(f"Total count: {pokemon_list.count}")

for pokemon in pokemon_list.results:
    print(f"- {pokemon['name']} (ID: {pokemon['id']})")
```

## Terminal Pokédex Application

The package includes a terminal-based Pokédex application that allows you to search for Pokémon and view their stats and ASCII art representation.

### Running the Pokédex

```bash
python pokedex.py
```

### Features

- Search for any Pokémon by name
- View detailed stats and ASCII art representation
- See additional information like moves and held items
- View different sprite variations (shiny, back view)

## Features

- Access to Pokémon endpoints
- Simple and intuitive API with visualization
- Lightweight with minimal dependencies
- Colored ASCII art generation from Pokémon sprites using ascii_magic
- One-line Pokémon visualization with `show_pokemon()`
- Terminal-based Pokédex application

## Available Resources

- Pokémon: `/pokemon/{id or name}`
- Pokémon List: `/pokemon`

## ASCII Art Options

The `get_ascii_sprite` method accepts the following parameters:

- `width`: Width of the ASCII art in columns (default: 40)
- `height`: Height of the ASCII art in rows (default: 20)
- `shiny`: Whether to use the shiny sprite (default: False)
- `back`: Whether to use the back sprite (default: False)
- `colored`: Whether to use colored ASCII art (default: True)

The ASCII art generator:
- Uses the ascii_magic library for high-quality ASCII art
- Supports colored output for terminal displays
- Automatically handles transparent backgrounds
- Maintains proper aspect ratio of sprites

## Pokémon Visualization

The `show_pokemon()` method provides a complete visualization of a Pokémon:

```python
# Get a Pokémon
pikachu = api.get_pokemon("pikachu")

# Display its information and sprite
pikachu.show_pokemon()

# Display with non-colored ASCII art
pikachu.show_pokemon(colored=False)
```

This displays:
- Pokémon name and ID
- Type(s)
- Height and weight
- Abilities (including hidden abilities)
- Base stats
- ASCII art sprite

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [PokéAPI](https://pokeapi.co/) for providing the API
- [ascii_magic](https://github.com/LeandroBarone/python-ascii_magic) for the ASCII art generation