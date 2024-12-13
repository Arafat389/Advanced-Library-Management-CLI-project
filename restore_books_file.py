"""import json

def restore_all_books(all_books):
    with open("all_books.json", "r") as fp:
        all_books = json.load(fp)
    return all_books"""

import json
import os

def restore_all_books(all_books):
    if not os.path.exists("all_books.json"):
        # If the file doesn't exist, initialize with an empty list
        with open("all_books.json", "w") as fp:
            json.dump([], fp)
        return []
    # Otherwise, read the existing file
    with open("all_books.json", "r") as fp:
        return json.load(fp)
