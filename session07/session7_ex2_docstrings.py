# Save as: session7_ex2_docstrings.py
def power(base, exponent):
    """
    TODO: Describe what this function does, its params, and returns.
    Returns 'base' to the power of 'exponent'

    :param base: a number to which a power is taken
    :param exponent: the power which is applied to base
    :return: base^exponent
    """
    return base ** exponent

def main():
    print(f"2^3 = {power(2, 3)}")
    print(f"5^2 = {power(5, 2)}")
    # Add more tests if you want

if __name__ == "__main__":
    main()