
# Save as: session5_ex6_dict_set_combine.py
def main():
    # TODO:
    # 1. Prompt for 3 (item, quantity) pairs, store in dict.
    # 2. Create set of items with quantity > 0.
    # 3. Print that set.
    item_dict = {}

    for i in range(3):
        item_number = i + 1
        item_name = input(f"Enter item #{item_number} name: ")
        item_quantity = int(input(f"Enter item #{item_number} quantity: "))
        item_dict[item_name] = item_quantity

    item_set = {k for k, q in item_dict.items() if q > 0}
    
    print(item_set)

if __name__ == "__main__":
    main()