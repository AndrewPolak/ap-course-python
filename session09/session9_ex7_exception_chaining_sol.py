# Save as: session9_ex7_exception_chaining_sol.py
def process_data(data):
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    if len(data) == 0:
        raise ValueError("No data provided")
    return "Data processed"

def main():
    try:
        # Suppose we prompt user for how to test it
        choice = input("Enter 'empty', 'nonlist', or 'good': ")
        if choice == "empty":
            user_data = []
        elif choice == "nonlist":
            user_data = "I'm not a list"
        else:
            user_data = [1,2,3]

        try:
            result = process_data(user_data)
            print(result)
        except (ValueError, TypeError) as e:
            # Chain it
            raise RuntimeError("Data processing failed") from e

    except RuntimeError as re:
        # Print the entire chain
        print("Caught RuntimeError:", re)
        print("Cause:", re.__cause__)

if __name__ == "__main__":
    main()