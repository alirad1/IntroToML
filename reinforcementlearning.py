student_scores = { "Alice": 85, "Bob": 92, "Charlie": 78, "Dana": 82, "Emily": 95 }
names = ["Alice", "Brian", "Charlie", "David", "Emily", "Fred"]
print()
for i in names:
    if i in student_scores:
        print(i, student_scores[i])
    else:
        student_scores[i] = 0
        print(i, "added")
print(student_scores)

student_scores = {
    "Alice": [85, 87, 92, 96],
    "Bob": [92, 91, 94, 84], 
    "Charlie": [78, 80, 82, 84] }

print(student_scores["Bob"][1])
student_scores["Charlie"][2] = 85
print(student_scores["Charlie"][1])
print(student_scores)


print()