# Save as: session7_ex7_utilities_sol.py

def is_valid_username(name, min_length=3):
    return len(name) >= min_length

def main():
    username = input("Enter username: ")
    if is_valid_username(username):
        print("Valid username")
    else:
        print("Invalid username")

if __name__ == "__main__":
    main()