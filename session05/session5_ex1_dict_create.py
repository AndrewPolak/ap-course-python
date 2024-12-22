# Save as: session5_ex1_dict_create.py
def main():
    # TODO:
    # 1. Prompt for a name and phone number.
    # 2. Create a dictionary {name: phone_number}.
    # 3. Print the dictionary.
    # 4. Print the phone number using dict access.
    name = input("Enter your name: ").strip()
    phone_number = input("Enter your phone number: ").strip()
    
    phonebook = { name:phone_number }

    print(phonebook)
    print(phonebook[name])

    pass

if __name__ == "__main__":
    main()