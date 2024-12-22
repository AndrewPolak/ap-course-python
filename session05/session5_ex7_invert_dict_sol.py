# Save as: session5_ex7_invert_dict_sol.py

def main():
    original = {}
    for i in range(5):
        k = input(f"Name for key #{i+1}: ").strip()
        v = input(f"Value for key #{i+1}: ").strip()
        original[k] = v

    inverted = {}
    for old_key, old_val in original.items():
        inverted[old_val] = old_key  # last wins if duplicates

    print(f"Original: {original}")
    print(f"Inverted: {inverted}")

if __name__ == "__main__":
    main()