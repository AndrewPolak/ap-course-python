# Save as: parse_input.py
def main():
    # TODO:
    # 1. Read a line of text.
    # 2. Split it into words (hint: str.split()).
    # 3. Print the first word, the last word, and the total number of words.
    text = input()
    parsed = text.split()
    print(f"First word: {parsed[0]}")
    print(f"Last word: {parsed[-1]}")
    print(f"Total words: {len(parsed)}")

    pass

if __name__ == "__main__":
    main()
