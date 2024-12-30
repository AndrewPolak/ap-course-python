# Save as: session13_ex3_pip_freeze.py

import subprocess


def main():
    """
    Programmatically call `pip freeze` and write the output to
    my_requirements.txt.
    If that is tricky (permissions, environment issues), you can replicate
    the concept with a docstring explanation or use os/system calls.
    """
    # TODO: implement
    result = subprocess.run(
        ['pip', 'freeze'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    with open('requirements.txt', 'w') as f:
        f.write(result.stdout.decode(encoding='utf-8').strip())


if __name__ == "__main__":
    main()
