# Save as: session8_ex7_package_init_sol.py

def main():
    # In a real scenario, you'd have:
    # mytools/helpers.py -> title_case(text)
    # mytools/numbers.py -> max_of_three(a,b,c)
    #
    # Then you'd do:
    # from mytools.helpers import title_case
    # from mytools.numbers import max_of_three

    # For demonstration, we'll define them inline:
    def title_case(text):
        return " ".join(word.capitalize() for word in text.split())

    def max_of_three(a, b, c):
        return max(a, b, c)

    user_text = input("Enter a string: ")
    print("Title-cased:", title_case(user_text))

    nums = input("Enter three numbers (comma-separated): ").split(",")
    a, b, c = map(float, nums)
    print("Max of three:", max_of_three(a, b, c))

if __name__ == "__main__":
    main()