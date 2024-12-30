# Save as: session13_ex5_venv_scripting.py

import subprocess

def main():
    """
    Attempt to create a venv folder (e.g., 'myenv') programmatically
    using subprocess or venv module.
    """
    # TODO: implement
    subprocess.run(['python3', '-m', 'venv', 'myvenv_s13_e05'])


if __name__ == "__main__":
    main()