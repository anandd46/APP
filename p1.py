age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")

marks=int(input("Enter your marks: "))
if marks>=50:
    print("You have passed the exam.")
else:
    print("You have failed the exam.")

salary1=int(input("Enter your salary: "))
salary2=int(input("Enter your salary: "))
highest_salary=salary1 if salary1>salary2 else salary2
print("The highest salary is:", highest_salary)

#conditions
amount =float(input("Enter purchase amount: "))
discount=amount*0.1 if amount>1000 else 0
print("Discount amount:", discount)
print("Final amount to be paid:", amount-discount)

age=25
is_stdnt=False
dscnt_code=True
if(age<18 or age >65) and not is_stdnt and dscnt_code:
    print("Discount applicable")

temperature=25
is_raining=False
is_weekend=True
if temperature>20 and not is_raining and is_weekend:
    print("Great day for outdoor activities.")