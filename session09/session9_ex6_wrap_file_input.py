# Save as: session9_ex6_wrap_file_input.py
def read_integers_from_file(filename):
    # TODO:
    # 1. open file in read mode
    # 2. read lines, convert to int
    # 3. handle FileNotFoundError, ValueError

    try:
        # f = open(filename, 'r')
        # numbers = []
        # for line in f:
        #     numbers.append(int(line))
        # f.close()
        # return numbers
        with open(filename, 'r') as f:
            lines = f.readlines
            return [int(line) for line in lines]
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except ValueError:
        print("Error: Non-integer data found.")
        return []

def main():
    fname = input("Enter filename: ")
    numbers = read_integers_from_file(fname)
    print("Numbers read:", numbers)

if __name__ == "__main__":
    main()