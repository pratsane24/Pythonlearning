# What are Operators?
# Operators are used to perform operations on variable and values in python.

# Types of Operators
# 1. Arithmetic operators
# 2.Assignment operators
# 3.Comparison operators
# 4.Logical operators
# 5.Identity operators
# 6.Membership operators

# Note:-
# 1. Arithmetic operators
# This is use to operations such as add,substract, etc

# 2.Assignment operators
# In this we assign value to a variable like short hand operators, like we use add the value & again stored in the same variable.

# 3.Comparison operators
# This operators are operator which helps use in decission making. This will give answer only in 2 ways either true or false.

# 4.Logical operators
# It is logical operation, like And, Or, Not. It gives true or false value after checking logical operation.

# 5.Identity operators
# It checks if your object is matching or not matching with the other. It will also give you only two answers i.e true or false.

# 6.Membership operators
# It helps to check the sequence, If there is a sequence and you want to check if this word is there in the sequence or not.

# Now let's start with practical e.g
# # 1.Arithmetic operators
# # i) Addtion operator
# x=10
# y=50
# z=x+y
# print("Answer:" ,z)

# # ii)Substraction operator
# a=10
# b=20
# c=a-b
# print("Answer:" ,c)

# # Multiplication
# x=10
# y=2
# z=x*y
# print("Answer:" ,z)

# NOTE:- Python works on the principle of step by step excutation,so it it take the 1st value till the new value is provided to it.

#2. Assignment Operator
# i) Equal to operator
# x=5
# print("X:",x)
# In this we have assign value 5 to x but using "=" sign.

# ii) Addition and equal to operators
# Let's say we have x = 5 and we want to add 5 & assign that value to x then we need to do this method.
# x=5
# x+=5
# Note :- There in line 62, x=x+5 will be the new value and it will be stored as 1st value or replce/update the 1st value.
# print("X : ", x)

# iii) Substration and equal to operators.
# x=6 
# x-=2
# x=x-2 i.e 6-2=4
# print("X : ", x)

#3. Comparison Operation
# i) Equal to-Equal to operator
# x=5
# y=3
# print(x==y)

# # another eg
# x=15/5
# y=3
# print(x==y)

# ii)Not equal to Operator
# x=5
# y=3
# print(x!=y)

# iii) Greater than equal to
# x=5
# y=3
# print(x>=y)

# iv) Less than equal to
# x=5
# y=3
# print(x<=y)

# 4. Logical Operators
# And Operator
# x=5
# print(x>3 and x<3)
# Answer is False, since condition  x>3 is satisfied, but x<3 is not satisfied so the answer is false.
# Both the condition is need to be satisfied, then only the answer will be true. 

# Or Operator
# x=5
# print(x>3 or x<3)
# Answer is True, since condition  x>3 is satisfied, but x<3 is not satisfied so the answer is True.
# In this if any 1 condition is satisfied then the answer will be true.

# 5. Identity Operators
# i) Is operator
# x=["Apple","Mango"]
# y=["Apple","Mango"]
# z=x
# print(z)
# Now we need to check x is y?
# print(x is y)
# Answer is false, since the values of x & y are matching(means the value present is bracket are same)
# but x is not equal to y (x object is not matching with y object).
# # Note:- We will get answer as true if we use is not in print. 
# print(x is z)
# There answer is True, Since we have given x=y as a condition so it's objects are matching.

# 6. Membership Operator
# i)In
# x=["Apple","Mango"]
# print("Banana" in x)
# Answer is false since banana is not present in list i.e x.

# ii) Not In
# x=["Apple","Mango"]
# print("Banana" not in x)
# Answer is true, since banana is not present in list i.e x.

# # Operator Precedence
# Which operator evaluates first can be confusing. So we have some rules for this too.This is the precedence table that 
# denotes which operator evaluates.
# list is in notebook.
# values flow from left to right.
# E.g
# value=(1+1)*2**4//3+4-1
# print(value)
# Answer=13
# E.g
# a=20
# b=10
# c=15
# d=5
# x=(a+b)*c/d
# print("Value of X: ",x)

# y=((a+b)*c)/d
# print("Value of y: ",y) 

# z=a+(b*c)/d
# print("Value of z: ",z) 

