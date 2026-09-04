from employee import calculate_salary
from employee import calculate_bonus
from employee import employee_details

salary = calculate_salary(50000, 10000)
bonus = calculate_bonus(salary, 6)

employee_details("Anand", "IT", salary, 6)

print("Bonus:", bonus)
