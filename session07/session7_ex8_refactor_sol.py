# Save as: session7_ex8_refactor_sol.py

def check_length(item, min_length=2):
    if len(item) < min_length:
        print("Too short!")
    else:
        print("Okay.")

def main():
    item1 = input("Enter item #1: ")
    check_length(item1)

    item2 = input("Enter item #2: ")
    check_length(item2)

    item3 = input("Enter item #3: ")
    check_length(item3)

    print("Done.")

if __name__ == "__main__":
    main()