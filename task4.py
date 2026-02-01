"""
Day 4 Activity: Parse nested dictionaries (student database).
Tasks:
1) Get Alice's AI301 grade
2) Calculate Bob's GPA (weighted by credits)
3) Find all students in CS101
4) Get average grade across all courses
5) Find student with highest GPA
"""

students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}

# TODO: Implement the tasks above using nested dict access.

Alice_grade = students["S001"]["courses"]["AI301"]["grade"]
print(Alice_grade)

Bob_courses = students["S002"]["courses"]
wighted_sum = sum(x["grade"] * x["credits"] for x in Bob_courses.values())
credits = sum(x["credits"] for x in Bob_courses.values())
Bob_gpa = wighted_sum / credits if credits else 0.0
print(Bob_gpa)

cs101_students = [
    student["name"]
    for student in students.values()
    if "CS101" in student["courses"]
]
print(cs101_students)

all_grades = []
for s in students.values():
    for course in s["courses"].values():
        all_grades.append(course["grade"])
        average_grade = sum(all_grades) / len(all_grades)
print(all_grades)

def calc_gpa(courses):
    weighted = sum(c["grade"] * c["credits"] for c in courses.values())
    credits = sum(c["credits"] for c in courses.values())
    return weighted / credits if credits else 0.0

highest_student = None
highest_gpa = -1

for s in students.values():
    gpa = calc_gpa(s["courses"])
    if gpa > highest_gpa:
        highest_gpa = gpa
        highest_student = s["name"]

print(highest_student, highest_gpa)