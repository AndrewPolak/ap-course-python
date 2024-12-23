# Save as: session8_ex5_aliasing.py

import random as rnd

def main():
    # TODO:
    # 1. import random as rnd
    # 2. Prompt user for n
    # 3. Generate list of n random ints in [1,100]
    # 4. Print the list

    n = int(input("Enter n: ").strip())
    selection = [rnd.randint(1, 100) for x in range(n)]
    print(f"Random list of {n} number: {selection}")


if __name__ == "__main__":
    main()