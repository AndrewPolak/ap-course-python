# Save as: session7_ex2_docstrings_sol.py

def power(base, exponent):
    """
    Return base raised to exponent.
    :param base: number to be raised
    :param exponent: power to raise base by
    :return: base^exponent
    """
    return base ** exponent

def main():
    print(f"2^3 = {power(2, 3)}")
    print(f"5^2 = {power(5, 2)}")

if __name__ == "__main__":
    main()