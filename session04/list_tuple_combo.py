# Save as: list_tuple_combo.py
def main():
    # TODO:
    # 1. Prompt for 2 names.
    # 2. Prompt for 2 ages.
    # 3. Create a list of tuples [(name1, age1), (name2, age2)].
    # 4. Print each entry as "Name: X, Age: Y".
    name1 = input().strip()
    name2 = input().strip()
    age1 = int(input().strip())
    age2 = int(input().strip())
    list = [(name1, age1), (name2, age2)]
    print(f"Name: {list[0][0]}, Age: {list[0][1]}")
    print(f"Name: {list[1][0]}, Age: {list[1][1]}")
    pass

if __name__ == "__main__":
    main()
