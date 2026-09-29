# import math
# d=50
# a=40
# r=math.radians(a)
# h=d*math.tan(r)
# print("Height of the tree is:",h,"metres")


# suppose a drone travels 100 m at an angle of 30degree
# above the horizontal.find its vertical displacement
import math
d=100
a=30
r=math.radians(a)
vd=d*math.sin(r)
print("Height of the tree is:",vd,"metres")


#Horizontal displacement
# import math
# d=200
# a=30
# r=math.radians(a)
# hd=d*math.cos(r)
# print("Horizontal displacement is:",hd,"metres")


# from datetime import datetime
# now = datetime.now()
# print("Current date and time:", now)
# print(now.strftime("%d-%m-%y"))
# print(now.strftime("%d/%m/%Y"))
# print(now.strftime("%B %d,%Y"))


# from datetime import date,datetime
# dob=date(2004,12,2)
# today=date.today()
# age=today.year-dob.year
# if((today.month,today.day)<(dob.month,dob.day)):
#     age-=1
# print("Age is:",age)
# start=date(2026,9,1)
# end=date(2026,12,31)
# deff=end-start
# print("Difference between two dates is:",deff.days,"days")





# #Scenario 1

# from collections import Counter
# from functools import reduce
# import random
# from datetime import date

# students = {
#     "Tarun": [82, 91, 78],
#     "Karthik": [65, 72, 68],
#     "Chadrika": [91, 95, 89],
#     "Trisha": [76, 81, 79],
#     "Atul": [88, 84, 92]
# }

# averages = {}

# for name, marks in students.items():
#     total = reduce(lambda x, y: x + y, marks)
#     averages[name] = total / len(marks)

# grades = []

# for name, avg in averages.items():
#     print(name, ":", round(avg, 2))

#     if avg >= 90:
#         grades.append("A")
#     elif avg >= 80:
#         grades.append("B")
#     elif avg >= 70:
#         grades.append("C")
#     else:
#         grades.append("D")

# print("Highest Average:", max(averages.values()))
# print("Random Student:", random.choice(list(students.keys())))
# print("Date:", date.today())
# print("Grades:", Counter(grades))





#Scenario 2 — Automated Course Project Team Allocation 

import sys
import random
import math
from collections import defaultdict
from itertools import combinations
from functools import reduce
from datetime import datetime

students = [
    ("Anita", "CSE", 85),
    ("Rahul", "CSE", 78),
    ("Priya", "CSE", 92),
    ("Kiran", "CSE", 88),
    ("Arun", "AI", 81),
    ("Meena", "AI", 90),
    ("Ravi", "AI", 75),
    ("Sneha", "AI", 86),
    ("Varun", "Data Science", 89),
    ("Divya", "Data Science", 94),
    ("Ajay", "Data Science", 82),
    ("Neha", "Cyber Security", 87)
]

if len(sys.argv) != 2:
    print("Usage: python allocation.py <team_size>")
    sys.exit()

team_size = int(sys.argv[1])

groups = defaultdict(list)

for student in students:
    groups[student[1]].append(student)

department = "CSE"
department_students = groups[department]

if team_size > len(department_students):
    print("Team size is greater than available students.")
    sys.exit()

possible_teams = list(combinations(department_students, team_size))

selected_team = random.sample(possible_teams, 1)[0]

marks = [student[2] for student in selected_team]

total_marks = reduce(lambda x, y: x + y, marks)

average_marks = total_marks / len(selected_team)

average_marks = math.floor(average_marks * 100) / 100

allocation_date = datetime.now().strftime("%d-%m-%Y")

print("===== PROJECT TEAM ALLOCATION =====")
print("Team Size:", team_size)
print("Allocation Date:", allocation_date)
print("Department:", department)
print("Selected Team:")

for i, student in enumerate(selected_team, 1):
    print(i, ".", student[0], "-", student[2])

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)