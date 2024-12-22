# Save as: session7_ex6_multiple_returns.py
def divide_and_mod(a, b):
    # TODO: return (a//b, a%b)
    return a // b, a % b

def main():
    # 1. Prompt for a, b
    # 2. call divide_and_mod
    # 3. print the results
    a = int(input("Enter a: ").strip())
    b = int(input("Enter b: ").strip())
    quotient, remainder = divide_and_mod(a, b)
    print(f"Quotient = {quotient}, Remainder = {remainder}")

if __name__ == "__main__":
    main()