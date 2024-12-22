# Save as: session6_ex3_for_sum_sol.py

def main():
    numbers = []
    for _ in range(5):
        num = int(input().strip())
        numbers.append(num)

    total = 0
    for n in numbers:
        total += n

    print(f"Sum: {total}")

if __name__ == "__main__":
    main()