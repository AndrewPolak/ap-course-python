# Save as: session11_ex5_pathlib_demo.py

from pathlib import Path

def main():
    # TODO:
    # 1. from pathlib import Path
    # 2. prompt for a dir
    # 3. Path(dir).mkdir(exist_ok=True)
    # 4. create example.txt inside, write a line
    # 5. print absolute path

    dir = input("Enter directory: ").strip()
    Path(dir).mkdir(exist_ok=True)
    try:
        f = open(Path(dir) / "example.txt", "w")
    except FileNotFoundError as e:
        print(e)
    else:
        with f:
            f.write("sample line" + '\n')
        print((Path(dir) / "example.txt").resolve())

if __name__ == "__main__":
    main()