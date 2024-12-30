# Save as: session13_ex5_venv_scripting_sol.py
import subprocess
import sys
import os


def main():
    env_name = "myenv_script"
    print(f"Creating virtual environment: {env_name}")
    subprocess.run([sys.executable, "-m", "venv", env_name])

    # We won't attempt to activate it within the script. We'll just show how.
    if os.path.isdir(env_name):
        print(f"Successfully created {env_name}/")
        print("To activate:")
        print(f"  source {env_name}/bin/activate  (Linux/macOS)")
        print(f"  {env_name}\\Scripts\\activate   (Windows)")
    else:
        print("Failed to create the environment.")


if __name__ == "__main__":
    main()

