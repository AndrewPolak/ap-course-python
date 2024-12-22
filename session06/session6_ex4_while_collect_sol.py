# Save as: session6_ex4_while_collect_sol.py

def main():
    words = []
    while True:
        w = input().strip()
        if w.lower() == "stop":
            break
        words.append(w)
    print(f"Words entered: {words}")

if __name__ == "__main__":
    main()