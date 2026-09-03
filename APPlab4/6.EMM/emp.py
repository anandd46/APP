
def calculate_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_bonus(salary, experience):
    if experience >= 5:
        return salary * 0.10
    else:
        return salary * 0.05


def employee_details(name, department, salary, experience):
    print("Employee Details")
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)
    print("Experience:", experience)
