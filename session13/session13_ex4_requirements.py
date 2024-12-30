# Save as: session13_ex4_requirements.py

def main():
    """
    1. Open 'requirements.txt'.
    2. Print each line (package==version).
    3. Optionally, mention how you'd run `pip install -r requirements.txt`.
    """
    # TODO: implement
    try:
        f = open('requirements.txt', 'r')
    except FileNotFoundError as e:
        print(e)
        exit(1)

    print(f.read())
    f.close()


if __name__ == "__main__":
    main()
