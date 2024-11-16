# PATTERN 1
# for j in range(4):
#     print ("*",end=" ")
# print()
# for j in range(4):
#     print ("*",end=" ")
# print()
# for j in range(4):
#     print ("*",end=" ")
# print()
# for j in range(4):
#     print ("*",end=" ")
# print()

# NOTE:- Here we are using same code again and again, so to maake it easy we can use another loop and put this
# code into it.

# for i in range(4):
#     for j in range(4):
#         print("*",end=" ")
#     print()

#  NOTE : We are getting the same output.
# * * * * 
# * * * * 
# * * * *
# * * * *


# PATTERN 2
# for i in range(4):
#     for j in range(i+1):
#         # since here range starts from 0 to 3 so it will not print any * in 1st row.
#         # therefore we are using i+1, and here the logic is u have to print stars (*) = no of rows
#         # like 1st row 1 star, 2nd row 2 star,etc. 
#         print("*",end=" ")
#     print()

# OUTPUT
# *
# * *
# * * *
# * * * *

# PATTERN 3

# for i in range(4):
#     for j in range(4-i):
#         print("*",end=" ")
#     print()

# NOTE:- think about this logic,as the row no increases star decreases,i.e in 1st row 4 star,
# 2nd row 3 stars then logic becomes (4-i)
# i.e 4-0 = 4
# 4-1=3 and so on.


# * * * * 
# * * * 
# * *
# *

# PATTERN 4

# n = 5
# for i in range(n):

#     for j in range(n-i):
#         print("  ", end="")
 
#     for j in range(i+1):
#         print("* ",end="")
#     print()

# NOTE:- Always remember that while using using multiple for loops,cross check your space, * , n etc in print statement.
# Bze the value in "" will change the shape of your pattern. 

# OUTPUT
#           * 
#         * * 
#       * * *
#     * * * *
#   * * * * *

# PATTERN 5
# n = 5
# for i in range(n):
#     for k in range(i+1):
#         print("  ",end=" ")
#     for j in range(n-i):
#         print("* ",end=" ")
#     print()

# OUTPUT:
#    *  *  *  *  *  
#       *  *  *  *  
#          *  *  *
#             *  *
#                *


# PATTERN 6
# n = 5
# for i in range(n):

#     for j in range(n-i):
#         print("  ", end="")
 
#     for k in range(i+1):
#         print("* ",end="")

#     for l in range(i):
#         print("* ",end="")

#     print()

# # OUTPUT:
#           * 
#         * * * 
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *


# PATTERN 7
# n = 5
# for i in range(n):

#     for j in range(i+1):
#         print("  ", end="")
 
#     for k in range(n-i):
#         print("* ",end="")

#     for k in range(n-i-1):
#         print("* ",end="")

#     print()

# OUTPUT:
#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * *
#         * * *
#           *

#     # PATTERN 8
# n = 5
# for i in range(n-1):

#     for j in range(n-i):
#         print("  ", end="")
 
#     for k in range(i+1):
#         print("* ",end="")

#     for l in range(i):
#         print("* ",end="")

#     print()

# for i in range(n):

#     for j in range(i+1):
#         print("  ",end="")
 
#     for k in range(n-i):
#         print("* ",end="")

#     for l in range(n-i-1):
#         print("* ",end="")

#     print()

# OUTPUT:
#           * 
#         * * * 
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *


# PATTERN 9
#      * 
#     * * 
#    * * *
#   * * * *
#  * * * * * 
# Soln:=
# n = 5
# for i in range(n):

#     for j in range(n-i-1):
#         print(" ", end="")
# #  NOTE :- Here we are using -1 bze we want decrement in space triangle.
#     for k in range(i+1):
#         print("* ",end="")
#     print()


# Alternate soln:
# n = 5
# for i in range(n):

#     for j in range(n-i):
#         print(" ", end="")

#     for k in range(i+1):
#         print("* ",end="")
#     print()


# PATTERN 10
# n=7

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("* ",end="")
#     print()
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(n-i-1):
#         print("* ",end="")
#     print()

# OUTPUT
#       *
#      * * 
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *
# * * * * * * *
#  * * * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *