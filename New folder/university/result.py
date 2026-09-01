def calculate_percentage(marks):
    """Return the average percentage for marks out of 100."""
    if not marks:
        return 0.0

    return sum(marks) / len(marks)
