# Exceptions are errors detected at the time of program execution.
# e.g Clear Road = Executing program without any exception.
# Accident = Exception
# Detour = Handling exception.
# E.g of exceptions:-
# 1/0
# TypeError :-ZeroDivisionError: division by zero
# print('abc'+2)
# TypeError:- can only concatenate str (not "int") to str

# Question:-write a program, & show how to escape exceptions.
# x=input("Enter number1: ")
# y=input("Enter number2: ")
# try:
#     z=int(x)/int(y)

# except Exception as e:
#     print('exception occured: ',e)
#     z=None 

# print("Division is: ", z)


# Another method

# x=input("Enter number1: ")
# y=input("Enter number2: ")
# try:
#     z=int(x)/int(y)

# except ZeroDivisionError as e:
#     print('Division by zero exception')
#     z=None 
# except TypeError as e:
#     print('exception type:',type(e).__name__)
#     z=None
# print("Division is: ", z)

# If you divide any no by 0 then the output gives error but if you divide 0 by any no then output occurs as 0.0

# If you enter any 1 value as 0, then the program stops there itself in the middle(on that line where error occur), it doesn't excecute ahead.

# If you try this for accident e.g

# try:
#     while road_is_clear():
#         drive()
# except Accident as e:
#     take_detour()

# Google"python builtin exceptions" to see list of standard exceptions in python.

