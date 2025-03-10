# PokéAPI Wrapper

A minimal Python wrapper for the PokéAPI with Pokémon visualization capabilities.

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

## Testing

The package includes a comprehensive test suite using pytest. To run the tests:

```bash
# Install test dependencies
pip install pytest

# Run the tests
pytest
```

### Test Philosophy

Our tests follow these principles:

- **Direct Testing**: We test functions and methods directly without mocks or fixtures
- **Function Existence**: We verify that functions exist and have the correct signatures
- **Integration Tests**: We include optional integration tests that can be run when needed
- **Simple and Readable**: Tests are straightforward and easy to understand

### Test Coverage

The test suite covers:
- API client functionality
- Pokemon model and related classes
- ASCII art generation utilities

### Running Specific Tests

You can run specific test categories:

```bash
# Run all tests
pytest

# Run API tests
pytest tests/test_api.py

# Run model tests
pytest tests/test_models.py

# Run integration tests (normally skipped)
pytest -v tests/test_api.py::TestPokeAPI::test_get_pokemon_integration
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [PokéAPI](https://pokeapi.co/) for providing the API
- [ascii_magic](https://github.com/LeandroBarone/python-ascii_magic) for the ASCII art generation