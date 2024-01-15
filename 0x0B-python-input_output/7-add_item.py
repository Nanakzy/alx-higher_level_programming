#!/usr/bin/python3
"""
Script to add arguments to a Python list and save to a JSON file
"""

import sys
import json
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_and_save_to_json_file():
    """Adds all arguments to a Python list and saves to a JSON file."""
    # Get the existing list from the file or create a new list
    if exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
    else:
        my_list = []

    # Add arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    add_and_save_to_json_file()
