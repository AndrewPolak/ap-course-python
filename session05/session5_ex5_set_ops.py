# Save as: session5_ex5_set_ops.py
def main():
    # TODO:
    # 1. Prompt user for two comma-separated lines.
    # 2. Convert each to a set.
    # 3. Print union, intersection, difference, symmetric difference.

    list1 = input("Enter the 1st list (comma separated): ").rstrip()
    list2 = input("Enter the 2nd list (comma separated): ").rstrip()

    print(list1)
    print(list2)

    set1 = set(x.strip() for x in list1.split(','))
    set2 = set(x.strip() for x in list2.split(','))

    print(set1)
    print(set2)

    print("Union: ", set1 | set2)
    print("Intersection: ", set1 & set2)
    print("Difference: ", set1 - set2)
    print("Symmetric difference: ", set1 ^ set2)

    print("Union: ", set1.union(set2))
    print("Intersection: ", set1.intersection(set2))
    print("Difference: ", set1.difference(set2))
    print("Symmetric difference: ", set1.symmetric_difference(set2))

if __name__ == "__main__":
    main()