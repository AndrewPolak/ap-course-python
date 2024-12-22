# Save as: session7_ex8_refactor.py

def check_length(item, min_length=2):
    if len(item) < min_length:
        print("Too short!")
    else:
        print("Okay.")

def main():
    # Original code (unrefactored example):
    #
    # item1 = input("Enter item #1: ")
    # if len(item1) < 2:
    #     print("Too short!")
    # else:
    #     print("Okay.")
    
    # item2 = input("Enter item #2: ")
    # if len(item2) < 2:
    #     print("Too short!")
    # else:
    #     print("Okay.")
    
    # item3 = input("Enter item #3: ")
    # if len(item3) < 2:
    #     print("Too short!")
    # else:
    #     print("Okay.")
    
    # print("Done.")

    # TODO:
    # 1. Implement check_length(item, min_length=2).
    # 2. Rewrite the above logic using that function.
    for i in range(1, 4):
        item = input(f"Enter item #{i}: ")
        check_length(item)
    
    print("Done.")

if __name__ == "__main__":
    main()