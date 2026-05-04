import json
import os

CONFIG_PATH = os.path.expanduser("~/.timetracker_config.json")


def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return {"data_dir": None}


def save_config(data_dir):
    with open(CONFIG_PATH, "w") as f:
        json.dump({"data_dir": data_dir}, f)