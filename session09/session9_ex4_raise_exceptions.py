# Save as: session9_ex4_raise_exceptions.py
def validate_username(username):
    # TODO:
    # 1. If empty, raise ValueError("Username cannot be empty")
    # 2. If spaces, raise ValueError("Username cannot contain spaces")
    # 3. else return "Valid username"
    if len(username) == 0:
        raise ValueError("Username cannot be empty")
    
    if ' ' in username:
        raise ValueError("Username cannot contain spaces")
    
    return "Valid username"

def main():
    # 1. Prompt for username
    # 2. try:
    #       print(validate_username(...))
    #    except ValueError as e:
    #       print("Error:", e)
    username = input("Enter username: ")
    try:
        print(validate_username(username))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()