# Save as: session11_ex8_read_config.py

import pathlib as Path

def main():
    """
    1. open config_demo.txt in 'r'
    2. parse each line as key=value
    3. store in a dict
    4. print the dict
    """
    # TODO: implement

    try:
        f = open("config_demo.txt", "r")
    except FileNotFoundError as e:
        print(e)
        exit(1)

    configs = {}
    for line in f:
        line = line.strip()
        if not line or "=" not in line:
            continue
        key, value = line.split('=', maxsplit=1)
        configs[key.strip()] = value.strip()

    # or this monstrosity could work:
    # configs = {k.strip(): v.strip() for line in f for k, v in [line.split('=', maxsplit=1)]}

    print(configs)

    f.close()


if __name__ == "__main__":
    main()