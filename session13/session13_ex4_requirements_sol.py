# Save as: session13_ex4_requirements_sol.py

def main():
    try:
        with open("requirements.txt", "r") as f:
            lines = f.readlines()
        print("Packages from requirements.txt:")
        for line in lines:
            print(line.strip())
    except FileNotFoundError:
        print("No requirements.txt found. Please create one or run pip freeze > requirements.txt.")

    print("\nTo install these packages, run:\n  pip install -r requirements.txt")

if __name__ == "__main__":
    main()