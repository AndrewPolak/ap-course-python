# Save as: session11_ex5_pathlib_demo_sol.py
from pathlib import Path

def main():
    dirname = input("Enter a directory name: ").strip()
    d = Path(dirname)
    d.mkdir(exist_ok=True)

    file_path = d / "example.txt"
    with open(file_path, "w") as f:
        f.write("Sample content.\n")

    print("Created example.txt at:", file_path.resolve())

if __name__ == "__main__":
    main()