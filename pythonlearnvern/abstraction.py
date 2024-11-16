# What is Abstraction?
# A class that consist of one or more abstract method is called the abstract class.
# Abstract method can be inherited by the subclass and abstract method gets its defination in the subclass.

# How to create Abstract Method and class?
# there is one abstract class with one abstract method:
# # Abstract class
# class abstractclasss:
#     # Abstract method
#     def abstractmethod(self):
#         pass
    
# Practical
# e.g RBI
# # Abstract class
# class RBI:
#     # abstract method
#     def interest(self):
#         pass

# # Child class
# class SBI(RBI):
#     # RBI interest Implements here.
#     def interest(self):
#         print("SBI Interest is 5%")

# # Child class
# class HDFC(RBI):
#     # RBI interest Implements here.
#     def interest(self):
#         print("HDFC Interest is 2%")

# # Creating object of SBI
# s=SBI() 
    
# # Creating object of HDFC
# h=HDFC()

# s.interest()
# # SBI interest method called
# h.interest()
# # HDFC interest method called

# # Abstract Class/Parent class
# class Animal:
#     # Abstract method
#     def move(self):
#         pass

# # Child class
# class Dog(Animal):
#     # Class animal implements methods here
#     def move(self):
#         print("I can bark")

# # Child Class
# class Snake(Animal):
#         # Class animal implements methods here
#     def move(self):
#         print("I can hisss")

# # Creating object of Class Dog
# d=Dog()
        
# # Creating object of Class Snake
# s=Snake()

# d.move()
# s.move()