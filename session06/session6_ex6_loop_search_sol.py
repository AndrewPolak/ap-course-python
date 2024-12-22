# Save as: session6_ex6_loop_search_sol.py

def main():
    target = input("Enter target: ").strip()
    found = False
    for i in range(1, 6):
        word = input(f"Enter word #{i}: ").strip()
        if word == target:
            print(f"Found {target}!")
            found = True
            break
    if not found:
        print("Not found.")

if __name__ == "__main__":
    main()