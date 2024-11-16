# What is regular expression?
# regular expression is also known as python RegEx in python.
# A regular expression(RegEx) is a sequence of characters that defines a search pattern.
# For using Regular Expression import re module.

# There are 2 types of function:
# 1. Match function
# 2. Search Function

# what is match function ?
# This function determines if the RE matches at the beginning of the string.
# Syntax:- re.match(pattern, string)
# Pattern :- This the regular expression to be matched

# String :- This is the string,which would be searched to match the pattern at the beginning of string.

#  Prctical
# # Match function
# #Import re module first
# import re
# pattern = r"^abc"
# mystring = "abcdef"

# x= re.match(pattern,mystring)
# print(x)

# # OUTPUT:- 
# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/regularexpression.py
# <re.Match object; span=(0, 3), match='abc'>

# Another E.g
# import re
# pattern = r"^abc"
# mystring = "acdef"

# x= re.match(pattern,mystring)
# print(x)
# OUTPUT:-
# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/regularexpression.py
# None
# Since pattern is not matched so output is none.

# Another E.g
# import re
# pattern = r"^abcd"
# mystring = "abcdef"

# x= re.match(pattern,mystring)
# print(x)
# OUTPUT:-
# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/regularexpression.py
# <re.Match object; span=(0, 4), match='abcd'>

# Another E.g
# import re
# pattern = r"^bcd"
# mystring = "abcdef"

# x= re.match(pattern,mystring)
# print(x)

# OUTPUT:-
# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/regularexpression.py
# None


# What is search function?
# Scan through a string,looking for any location where this RE matches.
# Syntax :- re.search(pattern,string)
# Pattern:- This is the regular expression to be matched.
# String:- THis is the string,which would be searched to match the pattern at the beginning of the string.

# Practice
# Search function
# import re module 1st
# imporst re
# txt = "We are learning python"
# THis expression is written for searching white space or blank space.
# x= re.search("\s",txt)
# print("The first whitespace: ",x.start())
# OUTPUT:-
# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/regularexpression.py
# The first whitespace:  <re.Match object; span=(2, 3), match=' '>


# OUTPUT:-
# To know where exact white space starts add .start() in print section.
# Ypu will get this output.
# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/regularexpression.py
# The first whitespace:  2

# Another E.g
# import re
# txt = "The rain in Gujarat"
# x=re.search("Ahmedabad",txt)
# print(x)

# OUTPUT:-

# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/regularexpression.py
# None
# since there is n word as ahmedabad in txt.


# What is Replace Function?
# Python regex offers sub() the subn() methods to search and replace patterns in a string.Using these methods we can
# replace one or more occurences of a regex pattern in the target string with substitute string.

# Syntax:- re.sub(pattern,repl,string)

# Practical
# 
# import re
# str1 ="Learnvern provide free online training"
# print("Before replace",str1)

# # After replace the word provide with python from str1

# result = re.sub(r"provide","python",str1)
# print("After Replace :",result)

# OUTPUT:-
# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/regularexpression.py
# Before replace Learnvern provide free online training
# After Replace : Learnvern python free online training

# Another E.g
# import re
# str1 ="Learnvern Provide Free Online Training"
# print("Before replace",str1)

# # Replace where there is a small word, it should be printed as 0.

# Result = re.sub(r"[a-z]","0",str1)
# print("After replace :",Result)

# Output:-
# PS D:\PYTHON\pythonlearnvern> & "C:/Program Files/Python310/python.exe" d:/PYTHON/pythonlearnvern/regularexpression.py
# Before replace Learnvern Provide Free Online Training
# After replace : L00000000 P000000 F000 O00000 T0000000