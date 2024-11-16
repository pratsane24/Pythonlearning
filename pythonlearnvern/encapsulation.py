# What is Encapsulation?
# The process of wrapping up variables and methods into a single entity is known as Encapsulation.

# Hoew to achieve Encapsulation?
#  _(single underscore) == Single Underscore stands for protected.
#  __(Double underscore) == Double Underscore stands for private.

# Achieving Encapsulationby private
# Parent class
# class A:
#     def __init__(self,a):
#         self.__a=a
#         # the variable is a private variable

#         def show(self):
#             # Printing a private variable using function.
#             print("Private variable :",self.__a)

# # Child class
# class B:
#     def __init__(self,b):
#         # Super method under overriding
#         super.__init__(b)

#     def showB(self):
#         print(self.__a)

# # Creating an object of class B
# obj = B(20)
# obj.showB()
# NOTE:- here error will occur,we cannot access "a" in any other class, since it is private.
# We cannot access parents class property with child class.


# Achieving Encapsulation by protected.

# # Parent class
# class A:
#     def __init__(self,a):
#         # THis variable a is a protected vaariable
#         self._a=a
    
#     def show(self):
#         print("Protected Variable:",self._a)

# # Child class
# class B(A):
#     def __init__(self,b):
#         super().__init__(b)

#     def showB(self):
#         print("Variable Value:",self._a)

# # Creating an object of class B
# obj = B(30)
# obj.showB()