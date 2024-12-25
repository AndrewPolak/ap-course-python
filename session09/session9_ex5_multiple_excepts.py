# Save as: session9_ex5_multiple_excepts.py
def main():
    # TODO:
    # 1. Prompt for two floats.
    # 2. try:
    #       parse them
    #       compute division
    #    except ValueError -> "Invalid float input!"
    #    except ZeroDivisionError -> "Cannot divide by zero!"
    # 3. print result if successful
    try:
        x = float(input("Enter float 1: ").strip())
        y = float(input("Enter float 2: ").strip())
        result = x / y
        print(f"Quotient of {x} and {y} = {result}")
    except ValueError:
        print("Error: Invalid float input!")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    
if __name__ == "__main__":
    main()