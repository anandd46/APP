# Open the file in write mode.
# If the file does not exist, it will be created.
# If it exists, old data will be erased.
with open("std.txt", "w") as file:
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"\nEnter details of Student {i + 1}")
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        marks = input("Enter Marks: ")
        file.write(f"{roll},{name},{course},{marks}\n")

print("\nStudent records saved successfully!")
print("\n========== STUDENTS RECORD ==========")
with open("std.txt", "r") as file:
    for line in file:
        roll, name, course, marks = line.strip().split(",")
        print("\nRoll Num:", roll)
        print("Name:", name)
        print("Course:", course)
        print("Marks:", marks)


# SEARCH FOR A STUDENT
roll_search = input("\nEnter Roll Number to search: ")
with open("std.txt", "r") as file:
   for line in file:
        roll,name,course,marks=line.strip().split(",")
        if roll == roll_search:
            print("Student found")
            print("Roll Num:",roll)
            print("Name",name)
            print("Course",course)
            print("Marks:",marks)
            break
        else:
            print("Student not found")


# CREATE BACKUP OF STUDENT RECORDS
with open("std.txt", "r") as source:
    content = source.read()
with open("std_backup.txt", "w") as backup:
    backup.write(content)

print("\nBackup created successfully!")

# DELETE THE FILE
# import os
# delete_choice = input(
#     "\nDo you want to delete the student record file? (yes/no): "
# )
# if delete_choice.lower() == "yes":
#     if os.path.exists("std.txt"):
#         os.remove("std.txt")
#         print("Student record file deleted successfully!")
#     else:
#         print("Student record file does not exist.")
# else:
#     print("Student record file was not deleted.")




-------------------------------------output------------------------------------------
# Enter number of students: 3

# Enter details of Student 1
# Enter Roll Number: 01
# Enter Name: A
# Enter Course: dsa
# Enter Marks: 90

# Enter details of Student 2
# Enter Roll Number: 02
# Enter Name: b
# Enter Course: c
# Enter Marks: 98

# Enter details of Student 3
# Enter Roll Number: 3
# Enter Name: c
# Enter Course: cs
# Enter Marks: 78

# Student records saved successfully!

# ========== STUDENTS RECORD ==========

Roll Num: 01
Name: A
Course: dsa
Marks: 90

Roll Num: 02
Name: b
Course: c
Marks: 98

Roll Num: 3
Name: c
Course: cs
Marks: 78

Enter Roll Number to search: 3
Student not found
Student not found
Student found
Roll Num: 3
Name c
Course cs
Marks: 78

Backup created successfully!