
import json
LENDS_FILE = "lends.json"

def load_lends():
    try:
        with open(LENDS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
