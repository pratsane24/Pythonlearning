# 1.

# for i in range(7):
#     for j in range(5):
#         if(j==0 or (i==0 or i==6)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# OUTPUT:
# * * * * *   
# *   
# *
# *
# *
# *
# * * * * *

# 2.

# for i in range(7):
#     for j in range(5):
#         if(j==0)  or (j==4 and (i!=0 and i!=6)) or ((i==0 or i==6) and (j>0 and j<4)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# OUTPUT

# * * * *   
# *       * 
# *       *
# *       *
# *       *
# *       *
# * * * *

# 3.

# for i in range(4):
#     for j in range(7):
#         if(j==0) or (j==6) or (i==2 and j==1) or (i==1 and j==2) or (i==0 and j==3) or (i==1 and j==4) or (i==2 and j==5):  
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# OUTPUT

# *     *     * 
# *   *   *   * 
# * *       * *
# *           *

# 4.

# for i in range(5):
#     for j in range(5):
#         if(i==j) or (i==0 and j==4) or (i==1 and j==3) or (i==3 and j==1) or (i==4 and j==0) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ANOTHER METHOD

# a=0
# b=4
# for i in range(5):
#     for j in range(5):
#         if i==a and j==b:
#             print("*",end=" ")
#             a=a+1
#             b=b-1
#         elif i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# OUTPUT
# *       * 
#   *   *   
#     *
#   *   *
# *       *

# 5.

# for i in range(7):
#     for j in range(4):
#         if(j==0) or (i==2 and j==1) or (i==1 and j==2) or (i==0 and j==3) or (i==4 and j==1) or (i==5 and j==2) or (i==6 and j==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# OUTPUT
# *     * 
# *   *   
# * *
# *
# * *
# *   *
# *     *

# 6.

# a=0
# b=4
# for i in range(7):
#     for j in range(5):
#         if(j==0) or (i==j+2 and j>1):
#             print("*",end=" ")
#         elif (i==a and j==b):
#             print("*",end=" ")
#             a=a+1
#             b=b-1
#         else:
#             print(" ",end=" ")
#     print()

# OUTPUT:
# *       * 
# *     *   
# *   *
# * *
# *   *
# *     *
# *       *


# 7.

# string = input ("Enter the string: ")
# length = len(string)
# for row in range(length):
#     for col in range(row+1):
#         # NOTE :- here in range for column,
#         # if row=0
#         # col=range(row+1)
#         # col=range(0+1)
#         # col=range(1)
#         # i.e it will print (row,col) as (0,0) and it will move to next line.
#         print(string[col],end=" ")
#     print()

# OUTPUT
# Enter the string: python
# p 
# p y
# p y t
# p y t h
# p y t h o
# p y t h o n

# 8.

# n = int(input("Enter the no of rows:"))
# for row in range(n,0,-1):
#     # In this range (n,0,-1), it will follow the following sequence of 5,43,2,1 in row numbering
#     for col in range(1,row+1):
#         print(col,end="")
#     print()

# OUTPUT:
# Enter the no of rows:6
# 123456
# 12345
# 1234
# 123
# 12
# 1

# 9.

# n = int(input("Enter the no of rows:"))
# for row in range(n,0,-1):
#     # In this range (n,0,-1), it will follow the following sequence of 5,43,2,1 in row numbering
#     for col in range(1,row+1):
#         print(row,end="")
#     print()

# OUTPUT:
# Enter the no of rows:5
# 55555
# 4444
# 333
# 22
# 1

# 10.

# num = int(input("Enter the number:"))
# n_list = [[0 for x in range(num)] for y in range(num)]

# n = 1
# low=0
# high = num-1
# count =int((num+1)/2)
# for i in range(count):
#     for j in range(low,high+1):
#         n_list[i][j]=n
#         n=n+1
#     for j in range(low+1,high+1):
#         n_list[j][high]=n
#         n=n+1
#     for j in range(high-1,low-1,-1):
#         n_list[high][j]=n
#         n=n+1
#     for j in range(high-1,low,-1):
#         n_list[j][low]=n
#         n=n+1
#     low=low+1
#     high=high-1

# for i in range(num):
#     for j in range(num):
#         print(n_list[i][j], end="\t")
#     print()

# OUTPUT:
# Enter the number:5
# 1       2       3       4       5
# 16      17      18      19      6
# 15      24      25      20      7
# 14      23      22      21      8
# 13      12      11      10      9

# another sample:
# Enter the number:4
# 1       2       3       4
# 12      13      14      5
# 11      16      15      6
# 10      9       8       7

# 11.

# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     for j in range(1,num-i+1):
#         print(" ",end=" ")
#     for k in range(i,0,-1):
#         print(k,end=" ")
#     for l in range(2,i+1):
#         print(l,end=" ")
#     print()

# OUTPUT:
# Enter a number: 4
#       1 
#     2 1 2
#   3 2 1 2 3
# 4 3 2 1 2 3 4

# 12.

