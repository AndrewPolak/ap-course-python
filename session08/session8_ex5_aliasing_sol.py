# Save as: session8_ex5_aliasing_sol.py
import random as rnd

def main():
    n = int(input("Enter n: "))
    numbers = [rnd.randint(1, 100) for _ in range(n)]
    print(f"Random list of {n} numbers: {numbers}")

if __name__ == "__main__":
    main()