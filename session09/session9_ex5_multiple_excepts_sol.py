# Save as: session9_ex5_multiple_excepts_sol.py
def main():
    try:
        a_str = input("Enter first float: ")
        b_str = input("Enter second float: ")
        a = float(a_str)
        b = float(b_str)
        result = a / b
        print(f"Result = {result}")
    except ValueError:
        print("Invalid float input!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

if __name__ == "__main__":
    main()