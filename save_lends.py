import json
LENDS_FILE = "lends.json"

def save_lends(lends):
    with open(LENDS_FILE, "w") as file:
        json.dump(lends, file, indent=4)