# Save as: session11_ex1_file_read.py

from pathlib import Path
import os

def main():
    # TODO:
    # 1. Attempt to open "sample_input.txt" in read mode.
    # 2. Print its contents.
    # 3. Handle FileNotFoundError (or check existence first).
    if (p := Path("sample_input.txt")).exists() and os.access(p, os.R_OK):
        with p.open("r") as f:
            for line in f:
                print(line.strip())
    
    try:
        f = open("sample_input.txt", "r")
    except FileNotFoundError as e:
        print("Error:", e)
    else:
        with f:
            for line in f:
                print(line.strip())

if __name__ == "__main__":
    main()