studentGrades = {
    'Alice': 90,
    'Bob': 78,
    'Charlie': 92,
    'David': 88,
    'Eve': 76
}

studentGrades['Alice'] = 10

for student, grade in studentGrades.items():
    if grade > 85:
        print(f"{student} has a grade higher than 85.")
