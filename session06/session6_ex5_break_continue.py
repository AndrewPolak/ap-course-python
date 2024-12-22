# Save as: session6_ex5_break_continue.py
def main():
    # TODO:
    # 1. Prompt user for a single line of comma-separated numbers.
    # 2. Convert them to a list of ints.
    # 3. For each number in the list:
    #       - if num == -1: break
    #       - if num == 0: continue
    #       - else: print(num)

    print("Enter a list of numbers (comma-separated): ")

    numbers = [int(x.strip()) for x in input().split(',')]

    for num in numbers:
        if num == -1:
            break
        elif num == 0:
            continue
        print(num)

if __name__ == "__main__":
    main()