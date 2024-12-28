# Save as: session11_ex4_file_exists_sol.py
import os

def main():
    fname = input("Enter a filename to check: ").strip()
    if os.path.exists(fname):
        print("File exists.")
        size = os.path.getsize(fname)
        print(f"Size: {size} bytes")
        # optional: mod_time = os.path.getmtime(fname)
    else:
        print("File does not exist.")

if __name__ == "__main__":
    main()