# Save as: session11_ex2_file_write_sol.py

def main():
    lines = []
    while True:
        user_input = input("Enter text (or 'stop' / empty to finish): ")
        if not user_input or user_input.lower() == "stop":
            break
        lines.append(user_input)

    with open("user_output.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")
    print("Saved lines to user_output.txt")

if __name__ == "__main__":
    main()