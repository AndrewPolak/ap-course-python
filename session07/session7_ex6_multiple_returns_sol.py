# Save as: session7_ex6_multiple_returns_sol.py

def divide_and_mod(a, b):
    return a // b, a % b

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    quotient, remainder = divide_and_mod(a, b)
    print(f"Quotient = {quotient}, Remainder = {remainder}")

if __name__ == "__main__":
    main()