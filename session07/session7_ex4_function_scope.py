# Save as: session7_ex4_function_scope.py
counter = 0

def increment():
    # TODO: increment the counter
    global counter
    counter += 1

def main():
    print(f"Initial counter: {counter}")
    increment()
    print(f"Counter after increment: {counter}")

if __name__ == "__main__":
    main()