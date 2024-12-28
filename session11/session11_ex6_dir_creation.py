# Save as: session11_ex6_dir_creation.py

import os

def main():
    # TODO:
    # 1. prompt for subdirectory path
    # 2. create all levels (parents=True)
    # 3. print success

    subdir_path = input("Enter subdirectory path: ").strip()

    if os.path.exists(subdir_path):
        print("Directory already existed or created")
        exit(1)

    try:
        os.makedirs(subdir_path, exist_ok=True)
    except Exception as e:
        print(e)
    else:
        print(f"Successfully created {subdir_path}")

if __name__ == "__main__":
    main()