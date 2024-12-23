# Save as: session8_ex3_custom_module_sol.py
import myutils  # <-- This file is expected to be in the same directory.

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"add({a}, {b}) = {myutils.add(a, b)}")
    print(f"subtract({a}, {b}) = {myutils.subtract(a, b)}")

if __name__ == "__main__":
    main()