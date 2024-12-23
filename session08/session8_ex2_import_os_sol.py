# Save as: session8_ex2_import_os_sol.py
import os

def main():
    cwd = os.getcwd()
    print(f"Current directory: {cwd}")

    dir_name = input("Enter a directory name: ").strip()
    exists = os.path.exists(dir_name)
    print(f"Directory exists: {exists}")

if __name__ == "__main__":
    main()