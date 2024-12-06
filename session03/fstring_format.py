# Save as: fstring_format.py
def main():
    # TODO:
    # 1. Prompt for first_name.
    # 2. Prompt for favorite_color.
    # 3. Print using an f-string: "Hello, <first_name>! I hear your favorite color is <favorite_color>."
    first_name = input().strip()
    favorite_color = input().strip()
    print(f"Hello, {first_name}! I heard your favorite colour is {favorite_color}.")
    pass

if __name__ == "__main__":
    main()
