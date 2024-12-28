# Save as: session11_ex8_read_config_sol.py

def main():
    config = {}
    try:
        with open("config_demo.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    except FileNotFoundError:
        print("config_demo.txt not found, using default empty config.")

    print("Config dictionary:", config)

if __name__ == "__main__":
    main()