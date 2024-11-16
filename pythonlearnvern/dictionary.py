# What is dictionary?
# dictionary is a collection of python, which works on key and value pair.
# Dictionary follows the ordered container or collection.
# Dictionary has immutable key and value could be immutable and mutable both which depends upon what value you are storing.

# What can be done with dictionary?
# 1.Create dictionary
# 2.Indexing/Slicing
# Dictionary Method


# # Creating Dictionary
# d1={1:"Apple",2:"Mango",3:"Orange",4:"Apple","A":"B"}
# print(d1)
# NOTE: In this 1,2,....are key & Apple,Mango..etc are values

# Datatype of dicitonary
# print(type(d1))

# List into Dicitonary Store
# Storing a list into a dictionary on single key.
# NOTE: use list or tuple to store multiple values on a single key.
# d2={1:"Python",2:"Java","Fruit":["Apple","Mango","Orange"]}
# print(d2)

# storing tuple into dictionary on a single key.
# d3={1:"Python",2:"Java","Language":("Java","Python","php")}
# print(d3)

# Access the value of Dictionary
# d1={1:"Apple",2:"Mango",3:"Orange",4:"Apple","A":"B"}
# print("Current Dict : ",d1)
# Access the value using key
# x = d1[3]
# print(x)

# Access the value by using get() method.
# y=d1.get(1)
# print(y)

# Access the value using item()
# z=d1.items()
# print(z)
# In output you will get dictionary into the form of tuple,Containing list with combination of keys and values.

# How to change the value in dictionary
# d1={1:"Apple",2:"Mango",3:"Orange",4:"Apple","A":"B"}
# d1[3]="kiwi"
# print("Updated Dict : ",d1)

# Updating dictionary By using update() method 
# print("Current Dict:",d1)
# d1.update({2:"Banana"})
# print("update Dict:",d1)

# How to remove values from dictionary
# Using pop() method
# NOTE:- pop() method is used to always remove the last value but in list not in dictionary.
# Here use should use pop() with key which you want to remove & popitem() to remove the last value.
# d1={1:"Apple",2:"Mango",3:"Orange",4:"Apple","A":"B"}
# print("Current Dict:",d1)
# d1.pop(2)
# print("Updated Dict:",d1)

# Using popitem()
# d1.popitem()
# print("Latest dict:",d1)

# Using del() method
# del d1[1]
# print("Updated dict:",d1)

# Using Clear() Method
# d1.clear()
# print("Updated dict :", d1)

# Ḥow to access particular key in dictionary
# k =d1.keys()
# print("Keys:",k)

# Ḥow to access particular values in dictionary
# v = d1.values()
# print("Values:",v)