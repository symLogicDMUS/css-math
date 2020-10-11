import os
from pprint import pprint


def get_css_file_paths(dir_path):
    """Step 1. get every file in dir_path with .css extention"""
    file_paths = []
    for root, dirs, files in os.walk(dir_path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            if file_path.endswith(".css"):
                file_paths.append(file_path)
    return file_paths


if __name__ == "__main__":
    pprint(get_css_file_paths("./testDir"))