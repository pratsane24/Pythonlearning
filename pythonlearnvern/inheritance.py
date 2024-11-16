# What is inheritance?
# Python supports inheritance, it even supports multiple inheritance.
# Classes can inherit from other classes.
# A class can inherit attributrs and behavior methods from another class,called the superclass.
# A class which inherits from a superclass is called a subclass, also called heir class or child class.

# This are also known as
# 1.Super class & base class
# 2.parent class & child class
# 3.Derived class & base class.

# inherit means taking a properties of another class into a another class.

# Type of inheritance
# 1.Single Inheritance
# 2.Multilevel inheritance
# 3.Multipe inheritance
# 4.Hiererchical Inheritance
# 5.Hybrid Inheritance

# # What is single Inheritance?
# # In single inheritance there is only one parent class & one child class.
# # In single inheritance only one parent class is inherit into one child class.

# # Practice Single inheritance.
# # Parent class
# class parentclass:
#     # Parent Class Property
#     def myfunction1(self):
#         print("Parent Class Function Called")

# # Child Class which inherit parent class
# class childclass(parentclass):
#     # Child class property
#     def myfunction2(self):
#         print("Child Class Function Called")
#         # Creating an object of childclass

# c1=childclass()
# c1.myfunction1()
# c1.myfunction2()

# What is multilevel Inheritance?
# In multilevel inheritance there are levels of class.

# Practice Multilevel Inheritance

# # Parent class
# class A:
#     def myfunction1(self):
#         print("Class A function called")
    
# # Sub-parent Class
# class B(A):
#     def myfunction2(self):
#         print("Class B function called")

# # Child Class
# class C(B):
#     def myfunction3(self):
#         print("Class C function called")


# # Creating an object of class C
# c1 = C()
# c1.myfunction1()
# c1.myfunction2()
# c1.myfunction3()

# What is Multiple Inheritance?
# When A child class inherits from multiple parent classes, it is called multiple inheritance.

# # Practical pf multiple Inheritance

# # 1st Parent class
# class A1:
#     def myfunction1(self):
#         print("Class A1 function called")

# # 2nd parent class
# class B1:
#     def myfunction2(self):
#         print("Class B1 function called")

# # Child Class
# class C1(A1,B1):
#      def myfunction3(self):
#         print("Class C1 function called")

# # Creating an object of class C1
# c1 = C1()
# c1.myfunction1()
# c1.myfunction2()
# c1.myfunction3()


# What is hierarchical Inheritance?
# When more than one child class is created from a sinlg parent class is called Hierarchical Inheritance.

# # Practical hierarchical Inheritance

# # Parent class
# class A1:
#     def myfunction1(self):
#         print("Class A1 function called")

# # 1st Child class
# class A2(A1):
#      def myfunction2(self):
#         print("Class A2 function called")

# # 2nd child class
# class A3(A1):
#      def myfunction3(self):
#         print("Class A3 function called")

# # Cretaing 2 objects,1 for A2 & 1 for A2.
# a2 = A2()
# a3 = A3()

# # Function of class A1
# a2.myfunction1()
# # Function of class A2
# a2.myfunction2()


# # Function of class A1
# a3.myfunction1()
# # Function of class A3
# a3.myfunction3()


# What is Hybrid Inheritance?
# THis form combines more than one form of inheritance.
# Basically, it is a blend of more than one type of inheritance.

# Practical Hybrid Inheritance

# # Parent class
# class B1:
#     def myfunction1(self):
#         print("Functon of class B1")


# #1st  Child Class
# class B2(B1):
#     def myfunction2(self):
#         print("Functon of class B2")

# # 2nd  Child Class
# class B3(B1):
#     def myfunction3(self):
#         print("Functon of class B3")


# # 3rd  Child Class
# class B4(B2,B3):
#     def myfunction4(self):
#         print("Functon of class B4")

# # Creating an object of class B4
# b= B4()
# b.myfunction1()
# b.myfunction2()
# b.myfunction3()
# b.myfunction4()

