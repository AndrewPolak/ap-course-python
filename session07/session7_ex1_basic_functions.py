# Save as: session7_ex1_basic_functions.py
def greet_user():
    # TODO:
    # 1. Prompt for username (input).
    # 2. Print "Hello, <username>!".
    username = input("Enter username: ").strip()
    print(f"Hello, {username}!")

def main():
    # Call greet_user() here
    greet_user()

if __name__ == "__main__":
    main()