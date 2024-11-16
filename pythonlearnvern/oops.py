#  ORIENTED LANGUAGE (OOPs)

# OOPs Concept
# 1.Class
# 2.Objects
# 3.Inheritance
# 4.Polymorphism
# 5.Abstraction
# 6.Encapsulation

# Ur languages such as java,.net,python,php etc all work on this 6 pron principle.

# 1.What is Class?
# Python classes provide all the standard features of Object Oriented Programming:the Class iheritance mechanism
# allows multiple base classes, a derived class can override any methods of its base or classes, and a method can 
# call method of a base class with the same name.

# # How to create a class in python?
# class classname:
#     class body


# 2.What is object?
# Class objects support two kinds of operations: attribute references and installation.
# Attribute references use the standard syntax used for alll attribute references in Python:obj.name.

# What is costructor?
# Constructor means it's a special member function which calls whenever object create of that class.
# Construction is identify by (_) underscore.
#_init_function : This function is called constructor in python and is call whenever the object is create of that class. 

# How to create constructor in python?
# def _init_(self):
#     constructor body

# How to create a call?
# class myclass:
#     x=5 
#     # property of class
# print(myclass)



# How to create object?
# class myclass:
#     x=5 
    # property of class

# Creating object of my class
# m1 = myclass()
# # m1 is an object of class myclass
# print(m1.x)

# NOTE:- without object you cannot access class property.

# Call a function by object?
# class myclass:
#     def myfunction(self):
#         #   # property of myclass
#         print("Hello myfunction")
# # Creating an object
# m1 =myclass()
# m1.myfunction()

# How to create a constructor?
# class myclass:
#     # Creating a constructor
#     def __init__(self):
#         print("This is my constructor")

# # Creating an object
# m1 = myclass()


# Change value by objects
# class myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age = age
#     def myfunction(self):
#         print("My name is :"+self.name)

# # Creating an object
# m1 = myclass("Sunit",25)
# m1.age
# m1.name
# # Changing age using object
# m1.age = 26
# print("Age:",m1.age)

# # delete object
# del m1.age
# print("Age:",m1.age)
  
    

