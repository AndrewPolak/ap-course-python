# Save as: session9_ex8_nested_try.py
def main():
    # TODO:
    # 1. Outer try: open filename
    # 2. inner try: parse lines as integers
    # 3. catch FileNotFoundError in outer except
    # 4. catch ValueError in inner except
    filename = input("Enter filename: ").strip()

    try:
        # f = open(filename, 'r')
        # try:
        #     numbers = []
        #     for line in f:
        #         numbers.append(int(line))
        #     print(numbers)
        # except ValueError:
        #     print(f"Error: invalid line in file {filename}: not an int")
        # finally:
        #     f.close()

        with open(filename, 'r') as f:
            try:
                lines = f.readlines()
                numbers = [int(line) for line in lines]
            except ValueError:
                print("Failed to parse integers in the file")

    except FileNotFoundError:
        print("Error: file not found")

if __name__ == "__main__":
    main()