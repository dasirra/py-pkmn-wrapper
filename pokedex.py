#!/usr/bin/env python3
"""
Pokédex Application

A simple terminal-based Pokédex that allows users to search for Pokémon
and view their stats and ASCII art representation.
"""

import os
import time
from pokeapi_wrapper.api import PokeAPI


def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")


def print_header():
    """Print the Pokédex header."""
    header = """
    ██████╗  ██████╗ ██╗  ██╗███████╗██████╗ ███████╗██╗  ██╗
    ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗██╔════╝╚██╗██╔╝
    ██████╔╝██║   ██║█████╔╝ █████╗  ██║  ██║█████╗   ╚███╔╝ 
    ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║  ██║██╔══╝   ██╔██╗ 
    ██║     ╚██████╔╝██║  ██╗███████╗██████╔╝███████╗██╔╝ ██╗
    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    """
    print(header)
    print("Welcome to the Terminal Pokédex!")
    print("--------------------------------")


def search_pokemon():
    """Search for a Pokémon by name."""
    api = PokeAPI()

    while True:
        clear_screen()
        print_header()

        # Get user input
        search_term = input("\nEnter a Pokémon name (or 'q' to quit): ").strip().lower()

        if search_term == "q":
            break

        if not search_term:
            print("\nPlease enter a valid Pokémon name.")
            time.sleep(1.5)
            continue

        try:
            # Search for the Pokémon
            print(f"\nSearching for {search_term.capitalize()}...")
            pokemon = api.get_pokemon(search_term)

            # Display the Pokémon
            clear_screen()
            print_header()
            pokemon.show_pokemon()

            # Ask if the user wants to see more details
            show_more = (
                input("\nWould you like to see more details? (y/n): ").strip().lower()
            )
            if show_more == "y":
                show_detailed_info(pokemon)

            # Ask if the user wants to search for another Pokémon
            continue_search = (
                input("\nSearch for another Pokémon? (y/n): ").strip().lower()
            )
            if continue_search != "y":
                break

        except Exception as e:
            print(
                f"\nError: Could not find Pokémon '{search_term}'. Please check the spelling and try again."
            )
            print(f"Details: {str(e)}")
            time.sleep(2)


def show_detailed_info(pokemon):
    """Show detailed information about a Pokémon."""
    clear_screen()
    print_header()

    print(f"\n=== {pokemon.name.upper()} DETAILED INFO ===\n")

    # Show moves (limited to first 10)
    if pokemon.moves:
        print("MOVES:")
        for i, move in enumerate(pokemon.moves[:10], 1):
            print(f"{i}. {move.move['name'].replace('-', ' ').capitalize()}")

        if len(pokemon.moves) > 10:
            print(f"...and {len(pokemon.moves) - 10} more moves.")

    # Show held items
    if pokemon.held_items:
        print("\nPOSSIBLE HELD ITEMS:")
        for item in pokemon.held_items:
            print(f"- {item.item['name'].replace('-', ' ').capitalize()}")

    # Show different sprite variations
    print("\nSPRITE VARIATIONS:")

    input("\nPress Enter to continue...")


def main():
    """Main function to run the Pokédex application."""
    try:
        search_pokemon()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
    finally:
        print("\nThank you for using the Pokédex!")


if __name__ == "__main__":
    main()
