# Variables
# Variables are names given to store some values
# It can store integers,float,string,boolean set, tuple,list & dictionary.

# Rules of Variables:
# Variable should start with Alphabet only
# variable name should not have whitespaces(abc should be name not a b c).
# We cannot use datatype names as a variable name
# Variable name are significant.


#Assign Multiple Variables
# Python allows multiple variable at a time.
# E.g:
# x,y,z="Orange","Mango","Banana"

# Concat Variables
# Python allows you to concat the variables using "+" sign.
# E.g:
# x="python"
# y="programming"
# z=x+y
# print(z)

# Print Variables
# Get input from user
# Users of print function

# How to create a variable?
# interger value to the variable
# a=10
# print(a)
# print(type(a))

# # float value to the variable
# b=10.5
# print(b)
# print(type(b))

# # String value to the variable
# c="python"
# print(c)
# print(type(c))

# # We ca store list in a variable
# l1=[1,2,3,4,5,6]
# print(l1)
# print(type(l1))

# # We can Store Tuple in a variable
# t1=(1,2,3,4,5)
# print(t1)
# print(type(t1))

# # Note:- You must know the rules of variable, with whom you are working.

# Type conversion
# Converting from one datat type to another data type is called type conversion, it is also known as type casting.
# E.g :-Consider we need a interger value & that from user
# a=input("Enter the value of A: ")
# print("A: ",a)
# print(type(a))

# Output is giving data type as string if we 
# Enter the value of A: 25
# A:  25
# <class 'str'>

# Now we need to do type conversion bze the type sholud depend upon my input.
# So now use this method
# E.g
# b=int(input("Enter the value of B: "))
# print("B: ",b)
# print(type(b))

# Output
# Enter the value of B: 12
# B:  12
# <class 'int'>

# Note:- But now if you enter string in value of B then error will occur since you have used int.
# String data type that can't convert but we can use any data type in string.
# E.g:-
# Enter the value of B: python
# Traceback (most recent call last):
#   File "d:\pythonlearnvern\variables.py", line 71, in <module>
#     b=int(input("Enter the value of B: "))
# ValueError: invalid literal for int() with base 10: 'python'
