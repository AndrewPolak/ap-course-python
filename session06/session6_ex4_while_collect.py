# Save as: session6_ex4_while_collect.py
def main():
    # TODO:
    # 1. Initialize an empty list `words`.
    # 2. Use a while True loop.
    # 3. Prompt for input, strip it.
    # 4. If it is "stop", break out of the loop.
    # 5. Otherwise, append to the list.
    # 6. Print the final list after the loop.

    words = []

    while True:
        word = input().strip()
        if word == "stop":
            break
        words.append(word)

    print("Words entered: ", words)


if __name__ == "__main__":
    main()