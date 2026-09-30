# # decorator
# def casechange():
#     def innerfun():
#         return function().upper()
#     return innerfun

# @casechange
# def message():
#     return "hello world"
# print(message())


# # A function can be assigned to a variable and called using that variable
# def greet():
#     print("Hello")
# message=greet
# message()


# #passing a function as an argument to another function
# def greet():
#     print("Hello")
# def execute(func):
#     func()
    
# execute(greet)



# def outer(name):
#     def inner():
#         print("Hello", name)
#     inner()
# outer("Tarun")


def makemultiplier(x):
    def multiplier(n):
        return x * n
    return multiplier
double = makemultiplier(2)
triple = makemultiplier(3)
print("Double:",double)
print("triple:",triple)