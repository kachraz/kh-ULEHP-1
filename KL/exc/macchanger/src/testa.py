# This will have various programs which you used for testing or are taken from different sources

import argparse


def animal_sound():
    def get_animal_sound(animal):
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
        return sounds.get(animal.lower(), "unknown sound")

    def print_animal_sound():
        parser = argparse.ArgumentParser(description="Print the sound of an animal.")
        parser.add_argument("animal", type=str, help="The name of the animal")

        args = parser.parse_args()
        animal = args.animal
        sound = get_animal_sound(animal)

        print(f"The {animal} says {sound}.")
