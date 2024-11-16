# NOTE:PATTERN 1
# *
# **
# ***
# ****
# *****
# soln:-
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print() 

# Alternate method
# *
# * *
# * * *
# * * * *
# * * * * *
# Soln:-
# row = int(input("Enter the no rows: "))
# for i in range(0,row):
#     for j in range(0,i+1):
#         print("*",end=(" "))
#     print()


# NOTE:PATTERN 2
# *****
# ****
# ***
# **
# *
# Soln:-
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# Alternate Method
# * * * * *
# * * * *
# * * *
# * *
# *

# Soln:-
# row = int(input("Enter the no rows: "))
# for i in range(0,row):
#     for i in range(0,(row-i)):
#          print("*",end=" ")
#     print()


# NOTE:PATTERN 3
# *
# ***
# *****
# Soln:=
# n = int(input("Enter no of rows"))
# k = 1
# for i in range(1,n):
#     for j in range(1,k+1):
#         print("*",end="")
#     k=k+2
#     print()

# NOTE: PATTERN 4
#     *
#    **
#   ***
#  ****
# *****
# totalrow = int(input("Enter the no rows: "))
# # This logic is for no. of rows. (since rows=column)
# for row in range(1,totalrow+1):
# # This logic is for space; space=total row - row no)
#     for space in range(1,((totalrow-row)+1)):
#          print(" ",end=" ")

#     for star in range(1,row+1):
#         print("* ",end="")
#     print()

# NOTE: PATTERN 5

