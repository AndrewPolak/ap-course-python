# Save as: session7_ex5_default_args.py
def format_name(first_name, last_name="Doe"):
    # TODO: print or return the formatted "<first_name> <last_name>"
    return f"{first_name} {last_name}"

def main():
    print(format_name(last_name="Smith", first_name="Alice"))
    print(format_name("Bob"))
    # add more tests

if __name__ == "__main__":
    main()