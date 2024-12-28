# Save as: session12_ex2_docstring_demo_sol.py

def func_a(x, y):
    """
    Multiply x and y.

    :param x: int or float
    :param y: int or float
    :return: product of x and y
    """
    return x * y

def func_b(name="Guest"):
    """
    Print a greeting for the given name.

    :param name: str, person's name
    """
    print(f"Hello, {name}!")

def main():
    result = func_a(3, 4)
    print("func_a(3,4) =", result)
    func_b("Alice")
    func_b()

if __name__ == "__main__":
    main()