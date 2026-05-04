#!/usr/bin/env python3

import argparse
from config import save_config
from cli import handle_list, handle_add


def main():
    parser = argparse.ArgumentParser(description="Time Tracker CLI")

    parser.add_argument("--config", help="Set data directory")
    parser.add_argument("--list", action="store_true", help="List entries")

    parser.add_argument(
        "--add",
        nargs="*",
        help='Add entry: --add 9 11 "123" "Coding"'
    )

    args = parser.parse_args()

    if args.config:
        save_config(args.config)
        print("Config gespeichert.")

    elif args.list:
        handle_list()

    elif args.add is not None:
        handle_add(args.add)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
