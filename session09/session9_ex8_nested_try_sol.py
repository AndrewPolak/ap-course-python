# Save as: session9_ex8_nested_try_sol.py
def main():
    filename = input("Enter a file with integers: ")
    try:
        with open(filename, "r") as f:
            try:
                lines = f.readlines()
                numbers = [int(line) for line in lines]
                print("Read numbers:", numbers)
            except ValueError:
                print("Failed to parse integers in the file.")
    except FileNotFoundError:
        print("File does not exist.")

if __name__ == "__main__":
    main()