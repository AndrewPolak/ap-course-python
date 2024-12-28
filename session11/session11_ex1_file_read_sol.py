# Save as: session11_ex1_file_read_sol.py

def main():
    try:
        with open("sample_input.txt", "r") as f:
            content = f.read()
            print(content, end="")  # 'end=""' to avoid double newlines
    except FileNotFoundError:
        print("Error: 'sample_input.txt' not found. Please create it first.")

if __name__ == "__main__":
    main()