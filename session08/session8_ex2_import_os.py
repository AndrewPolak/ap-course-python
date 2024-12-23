# Save as: session8_ex2_import_os.py

import os

def main():
    # TODO:
    # 1. import os
    # 2. Print os.getcwd()
    # 3. Prompt for a directory path
    # 4. Check existence with os.path.exists()
    print(f"Current directory: {os.getcwd()}")
    dir_name = input("Enter a directory name: ").strip()
    print(f"Directory exists: {os.path.exists(dir_name)}")


if __name__ == "__main__":
    main()