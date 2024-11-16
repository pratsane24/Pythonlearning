# What is list?
# List is Collection in python, Which store the data into sequence.
# list store multiple datatype value like string, int, float, character.
# list works on Index Value which start from zero(0).
# List is mutable(Changable at runtime) data structure.

# What can be done with list?
# Create list
# Indexing and slicing
# Apply built-In methods
# Nested List

# Creating a list
# This list stores the integer value
# l1 = [1,2,3,4,5,6]
# This list stores the string value
# l2 = ["Apple","Mango","Orange"]
# print("Interger List: ",l1)
# print("String List: ",l2)

# Duplicate Values in List
# l1=[1,2,3,4,5,6,1,2,3]
# print("Duplicate Value : ",l1)
# It will print duplicate value also.List doesn't have anything to do with repeated values. It will print as it is.

# List Constructor
# l1 = list(("Apple","Mango","Orange"))
# Note:- Here we are using double brackets (()).
# print(l1)
# Output will be in [] brackets.

# # List Slicing.
# l1= [1,2,3,4,5,6,7,8,9,10]
# print("Current list : ",l1)
# # Access the value of Index 1
# print("Index 1 Value : ",l1[1])
# # Access the value between 1 to 6
# print("Index between 1 to 6 :",l1[1:6])
# # Access the value till 6
# print("Index value till 6 : ",l1[:6])
# # Access the last value
# print("Last value : ",l1[-1])

# List Item Change
# x = ["Apple","Banana","Cherry","Mango","Orange","Kiwi"]
# print("Current list:", x)
# Change the item in list
# x[1:3]=["Grapes","Watermelon"]
# print("updated list:",x)
# Insert into list
# l1 = [1,2,3,4,5,6]
# print("Current list:",l1)
# l1.insert(2,"python")
# In this 2 is index value, and python is value which will be added to that index value.
# print("Updated list:",l1)

# Extend the list
# l1 = [1,2,3,4,5]
# l2 = ['A','B,','C','D','E']
# extending the list of l2 into list l1.
# l1.extend(l2)
# print(l1)

# Remove items from list
# 1. remove()
# This method is used to remove element from list.
# l1=[1,2,3,4,5,6,7]
# print("Current list:",l1)
# Removing the item using remove method.
# l1.remove(3)
# print("Updated list: ",l1)

# 2.pop()
# This method is use to remove last value from list.
# l1=[1,2,3,4,5,6,7]
# print("Current list:",l1)
# # remove item using pop method
# l1.pop()
# print("Updated list:",l1)

# 3.del() method
# this method is used to remove items from the index
# l1=[1,2,3,4,5,6,7]
# print("Current list:",l1)
# remove item using del method
# del l1[2]
# print("Updated list:",l1)

# 4. Clear()method
# THis method is used to clear the list
# l1=[1,2,3,4,5,6,7]
# print("Current list:",l1)
# remove item using clear method
# l1.clear()
# print("Updated list:",l1)