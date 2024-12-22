# Save as: session6_ex5_break_continue_sol.py

def main():
    line = input().strip()
    str_nums = line.split(',')
    nums = [int(x.strip()) for x in str_nums]

    for n in nums:
        if n == -1:
            break
        if n == 0:
            continue
        print(n)

if __name__ == "__main__":
    main()