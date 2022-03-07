students = []

students.append("Peter")
students.append("Paul")
students.append("Mary")

print(type(students))
print(students)
print(students[1])
print(len(students))
print(students[-1])#last element of list

for student in students:
    print(student)


students.append('Cooper')
print(students)
students.sort()#sorts alphabetical
print(students)
#what was once element 0 is now something else, in this case, element 3
students.reverse()#reverse order
print(students)
x = students.pop() #pop removes last item from list but can also return it
print(students)
print(x)
#students.remove[0] doesnt work
students.remove("peter")
print(students)

new_students = ["Simon", "Andrew", "Martha", "Andrea"]
grades = [23, 45, 79, 32]

for i in range(len(new_students)):
    print(new_students[i], "got the grade", grades[i])


name = 'cooper'
letters = list(name)
print(letters)

name = "Cooper Manderson"
name_parts = name.split()
print(name_parts)
first_name = name_parts[0]
last_name = name_parts[1]
print(last_name.upper(), first_name)