# Save as: session11_ex4_file_exists.py

import os
import pathlib

def main():
    # TODO:
    # 1. import os or pathlib
    # 2. prompt user for filename
    # 3. check existence
    # 4. optional: print size or modification time

    filename = input("Enter filename: ").strip()

    if os.path.exists(filename) and pathlib.Path(filename).exists():
        print("File exists")
        stats = os.stat(filename)
        print(f"Size (bytes): {stats.st_size}")
        print(f"Last Modified: {stats.st_mtime}")

    else:
        print("File does not exist")

if __name__ == "__main__":
    main()