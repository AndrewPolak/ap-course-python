# Save as: session6_ex6_loop_search.py

NUM_OF_WORDS = 5

def main():
    # TODO:
    # 1. Prompt user for target word.
    # 2. For 5 times, prompt a word.
    #    - If word == target, print "Found <target>!" and break.
    # 3. If never found, print "Not found."
    target = input("Enter target: ").strip()
    
    for i in range(NUM_OF_WORDS):
        word = input(f"Enter word #{i+1}: ").strip()
        if word == target:
            print(f"Found {target}!")
            break
    
    if word != target:
        print("Not found.")
    

if __name__ == "__main__":
    main()