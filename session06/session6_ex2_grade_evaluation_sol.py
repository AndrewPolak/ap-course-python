# Save as: session6_ex2_grade_evaluation_sol.py

def main():
    score = int(input().strip())
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