# Save as: session5_ex1_dict_create_sol.py

def main():
    name = input().strip()
    phone = input().strip()
    phonebook = {name: phone}
    print(f"Dictionary: {phonebook}")
    print(f"{name}'s number is: {phonebook[name]}")

if __name__ == "__main__":
    main()