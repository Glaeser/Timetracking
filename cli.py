# from storage import (
#     list_markdown_files,
#     read_file,
#     ensure_week_file,
#     add_entry_to_today,
# )

from config import load_config
from utils import normalize_time
import os
import storage

def handle_list():
    config = load_config()
    directory = config.get("data_dir")

    if not directory:
        print("Kein Verzeichnis konfiguriert.")
        return

    files = storage.list_markdown_files(directory)

    for i, file in enumerate(files):
        print(f"{i + 1}: {file}")

    choice = int(input("Datei auswählen: ")) - 1

    filepath = os.path.join(directory, files[choice])
    print("\n" + storage.read_file(filepath))


def handle_add(args=None):
    config = load_config()
    directory = config.get("data_dir")

    if not directory:
        print("Kein Verzeichnis konfiguriert.")
        return

    filepath = storage.ensure_week_file(directory)

    # 👉 CLI MODE
    if args and len(args) >= 2:
        time_from = normalize_time(args[0])
        time_to = normalize_time(args[1])
        activity = args[2] if len(args) >= 3 else ""
        doing = args[3] if len(args) >= 4 else ""

    # 👉 INTERACTIVE MODE
    else:
        time_from = normalize_time(input("Von: "))
        time_to = normalize_time(input("Bis: "))
        activity = input("Aktivität (optional): ")
        doing = input("Doing: ")

    storage.add_entry_to_today(filepath, time_from, time_to, activity, doing)

    print("Eintrag gespeichert.")