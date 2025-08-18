student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for key, value in student_scores.items():
    if value >= 91:
        student_scores[key] = 'Outstanding'
    elif value >= 81:
        student_scores[key] = "Exceeds Expectations"
    elif value >= 71:
        student_scores[key] = "Acceptable"
    else:
        student_scores[key] = "Fail"
student_grades = student_scores
print(student_grades)

#########################################################
# Explanation from course

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Create an empty dictionary to collect the new values.
student_grades = {}

# Loop through each key in the student_scores dictionary
for student in student_scores:

    # Get the value (student score) by using the key each time.
    score = student_scores[student]

    # Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
#########################################################