# Save as: session11_ex2_file_write.py
import pathlib
import os

def main():
    # TODO:
    # 1. Collect lines in a list until user enters empty or "stop".
    # 2. Write them to "user_output.txt" in 'w' mode.
    # 3. Print "Saved lines to user_output.txt."
    try:
        f = open("user_output.txt", "w")
    except FileNotFoundError as e:
        print("Error:", e)
    else:
        # while (line := input().strip()) and len(line) != 0 and line != "stop":
        #     f.write(line + '\n')
        # f.close()

        line = input().strip()
        while True:
            f.write(line + '\n')
            line = input().strip()
            if len(line) == 0 or line == "stop":
                break

        f.close()

if __name__ == "__main__":
    main()