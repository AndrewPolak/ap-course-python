# Save as: text_processing.py
def main():
    # TODO:
    # 1. Read input string.
    # 2. Print the entire string in uppercase.
    # 3. Slice the first half of the string.
    # 4. Print a formatted message including the original length and the sliced half.
    text = input().rstrip()
    print(text.upper())
    first_half = text[:(len(text) //2)]
    print(first_half)
    print(f"The original string has {len(text)} characters, and the first half is {first_half}.")
    pass

if __name__ == "__main__":
    main()
