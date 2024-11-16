# What is exceptional handling?
# How to use exceptonal handling?

# What is exceptional handling?
# Exception means the abnormal situation occurs at runtime and stop the execution of program is called exception.
# In python two types of Error:
# 1.Syntax Error
# 2.Exception

# 1.Syntax error
# As the name suggest this error is caused by wrong syntax in the code.It leads to the termination of the program.


# Exceptions are raised when the program is syntactically correct but the code resulted in an error. This error does not stop
# the execution of the program, however,it changes the normal flow of the program.

# User define exception
# User define exception means user can generate his custom exception in python by inherited the exception class.

# Exception create
# a= int(input("Enter the value of A :"))
# print("A :",a)

# # OUTPUT:
# # In first output we entered no,and got correct output
# # But in second we got error as we entered string in place of integer.
# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/exceptionhandling.py
# Enter the value of A :10
# A : 10
# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/exceptionhandling.py
# Enter the value of A :python
# Traceback (most recent call last):
#   File "d:\PYTHON\pythonlearnvern\exceptionhandling.py", line 21, in <module>
#     a= int(input("Enter the value of A :"))
# ValueError: invalid literal for int() with base 10: 'python'

# Another e.g
# a = int(input("Enter the value of A :"))
# b = int(input("Enter the value of B :"))
# c = a/b
# print("Answer: ",c)
# print("Bye")

# NOTE:- here exception occurs on runtime bze division by zero.
# OUTPUT:-
# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/exceptionhandling.py
# Enter the value of A :10
# Enter the value of B :0
# Traceback (most recent call last):
#   File "d:\PYTHON\pythonlearnvern\exceptionhandling.py", line 40, in <module>
#     c = a/b
# ZeroDivisionError: division by zero

# SOLUTION FOR THIS ERROR:- try and except
# try:
#     # the code which is written in try block can be occur error at run time.
#     a = int(input("Enter the value of A :"))
#     b = int(input("Enter the value of B :"))
#     c = a/b
#     print("Answer: ",c)
# except Exception as e:
#     # This block will run when exception occur
#     print("Exception Caught:",e)

# print("Bye")

# OUTPUT:-
# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/exceptionhandling.py
# Enter the value of A :20
# Enter the value of B :0
# Exception Caught: division by zero
# Bye
# NOTE:- In this error occured but our application didn't stop, it run till bye.

# Consider you need to handle many exceptions
# try:
#     # In this, we have not definee variable x
#     print(x)
# except NameError:
#     print("Variableis not defined")
# except:
#     print("Exception Caught")
# print("Bye")

# How to use exception with else part?
# try:
#     print("Hello")
# except:
#     print("something went wrong")
# else:
#     print("Nothing went wrong")

# Another eg with variable x
# try:
#     print(x)
# except:
#     print("something went wrong")
# else:
#     print("Nothing went wrong")

# Finally block
# the block which run compulsory if error occurs or not.
# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# finally:
#     print("Finally block")

# Another eg with different output
# try:
#     print(x)
# except:
#     print("Something went wrong")
# finally:
#     print("Finally block")

# User defined exception
# class myexception(Exception):
#     pass

# c=25
# if c>5:
#     raise myexception("Something went wrong")

