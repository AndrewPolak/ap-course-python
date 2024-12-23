# Save as: session8_ex8_standard_library_explore.py

import datetime

from collections import deque

def main():
    # TODO:
    # 1. import a standard library module of your choice
    # 2. demonstrate 2 features

    d = deque()
    d.append(5)
    d.appendleft(3)
    print(d)

if __name__ == "__main__":
    main()