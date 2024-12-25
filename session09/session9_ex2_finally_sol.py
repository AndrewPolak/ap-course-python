# Save as: session9_ex2_finally_sol.py
def main():
    filename = input("Enter filename: ")
    file_obj = None
    try:
        file_obj = open(filename, "r")
        data = file_obj.read()
        print("File content:", data)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    finally:
        print("Attempted file operation.")
        if file_obj:
            file_obj.close()

if __name__ == "__main__":
    main()