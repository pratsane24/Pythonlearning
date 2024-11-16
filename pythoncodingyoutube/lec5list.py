item1="bread"
item2="pasta"
item3="fruits"
item4="vegetables"
# items=[item1,item2,item3,item4]
# Note:- just did the above function for trial.
items=["bread","pasta","fruits","vegetable"]
print(items)
# Note:-So we create the list of various data by using "" with a square bracket[]. 
# Note:-You can't replace a letter in a string. Convert the string to a list, replace the letter, and convert it back to a string.


# print(items[0])
# items[0]="chips"
# print(items)

# Note:- Eg to convert list into string.
# s = "Chips"
# x = list(s)
# print(x)
# print(x[0])
# x[0]="c"
# print(x)


# print(items[0:2])
# Note:-[-1] in index means 1st but from last or end of the list.
# print(items[-1])

# Note:- We have some predefined words in python:- 1. append: it is used to add a new word in list but at the end of the list. syntax is .append("word to be inserted")
# 2.insert: it is use to add item or word in the list but at the location where you want to add that word in given syntax .insert(location of index,"word to be added")

# print(items.append("butter"))
# print(items.insert(1,"butter"))

# Note:- if you have 2 more list to be added or merged to together to create one follow this syntax
food=["bread","pasta","fruits","vegetable"]
bathroom =["soap","shampoo"]
items=(food+bathroom)
print(items)

# print(food+bathroom)
# Note:- above format is just a alternative method.



# Note:- to calculate the length of items means total no of items in a list we use len predefined syntax for length in python.
print(len(items))

# Note:- if you want to find any item from the list if is there or not then follow the following method.

print("bread" in items)
print("tooth brush" in items)
