# Save as: session7_ex7_utilities.py
def is_valid_username(name, min_length=3):
    """
    TODO: description
    """
    # TODO: return True/False based on length check
    return len(name) >= min_length

def main():
    username = input("Enter username: ").strip()
    if is_valid_username(username):
        print("Valid username")
    else:
        print("Invalid username")

if __name__ == "__main__":
    main()