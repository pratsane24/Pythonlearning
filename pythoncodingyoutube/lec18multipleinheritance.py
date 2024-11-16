# class Father():
#     def gardening(self):
#         print("I enjoy gardening")

# class Mother():
#     def cooking(self):
#         print("I love cooking")

# class Child(Father,Mother):
#     def sports(self):
#         print("I enjoy sports")

# c = Child()
# c.gardening()
# c.cooking()
# c.sports()


# Father & Mother are base class 
# Child is Derived class from base class (Father & Mother)
# Benifits of multiple inheritance is sometimes you have two different classes and you just want to inherit the propertiesand methods
# of those classes just to reuse the code and then you want to add your own customization.
# In a single method you can call the base class matter.

# Question:- If father & Mother has multiple skills
# there is another alternate method.
# If you have same subclass as skills, then it should take all the values in account.

class Father():
    def skills(self):
        print("gardening,programming")

class Mother():
    def skills(self):
        print("arts,cooking")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")

c = Child()
c.skills()






