# Save as: session9_ex2_finally.py
def main():
    # TODO:
    # 1. Prompt for a filename.
    # 2. Try opening it, read or do something trivial.
    # 3. except FileNotFoundError -> print error
    # 4. finally -> print "Attempted file operation."
    filename = input("Enter filename: ").strip()
    try:
        f = open(filename, 'r')
        f.close()
    except FileNotFoundError:
        print("Error: file not found")
    finally:
        print("Attempted file operation.")

if __name__ == "__main__":
    main()