# What is looping statement?
# Loop control statements change execution from its normal sequence. When execution leaves a scope,
# all automatic objects that were created in that scope are destroyed.
# Different types of loops
# 1.While loop
# 2.For loop
# 3.Nested For loop

# 1.While loop
# Question:- We need to print a sequence, 5,9,12,14,15 by using while loop.
# Solution
# sum=0
# n=int(input("N: "))
# while n>0:
#     sum = sum+n
#     n-=1
#     print("sum: ",sum)
# print("Bye")

# While loop with else part
# only in python we can use else part in while loop.

# sum=0
# n=int(input("N: "))
# while n>0:
#     sum = sum+n
#     n-=1
#     print("sum: ",sum)
# else:
#     print("loop Error")
# print("Bye")


# 2.Simple For loop
# see iteration & Also calculate length of words.
# Solution for i= iteration
# word=["python","Java", "Graphic","Angular"]
# for i in word:
#     print(i)


# # Solution for length of words.
# word=["python","Java", "Graphic","Angular"]
# for i in word:
#     print(i,'=',len(i))

# 3. Nested for loop.
# Question:-
#   *
#   **
#   ***
#   ****
#   *****

# Solution:In this we need to use range.
# range(start point,end point,step(jump))
# In this we need to use I=row, J=column.
#
for i in range(1,6):
#     # Alway use +1 increment for end range(value).
    for j in range(i):
        print("*",end="")
        # This print is used to print * & end="" to end with space.
    print()
    # This print is used to jump in sencond row.

# How to do to reverse ?
# for i in range (5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

