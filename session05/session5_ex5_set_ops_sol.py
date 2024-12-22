# Save as: session5_ex5_set_ops_sol.py

def main():
    first_line = input("Enter first list (comma separated): ").strip()
    second_line = input("Enter second list (comma separated): ").strip()

    set1 = set(x.strip() for x in first_line.split(','))
    set2 = set(x.strip() for x in second_line.split(','))

    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference (first-second): {set1 - set2}")
    print(f"Symmetric difference: {set1 ^ set2}")

if __name__ == "__main__":
    main()