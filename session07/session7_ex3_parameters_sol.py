# Save as: session7_ex3_parameters_sol.py

def add_numbers(a, b):
    return a + b

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = add_numbers(x, y)
    print(f"Sum = {result}")

if __name__ == "__main__":
    main()