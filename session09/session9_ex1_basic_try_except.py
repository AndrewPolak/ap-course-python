# Save as: session9_ex1_basic_try_except.py
def main():
    # TODO:
    # 1. Prompt for an integer.
    # 2. Wrap in try/except ValueError.
    # 3. Print success or "Invalid integer!".
    try:
        number = int(input("Enter an integer: ").strip())
        print(f"You entered {number}")
    except ValueError:
        print("Invalid integer!")

if __name__ == "__main__":
    main()