# Save as: session6_ex2_grade_evaluation.py
def main():
    # TODO:
    # 1. Prompt for a score, convert to int.
    # 2. Use if/elif/else to classify the score into letter grade.
    # 3. Print the letter grade.
    score = int(input("Enter a numerical score (0 to 100): ").strip())

    if score < 0 or score > 100:
        exit(1)
    
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

if __name__ == "__main__":
    main()