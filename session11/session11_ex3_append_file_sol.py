# Save as: session11_ex3_append_file_sol.py

def main():
    line = input("Enter a line to append: ")
    with open("journal.txt", "a") as f:
        f.write(line + "\n")
    print("Appended to journal.txt")

if __name__ == "__main__":
    main()