# This will have various programs which you used for testing or are taken from different sources

import argparse


def animal_sound():
    # Define the sounds for different animals
    sounds = {
        "dog": "bark",
        "cat": "meow",
        "cow": "moo",
        "bird": "tweet",
        "lion": "roar",
        "sheep": "baa",
        "horse": "neigh",
        "duck": "quack",
        "pig": "oink",
        "chicken": "cluck",
    }

    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Print the sound of an animal.")
    parser.add_argument("animal", type=str, help="The name of the animal")

    # Parse the arguments
    args = parser.parse_args()
    animal = args.animal

    # Get the sound for the given animal
    sound = sounds.get(animal.lower(), "unknown sound")

    # Print the result
    print(f"The {animal} says {sound}.")
