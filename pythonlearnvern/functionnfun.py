# What is function?
# Function is a block of code which only runs when is called.
# function is also used for reusability of code.
# Function is start with "def" keyword.

# types of functions
# 1.Built-in Function
# 2.User-define function
# 3.Anonymous function

# In-built function
# Are those functions which are in-built in python.
# print()
# range()
# len()
# round()
# max()
# min()

# User define function
# Creating a function:
# def function():
#       function body

#Calling a function
# function()

# What can be done?
# Creating a Function
# Calling a function
# Function with one Argument
# Function with multiple Argument
# Anonymous Function(Lambda function)
 

# In-Built function
# # print()function
# print("Hello world")

# # range()function
# for i in range(1,9):
#     print(i)

# # round() function
# x=round(53.2451,2)
# print(x)

# User Defined function
# Create function

# def myfunction():
#     print("hello")
# # Here u won't get the output since u haven't the function.
# # calling a function
# myfunction()

# Function with one argument
# # creating a function
# def myfunction(a):
#     print("A: ",a)
# # calling a function
# myfunction(10)
# # passing argument as a 10

# How to pass multiple argument
# # Creating a function
# def myfunction(a,b):
#     print("A :",a)
#     print("B :",b)

# # Calling a function
# myfunction(10,20)
# Passing 2 arguments

# Keywords Argument
# Creating a function
# def myfunction(child3,child2,child1):
#     print("Youngest Child is: "+child3)

# # Calling a function
# myfunction(child1="Ritesh",child2="Ram",child3="Geeta")

# Default Parameter Value
# Creating a function
# def myfunction(state="Gujarat"):
#     print("I m from :"+state)

# # Calling a function
# myfunction("Rajasthan")
# myfunction("Punjab")
# myfunction("Maharashtra")
# myfunction()
# # Output:
# I m from :Rajasthan
# I m from :Punjab
# I m from :Maharashtra
# I m from :Gujarat
# In this where fun() is empty it take default value.

# Passing a list into function
# Creating a function
# def myfunction(fruit):
#     for i in fruit:
#         print(i)
# f=["Apple","Mango","Orange"]
# # Calling a function
# myfunction(f)

# Return value from Function
# Creating a function
# def myfunction(x):
#     return 5*x
# # Calling a function
# print(myfunction(3))
# print(myfunction(4))
# print(myfunction(5))

# # Recursion function
# # Creating a functon

# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return(x*factorial(x-1))
#     # Calling recursion function
# num = int(input("Num :"))
# print("The factorial of ",num,"is: ",factorial(num))

# Anonymous Function (Lambda function)
# Creating a function
# one line function.

# x = lambda a: a+10
# print(x(5))

# # Lambda function with multiple Arguments
# y=lambda a,b:a*b
# print(y(5,10))

# Global Variable
# Global variable means the variable can be used anywhere in the program
# z=25
# # here z is Global variable
# def myfunction():
#     global z
#     print(z)
#     z=20
# myfunction()
# print(z)
# # Global variable can be used anywhere in the function.

# Local Variable
# The variable which can be used in it's scope.
# It can be used only in that function,not outside of function.

# def sum(x,y):
#     sum = x+y
#     return sum
# print(sum(5,10))

# # print(x)
# Here u will get error,since x is local variable

