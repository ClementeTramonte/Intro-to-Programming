#Function takes number and converts to letter grade

def calculate_letter_grade(average_score):
    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
        return "C"
    elif average_score >= 60:
        return "D"
    else:
        return "F"

student_name = input("Enter student name: ")
grade1 = float(input("Enter Grade 1: "))
grade2 = float(input("Enter Grade 2: "))
grade3 = float(input("Enter Grade 3: "))
grade4 = float(input("Enter Grade 4: "))
grade5 = float(input("Enter Grade 5: "))

total_score = sum([grade1, grade2, grade3, grade4, grade5])
average_score = total_score / 5
letter_grade = calculate_letter_grade(average_score)

print(student_name)
print("Average: %.1f" % average_score)
print("Letter Grade: ", letter_grade)

