# What is polymorphism?
# Polymorphism means having many form of same name.
# In programming polymorphism means function having same name but different signature.

# Type of polymorphism
# There are 2 types of Polymorphism
# 1. Complile Time Polymorphism
# a) Method Overloading

# 2. Runtime Polymorphism
# a) Method Overriding

# What is Method Overloading?
# Method overloading is the compile time polymorphism.
# Method Overloading means having same name methods in same class,but different arguments.
# In method overloading inheritance is not required.

# Practical

# Method Overloading
 
# class mo:
#     def myfunction(self):
#         print("Function with no arguments")

#     def myfunction(self,a):
#         print("Function with 1 argument")

#     def myfunction(self,a,b):
#         print("Function with 2 arguments")

# # Creating an object of class mo
# m= mo()
# m.myfunction(10,20)

# NOTE :- Method Overloading is not supported in python bze python is interpreted language.

# What is method overriding?
# Method overriding is the runtime polymorphism.
# MEthod overriding means having same name methods, but into different class, argumenta are also same.
# In method overriding inheritance is compulsory.

# Practical

# Method overriding  

# # # Parent class
# class mo1:
#     def myfunction(self,a):
#         print("Class MO1 function called")

# # # Child class
# class mo2(mo1):
#     def myfunction(self,a):
#         print("Class MO2 function called")
# # Super MEthod calling the method of class mo1
#         super().myfunction(10)

# # # Child Class
# class mo3(mo2):
#     def myfunction(self,a):
#         print("Class MO3 function called")
# # Super MEthod calling the method of class mo2
#         super().myfunction(10)


# # Creating Object of class mo3

# # object of mo3
# m = mo3()
# m.myfunction(10)








