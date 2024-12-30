# Save as: session13_ex3_pip_freeze_sol.py
import subprocess

def main():
    # Call pip freeze using subprocess, capture output
    result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
    frozen = result.stdout.strip()

    with open("my_requirements.txt", "w") as f:
        f.write(frozen + "\n")

    print("Saved current dependencies to my_requirements.txt")

if __name__ == "__main__":
    main()