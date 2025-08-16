# Student Result Analyzer
# Author: Ankit
# GitHub Project: Student-result-analyzer

def calculate_grade(percentage):
    """Function to return grade according to percentage"""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def main():
    print("Welcome to Student Result Analyzer")
    name = input("Enter student name: ")
    marks_obtained = float(input("Enter marks obtained: "))
    total_marks = float(input("Enter total marks: "))

    percentage = (marks_obtained / total_marks) * 100
    grade = calculate_grade(percentage)

    print(f"\nResult for {name}:")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
