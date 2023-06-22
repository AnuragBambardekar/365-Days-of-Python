"""
python .\diff_checker_tool_CLI_ver.py my_shopping_list.txt friends_shopping_list.txt
"""

import difflib
import sys

from pathlib import Path


def create_diff(old_file: Path, new_file: Path):
    file_1 = open(old_file).readlines()
    file_2 = open(new_file).readlines()

    delta = difflib.unified_diff(file_1, file_2, old_file.name, new_file.name)
    sys.stdout.writelines(delta)

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("old_file_version")
    parser.add_argument("new_file_version")
    args = parser.parse_args()

    old_file = Path(args.old_file_version)
    new_file = Path(args.new_file_version)

    create_diff(old_file, new_file)


if __name__ == "__main__":
    main()
