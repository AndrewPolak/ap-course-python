# Save as: session5_ex2_dict_methods.py
def main():
    # TODO:
    # 1. grades = {"Alice": 85, "Bob": 90}
    # 2. Prompt user for a name + grade, update/add in dict.
    # 3. Prompt user for a name to remove, use pop().
    # 4. Print keys and values separately.

    grades = {"Alice": 85, "Bob": 90}
    name = input("Enter a name: ").strip()
    grade = int(input("Enter a grade: ").strip())
    grades[name] = grade

    name_to_remove = input("Enter a name to remove: ").strip()
    del grades[name_to_remove]
    grades.pop(name_to_remove, None)

    print(grades.keys())
    print(grades.values())

if __name__ == "__main__":
    main()