# Save as: session8_ex7_package_init.py

from mytools.helpers import title_case
from mytools.numbers import max_of_three

def main():
    # TODO:
    # 1. from mytools.helpers import title_case
    # 2. from mytools.numbers import max_of_three
    # 3. Prompt user for a string -> print title_case of it
    # 4. Prompt for three numbers -> print max_of_three

    sentence = input("Enter a string: ").strip()
    print(title_case(sentence))

    numbers = []
    for i in range(1, 4):
        numbers.append(int(input(f"Enter number #{i}: ").strip()))
    
    print(max_of_three(v for v in numbers))

if __name__ == "__main__":
    main()