# Save as: session9_ex4_raise_exceptions_sol.py
def validate_username(username):
    if not username:
        raise ValueError("Username cannot be empty")
    if " " in username:
        raise ValueError("Username cannot contain spaces")
    return "Valid username"

def main():
    username = input("Enter username: ")
    try:
        result = validate_username(username)
        print(result)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()