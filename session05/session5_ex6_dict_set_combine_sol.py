# Save as: session5_ex6_dict_set_combine_sol.py

def main():
    inventory = {}
    for _ in range(3):
        item = input().strip()
        qty_str = input().strip()
        qty = int(qty_str)
        inventory[item] = qty

    in_stock = {k for k, v in inventory.items() if v > 0}
    print(f"In-stock items: {in_stock}")

if __name__ == "__main__":
    main()