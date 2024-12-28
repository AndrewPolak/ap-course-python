# Save as: session12_ex1_pep8_check_sol.py
# Example of a script with corrected style after checking with flake8.

def add_nums(a, b):
    """Return sum of a and b."""
    return a + b


def main():
    x = 10
    y = 5
    total = add_nums(x, y)
    print("Total:", total)


if __name__ == "__main__":
    main()