# Save as: session9_ex1_basic_try_except_sol.py
def main():
    try:
        num_str = input("Enter an integer: ")
        num = int(num_str)
        print(f"You entered {num}")
    except ValueError:
        print("Invalid integer!")

if __name__ == "__main__":
    main()