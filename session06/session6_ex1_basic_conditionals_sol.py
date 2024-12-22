# Save as: session6_ex1_basic_conditionals_sol.py

def main():
    num = int(input().strip())
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

if __name__ == "__main__":
    main()