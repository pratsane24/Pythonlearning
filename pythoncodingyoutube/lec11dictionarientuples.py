# Dictionary is something that allows u to store key,value pairs.Also known as Maps, Hashtables, Associate arrays.
# Order in dictionaries doesn't matter.
# eg telephone directory.



# d={"tom":9874563210, "rob":7894561203,"joe":7410258963}
# print(d)


# When we write any comment in "" in print then it will print as it is, written in ("").The comment becomes string when written in "". 
# Whereas when we want to print the variable value we have to write it without"" in print. Variables are not written in "". 

# print(d["tom"])

# Question:- How to add a new telephone no in the dictionaries.
# d["sam"]=7412589036
# print(d)

# Question:- How to delete a telephone no in the dictionaries.
# del d["rob"]
# print (d)

# Question:- How to print all the directory values?
# for that u can use for loop.

# for key in d:
#     print("key:",key,"value:",d[key])

# Another method to the this through truples.

# for k,v in d.items():
#     print("key:",k,"value:",v)


# Question: How to check if there is any specific name or not?
# print("tom" in d)
# print("sam" in d)


# Question:-All the phone nos are getting changed n I want to trash all the entires from my telephone directory?
# d.clear()
# print()


# Tuples is a list of values grouped together.
# The difference betn list n tuples are:python
# list: All values have similar meaning(Homogeneous)
# Tuples: All values have different meaning(heterogeneous) 
# For eg. u want represent a geometric point in 2D plane how will u do that?
point=(5,9)
print(point[0])
# In this, this is a exam of tuple bze both the valuse have different meaning 5 is X-cordinate whereas 9 is Y-cordinate.

# List Eg. 
# expense_list=[2300,2500,2900,6700], every item is an expense.
# list_of_names=["bob","joe","tom"], every item is a name of a person.

# Tuple eg. 
# point=(4,5), 4 is x-cordinate while 5 is y-cordinate
# address=('1 purple street","new york", 10001), in this 1st is street name, 2nd is city name while 3rd is pin code.
# tuples are immutable 
