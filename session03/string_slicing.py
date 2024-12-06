# Save as: string_slicing.py
def main():
    # TODO:
    # 1. Read a line of input into a variable 'text'.
    # 2. Print the first 5 chars.
    # 3. Print the last 3 chars.
    # 4. Print every second character.
    text = input()
    print(f"First 5 chars: {text[0:5]}")
    print(f"Last 3 char: {text[-3:]}")
    print(f"Every second char: {text[::2]}")
    pass

if __name__ == "__main__":
    main()
