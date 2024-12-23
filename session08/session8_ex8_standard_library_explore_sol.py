# Save as: session8_ex8_standard_library_explore_sol.py
import collections  # example choice

def main():
    # 1. Demonstrate collections.Counter
    fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counter = collections.Counter(fruits)
    print(f"Counter for fruits: {counter}")

    # 2. Demonstrate collections.deque (double-ended queue)
    dq = collections.deque([1, 2, 3])
    dq.appendleft(0)
    dq.append(4)
    print(f"Deque after modifications: {dq}")

if __name__ == "__main__":
    main()