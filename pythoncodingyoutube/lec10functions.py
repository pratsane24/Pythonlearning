# Function is a block of code that performs a specific task.
# functions make the code more modular & more readable.


# Question:- You are given two lists of nos & you need to find total of each of these list.

# Traditional Method:-

# tom_exp_list = [2100,3400,3500]
# joe_exp_list = [200,500,700]

# total=0
# for item in tom_exp_list:
#     total=total+item
# print("Tom's total expenses:",total)

# total=0
# for item in joe_exp_list:
#     total=total+item
# print("Joe's total expenses:",total)

# IF there are 100 or more such list to be calculated, then it will be very diificult or hectic to type code for all list 
# so we can use function to write a single code for 100 of list togrther.
# def calculate_total(exp):- In this (exp) means function arguments
# return total :- In this return is return Value.
# & from def to last return value is known as fuction Body.


# def calculate_total(exp):
#     total=0
#     for item in exp:
#         total=total+item
#     return total
    
# tom_exp_list = [2100,3400,3500]
# joe_exp_list = [200,500,700] 

# toms_total=calculate_total(tom_exp_list)
# joes_total=calculate_total(joe_exp_list)

# print("Tom's total expenses:",toms_total)
# print("Joe's total expenses:",joes_total)
    

# Question:- You want sum of 2 no. using a function
# def sum(a,b):
#     total=a+b
#     return total

# n=sum(5,6)
# print("Total:",n)


# Steps Into(F7) takes the debug control inside the function.
def sum(a,b):
    print("a:",a)
    print("b:",b)
    total=a+b
    print(" Total inside function:",total)
    return total


n=sum(5,6)
print("Total outside function:",n)

# Arguments are of two type,
# 1. Positional Arguments
# 2. Named Arguments


# Local v/s Global Variable.
# any variable which is outside function is global variable whereas any variable created inside Function is called local variable. 
# Default Arugument
# If sometimes value for any variable is missing to run a fun or code, it will show Error, then some times you asign a specific
# value like a=0, then it will take it as a default value & code will run.
# Document Strings
# If you have any long function & you need to make notes there for explaining the input/output etc, you need to use triple coates
# """to write a note""" in pycharm or directly comment it by ctrl / i.e ? mark in VSC.
