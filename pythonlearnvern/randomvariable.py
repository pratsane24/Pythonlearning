# What is Random Variable
# Python provide multiple inbuilt function that are used to choose or generate random number by using random module.

# Random Number Operations
# Choice():
# Choice() is inbuilt function of random module, which is used to return random number from list,tuple,set.
# Randint():
# randint() is inbuilt function of random module,which is used to generate random number from particular given range.E.g is OTP.
# Shuffle():
# Shuffle() is inbuilt function of random module,which is used to shuffle a value of list.

# What can be done ?
# Import random
# Random operations

# Import Random
# from random import function name
# import random
# 
# # Choice()
# from random import choice
# l1=[1,2,3,4,5,6]
# print(choice(l1)) 
# Here it gives any random variable in output.

# # Randint()
# # It is used to generate random no in particular range.
# from random import randint
# otp = randint(10000,999999)
# print("Your OTP :",otp)

# # Shuffle Function()
# # E.g You might have played candy crush, in that game ghe candy gets shuffle like that here also shuffle() works
# from random import shuffle
# l2 = ["Apple","Banana","Mango"]
# x=shuffle(l2)
# print(l2)
# # Shuffle means from ur particular list, everytime u run the code, ur list will get shuffle.