# Save as: list_methods.py
def main():
    # TODO:
    # 1. Start with list [10, 5, 7].
    # 2. Prompt the user for a number and append it.
    # 3. Remove the smallest number from the list.
    # 4. Print the updated list and its length.
    list = [10, 5, 7]
    list.append(int(input()))
    list.remove(min(list))
    print("Updated list:", list)
    print("length:", len(list))
    pass

if __name__ == "__main__":
    main()
