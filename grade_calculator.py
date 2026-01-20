# grade_calculator.py

def calculate_grade(marks):
    # Validate marks
    if marks < 0 or marks > 100:
        return "❌ Invalid marks! Please enter between 0 and 100."

    # Business logic with conditions
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    # Nested condition example
    if grade == "F":
        return f"Grade: {grade} → Needs Improvement!"
    else:
        return f"Grade: {grade} → Good job!"

# Main program
try:
    marks_input = int(input("Enter your marks (0-100): "))
    print(calculate_grade(marks_input))
except ValueError:
    print("❌ Please enter a valid integer.")