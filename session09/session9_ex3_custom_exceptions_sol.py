# Save as: session9_ex3_custom_exceptions_sol.py

class NegativeNumberError(Exception):
    pass

def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            raise NegativeNumberError(f"Input {num} is negative!")
        print(f"Valid input: {num}")
    except NegativeNumberError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()