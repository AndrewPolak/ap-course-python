# Save as: session6_ex1_basic_conditionals.py
def main():
    # TODO:
    # 1. Prompt the user for an integer.
    # 2. Convert to int.
    # 3. Check if positive, negative, or zero using if/elif/else.
    # 4. Print the result.
    number = int(input("Enter an integer: ").strip())
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

if __name__ == "__main__":
    main()