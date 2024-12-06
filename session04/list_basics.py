# Save as: list_basics.py
def main():
    # TODO:
    # 1. Read 3 items from the user.
    # 2. Store them in a list.
    # 3. Print the full list.
    # 4. Print the first and last items.
    fruits = []
    fruits.append(input())
    fruits.append(input())
    fruits.append(input())
    print("Full list:", fruits)
    print("First item:", fruits[0])
    print("Last item:", fruits[-1])

    pass

if __name__ == "__main__":
    main()
