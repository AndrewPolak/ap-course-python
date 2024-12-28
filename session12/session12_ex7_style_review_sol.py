# Save as: session12_ex7_style_review_sol.py
# After reviewing & refactoring for style, naming, docstrings, etc.

def calculate_product(a, b):
    """
    Return the product of two numbers.

    :param a: int or float
    :param b: int or float
    :return: product of a and b
    """
    return a * b


def main():
    """Prompt user, read two numbers, compute product, print result."""
    num1_str = input("Enter first number: ")
    num2_str = input("Enter second number: ")

    # convert to float
    num1 = float(num1_str)
    num2 = float(num2_str)

    result = calculate_product(num1, num2)
    print("Product =", result)


if __name__ == "__main__":
    main()
