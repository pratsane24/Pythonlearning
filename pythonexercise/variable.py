# Question :- Create a variable called break and assign it a value5. See what happens and find out the reason behind the behavior that you see?
# break=5
# print(break)

#  We cannot us break as a variable, Since break is a predefined function in python. 
# Therefore it is showing Syntax eror.


# Question:- Create two variables. one to store your birth year and another one to store current year. Now calculate your 
# age using these two variables.
# a=2003
# b=2024
# age=b-a
# print(age)


# a=input("enter a birth year: ")
# b=input("enter a current year: ")
# print(type(a))
# print(type(b))
# a=int(a)
# b=int(b)
# age=b-a
# print(age)
# print(type(a))
# print(type(b))


# TypeError: unsupported operand type(s) for -: 'str' and 'str'
# NOte:- We cannot sub str from str.so we were getting error. 
# Do check by using print(type()) for type we used.
# Question: Store your first, middle & last name in 3 different variables & then print your full name using these variables?
# first= "Dhawal"
# middle="Rambhai"
# surname="Patel"
# a=first+" "+middle+ " " +surname
# print("My full name is:", a )

# Another Method

first= input("please enter your first name: ")
middle=input("please enter your middle name: ")
surname=input("please enter your surname: ")
a=first+' '+middle+' '+surname
print("My full name is:", a )

# ""- string (str)
# ''-used for character(char)





































# First name=input("please enter your first name")