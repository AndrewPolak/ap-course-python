# Save as: session7_ex4_function_scope_sol.py

counter = 0

def increment():
    global counter  # approach #1: use 'global' (less recommended in larger programs)
    counter += 1

def main():
    print(f"Initial counter: {counter}")
    increment()
    print(f"Counter after increment: {counter}")

if __name__ == "__main__":
    main()