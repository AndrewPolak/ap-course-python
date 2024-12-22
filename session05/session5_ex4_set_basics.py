# Save as: session5_ex4_set_basics.py
def main():
    # TODO:
    # 1. Create an empty set.
    # 2. Prompt for 5 items, add each to the set.
    # 3. Print the set.
    # 4. Prompt for a check item.
    # 5. Print membership result.
    # 6. Print length of set.

    fruits = set()
    for i in range(5):
        fruits.add(input(f"Enter fruit #{i + 1}: ").rstrip())
    
    print(fruits)

    fruit = input("Enter a fruit to check membership: ")

    print(f"{fruit} is not in the set" if fruit not in fruits else f"{fruit} is in the set")

    print(f"{fruit} is in the set" if fruit in fruits else f"{fruit} is not in the set")

    print(f"{fruit} is", "not" if fruit not in fruits else "", "in the set")

    print("Number of unique items: ", len(fruits))

if __name__ == "__main__":
    main()