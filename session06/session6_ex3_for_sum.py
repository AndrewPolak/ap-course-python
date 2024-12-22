
# Save as: session6_ex3_for_sum.py
def main():
    # TODO:
    # 1. Prompt for 5 integers.
    # 2. Append each integer to a list.
    # 3. Use a for loop to sum them.
    # 4. Print the sum.
    numbers = []

    sum = 0
    for i in range(5):
        numbers.append(int(input("Enter an integer: ").strip()))

    for value in numbers:
        sum += value
    
    print(f"Sum: {sum}")

if __name__ == "__main__":
    main()