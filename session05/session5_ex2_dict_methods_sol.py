# Save as: session5_ex2_dict_methods_sol.py

def main():
    grades = {"Alice": 85, "Bob": 90}
    new_name = input().strip()
    new_grade_str = input().strip()
    new_grade = int(new_grade_str)
    grades[new_name] = new_grade  # add or update

    remove_name = input().strip()
    grades.pop(remove_name, None)  # remove if exists, else do nothing

    print(f"Keys: {list(grades.keys())}")
    print(f"Values: {list(grades.values())}")

if __name__ == "__main__":
    main()