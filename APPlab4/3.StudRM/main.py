try:
    from .student_res import cal_total, cal_percentage, cal_grade
except ImportError:
    from student_res import cal_total, cal_percentage, cal_grade


def get_marks():
    """Read a valid number of subject marks from the user."""
    while True:
        try:
            n = int(input("Enter the number of subjects: "))
            if n <= 0:
                print("Please enter at least 1 subject.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")

    marks = []

    for i in range(n):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i + 1}: "))
                if not 0 <= mark <= 100:
                    print("Marks must be between 0 and 100.")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Please enter a valid number.")

    return marks


marks = get_marks()

total = cal_total(marks)
percentage = cal_percentage(marks)
grade = cal_grade(percentage)

print(f"Total marks: {total:g}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
