import cal


def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


a = read_number("Enter first number: ")
b = read_number("Enter second number: ")

print("Addition:", cal.add(a, b))
print("Subtraction:", cal.subtract(a, b))
print("Multiplication:", cal.multiply(a, b))
print("Division:", cal.divide(a, b))
print("Power:", cal.power(a, b))
print("Square root of first number:", cal.square_root(a))
