# Save as: session8_ex3_custom_module.py
# Create myutils.py in the same directory with add() and subtract().

import myutils

def main():
    # TODO:
    # 1. import myutils
    # 2. Prompt user for two numbers
    # 3. Print add(...) and subtract(...)
    x = int(input("Enter x: ").strip())
    y = int(input("Enter y: ").strip())
    print(f"sum({x}, {y}) = {myutils.add(x,y)}")
    print(f"subtract({x}, {y}) = {myutils.subtract(x,y)}")

if __name__ == "__main__":
    main()