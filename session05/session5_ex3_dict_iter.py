# Save as: session5_ex3_dict_iter.py
def main():
    # TODO:
    # 1. Prompt for 3 key-value pairs. Store in dict.
    # 2. Iterate using .items() and print each pair.
    # 3. Prompt for a key to search.
    # 4. If found, print the value. Else, "Key not found."

    city_to_country = {}

    for _ in range(3):
        city = input("Enter city: ").strip()
        country = input("Enter country: ").strip()
        city_to_country[city] = country
    
    city = input("Enter a city to check: ").strip()

    print("city not in database" if city not in city_to_country else city_to_country[city])

if __name__ == "__main__":
    main()