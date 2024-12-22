
NUM_PAIRS = 4

# Save as: session5_ex7_invert_dict.py
def main():
    # TODO:
    # 1. Prompt for 5 key-value pairs, store in dict.
    # 2. Build a new dict where old_value -> old_key.
    # 3. Print both dicts.

    normal = {}
    inverted = {}

    for i in range(NUM_PAIRS):
        pair_number = i + 1
        key = input(f"Name for key #{pair_number}: ").rstrip()
        value = input(f"Value for key #{pair_number}:").rstrip()
        normal[key] = value

    for k, v in normal.items():
        inverted[v] = k

    print("Original: ", normal)
    print("Inverted: ", inverted)


    

if __name__ == "__main__":
    main()