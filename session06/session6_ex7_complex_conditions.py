# Save as: session6_ex7_complex_conditions.py
def main():
    # TODO:
    # 1. Prompt for x, y.
    # 2. If x==0 and y==0, print "Both are zero" and return.
    # 3. If exactly one is zero, print "One is zero" and return.
    # 4. Else check sign combos:
    #    - Both positive -> print "Both positive"
    #    - Both negative -> print "Both negative"
    #    - Otherwise -> "Mixed signs"
    x = int(input("Enter x: ").strip())
    y = int(input("Enter y: ").strip())

    if x > 0 and y > 0:
        print("Both positive")
    elif (x > 0 and y < 0) or (x < 0 and y > 0):
        print("Mixed signs")
    elif x < 0 and y < 0:
        print("Both negative")
    elif x * y == 0:
        if x + y == 0:
            print("Both are zero")
        else:
            print("One is zero")

if __name__ == "__main__":
    main()