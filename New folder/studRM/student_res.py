def cal_total(marks):
    """Return the total of all subject marks."""
    return sum(marks)


def cal_percentage(marks):
    """Return the average percentage, assuming each subject is out of 100."""
    if not marks:
        return 0.0

    return cal_total(marks) / len(marks)


def cal_grade(percentage):
    """Return a grade based on the percentage."""
    if percentage >= 90:
        return "O"
    elif percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    else:
        return "F"
