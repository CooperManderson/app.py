student_grades = {
    "Simon": 45,
    "Alison": 78,
    "John": 72,
    "Tracy": 83,
    "Zac": 22
}

print(type(student_grades))
print(student_grades)

#print the student names and their grades
for k, v in student_grades.items():
    print(k, "got", v)

#ask for a name and return the grade or 'not found'

name = input("what name would you like the grade of? ")
if name in student_grades:
    print(student_grades[name])
else:
    print("name not found")

#print a list of all the student names -> ie the keys
print(list(student_grades.keys()))
student_names = list(student_grades.keys())
