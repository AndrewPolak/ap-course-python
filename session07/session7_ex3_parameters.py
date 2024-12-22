# Save as: session7_ex3_parameters.py
def add_numbers(a, b):
    """
    Returns the sum of 'a' and 'b'
    : a : the first number of the sum
    : b : the second number of the sum
    """
    # TODO: return sum of a and b
    return (a + b)

def main():
    # 1. Prompt for two integers
    # 2. Pass to add_numbers
    # 3. Print the result
    first = int(input("Enter first number: ").strip())
    second = int(input("Enter second number: ").strip())
    print(f"Sum = {add_numbers(first, second)}")

if __name__ == "__main__":
    main()