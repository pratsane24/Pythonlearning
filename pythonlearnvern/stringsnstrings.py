# what is string?
# String in python are surrounded by either single quotation marks or double quoation marks.
# String is the collection of character.
# String allows any datatype value to be stored - chr(),double(),float().

# What can be done with String.
# Create String
# Indexing and slicing
# Apply built-in methods


#  How to use string in python?
# 1. Single quote in string
# print('Hello World')
# It is giving output in single quote, this is only possible in python.

# 2. Double Quote in string
# print("Hello World")
# It is also giving output.

# 3.Multi-line String - We need to work with """ 
# a = """Python is booming in the market,
# Python is smart language,
# Python is used in AI, Machine learning,Data science"""
# print(a)

# How we can update a string?
# a= "Hello World!"
# print(a)
# Now we want print python inplace of world.
# print("Updatd String :",a[:6]+"Python")

# String Slicing - It is also known as string using array.
# a="Hello Python"
# Access the value of Index 1
# print("Index 1 : ",a[1])
# Access the value between Index 1 to 6
# print("Index between 1 to 6 : ",a[1:6])
# Access the value of Index till 6
# print("Index value till 6 : ",a[:6])
# Access the last value from string
# print("Last value : ",a[-1])

# String In-built Methods.
# 1. Capitalize() :- This method converts the first character in string into capital letter.
# a= "hello and welcome to learnvern"
# x=a.capitalize()
# print(x)

# 2. Casefold() :- This method converts all capital letter in small letter.
# a= "Hello and Welcome to Learnvern"
# x=a.casefold()
# print(x)

# 3.Center() :- This is use to bring your string into center.
# a="python"
# print(a)
# x=a.center(20)
# updated using center method.It left 20 space and then printed python. 
# print(x)

# 4.Count() :- This method is used to count the repeated word in string.
# a=" I love Python, Python is a smart language"
# x=a.count("Python")
# print(x)

# How to compare a string.
# str1="Learnvern"
# str2="Learnvern"
# result = str1==str2
# print(result)
# Answer is :- True, Since str1 and Str2 have same words with same cases.

# str1="Learnvern"
# str2="Python"
# result = str1==str2
# print(result)
# Answer is :- False, since the words are different.

# Str1 = 'A'
# str2 = 'B'
# result = Str1<str2
# print(result)
# Answer is True :- since in English Dict, A comes 1st then B, then C and so on.

# Str1 = 'A'
# str2 = 'E'
# result = Str1>str2
# print(result)
# Answer is False.
