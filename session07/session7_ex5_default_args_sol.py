# Save as: session7_ex5_default_args_sol.py

def format_name(first_name, last_name="Doe"):
    return f"{first_name} {last_name}"

def main():
    print(format_name("Alice", "Smith"))  # "Alice Smith"
    print(format_name("Bob"))            # "Bob Doe"

if __name__ == "__main__":
    main()