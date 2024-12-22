def main():
    x = int(input().strip())
    y = int(input().strip())

    # Zero checks override others
    if x == 0 and y == 0:
        print("Both are zero")
        return
    if (x == 0 and y != 0) or (x != 0 and y == 0):
        print("One is zero")
        return

    # Now check sign combos
    if x > 0 and y > 0:
        print("Both positive")
    elif x < 0 and y < 0:
        print("Both negative")
    else:
        print("Mixed signs")

if __name__ == "__main__":
    main()