# Save as: session11_ex3_append_file.py

def main():
    # TODO:
    # 1. Prompt user for one line of text.
    # 2. Open "journal.txt" in "a" mode.
    # 3. Write the line + "\n".
    # 4. Print confirmation.
    line = input("Enter one line of text: ").strip()

    try:
        with open("journal.txt", "a") as f:
            f.write(line + '\n')
        print("Appended to journal.txt")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()