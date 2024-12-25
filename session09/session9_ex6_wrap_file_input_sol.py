# Save as: session9_ex6_wrap_file_input_sol.py
def read_integers_from_file(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            return [int(line) for line in lines]
    except FileNotFoundError:
        print("File not found.")
        return []
    except ValueError:
        print("Non-integer data found.")
        return []

def main():
    fname = input("Enter filename: ")
    numbers = read_integers_from_file(fname)
    print("Numbers read:", numbers)

if __name__ == "__main__":
    main()