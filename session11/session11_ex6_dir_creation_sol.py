# Save as: session11_ex6_dir_creation_sol.py
import os

def main():
    path_str = input("Enter directory path (may include subdirs): ").strip()
    os.makedirs(path_str, exist_ok=True)
    print(f"Directory '{path_str}' created (or already existed).")

if __name__ == "__main__":
    main()