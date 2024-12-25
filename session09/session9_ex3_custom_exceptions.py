# Save as: session9_ex3_custom_exceptions.py

class NegativeNumberError(Exception):
    pass

def main():
    # TODO:
    # 1. Prompt user for an integer.
    # 2. If negative, raise NegativeNumberError("Input <num> is negative!")
    # 3. Wrap in try/except.
    try:
        number = int(input("Enter a positive integer: ").strip())
        if number < 0:
            raise NegativeNumberError(f"Input {number} is negative!")
        print(f"You input {number}")
    except ValueError:
        print("Error: invalid input: exiting...")
    except NegativeNumberError as e:
        print("Error:", e)
    

if __name__ == "__main__":
    main()