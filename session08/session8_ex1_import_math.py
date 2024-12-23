# Save as: session8_ex1_import_math.py
import math

def main():
    # TODO:
    # 1. import math
    # 2. Prompt user for a number.
    # 3. Use math.sqrt() to compute square root.
    # 4. Print the result and math.pi
    number = int(input("Enter a number: ").strip())
    print(f"sqrt({number}) = {math.sqrt(number)}")
    print(math.pi)

if __name__ == "__main__":
    main()