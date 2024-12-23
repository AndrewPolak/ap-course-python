# Save as: session8_ex4_from_import.py

from math import factorial as fact

def main():
    # TODO:
    # 1. from math import factorial as fact
    # 2. Prompt for an integer
    # 3. Print factorial of that integer
    n = int(input("Enter an integer: ").strip())
    print(f"factorial({n}) = {fact(n)}")

if __name__ == "__main__":
    main()