# Save as: session5_ex4_set_basics_sol.py

def main():
    items = set()
    for _ in range(5):
        item = input().strip()
        items.add(item)
    print(f"Set of items: {items}")

    check_item = input().strip()
    print(f"Is '{check_item}' in the set? {check_item in items}")
    print(f"Number of unique items: {len(items)}")

if __name__ == "__main__":
    main()