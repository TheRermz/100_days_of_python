# new_dict = {new_key:new_value for (key,value) in dict.items()}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Fred"]
student_scores = {student: random.randint(1, 100) for student in names}

print(student_scores)

passed_students = {
    student: score for (student, score) in student_scores.items() if score >= 60
}
print(passed_students)
