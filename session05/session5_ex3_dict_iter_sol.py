# Save as: session5_ex3_dict_iter_sol.py

def main():
    info = {}
    for i in range(3):
        key = input(f"Enter key #{i+1}: ").strip()
        value = input(f"Enter value #{i+1}: ").strip()
        info[key] = value

    # Print key -> value
    for k, v in info.items():
        print(f"{k} -> {v}")

    check_key = input("Which key to check? ").strip()
    if check_key in info:
        print(f"{check_key} found, value: {info[check_key]}")
    else:
        print("Key not found.")

if __name__ == "__main__":
    main()