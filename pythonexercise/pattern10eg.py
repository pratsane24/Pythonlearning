# NOTE:PATTERN 1
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
        
    

# NOTE: PATTERN 2
# * * * * * 
# * * * * 
# * * *
# * *
# *

# # 1st logic
# for i in range(5,0,-1):
#     for j in range(i):
#         print("* ",end="")
#     print()

# # 2nd logic
# for i in range(0,5):
#     for j in range(0,(5-i)):
#         print("* ",end="")
#     print()

# 3rd logic
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()

# NOTE:PATTERN 3
# * 
# * * 
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# no_rows = int(input("Enter no of rows: "))
# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         print("*",end=(" "))
#     print()

# for i in range(no_rows-1,0,-1):
# #     # We are using 4 in place of 5 bze 5 stars should be printed only once.
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()


# NOTE:PATTERN 4
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# no_rows = int(input("Enter no of rows: "))
# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         print(i,end=(" "))
#     print()


# NOTE:PATTERN 5
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# no_rows = int(input("Enter no of rows: "))
# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         print(j,end=(" "))
#     print()

# NOTE:PATTERN 6
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# no_rows = int(input("Enter no of rows: "))
# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         print(i,end=(" "))
#     print()

# for i in range(no_rows-1,0,-1):
# #     # We are using 4 in place of 5 bze 5 stars should be printed only once.
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# # NOTE:PATTERN 7
# 11 
# 12 22
# 13 23 33
# 14 24 34 44
# 15 25 35 45 55
# no_rows = int(input("Enter no of rows: "))
# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         print("{0}{1}".format(j,i),end=(" "))
#     print()

# # NOTE:PATTERN 8
# 11 
# 21 22
# 31 32 33
# 41 42 43 44
# 51 52 53 54 55
# no_rows = int(input("Enter no of rows: "))
# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         print("{0}{1}".format(i,j),end=(" "))
#     print()

# NOTE:PATTERN 9
# 11 
# 22 22
# 33 33 33
# 44 44 44 44
# 55 55 55 55 55
# no_rows = int(input("Enter no of rows: "))
# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         print("{0}{1}".format(i,i),end=(" "))
#     print()

# NOTE:PATTERN 10
# 11 
# 11 22
# 11 22 33
# 11 22 33 44
# 11 22 33 44 55
# no_rows = int(input("Enter no of rows: "))
# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         print("{0}{1}".format(j,j),end=(" "))
#     print()


# NOTE: PATTERN 11
# 11 
# 21 22
# 31 32 33
# 41 42 43 44
# 51 52 53 54 55
# 41 42 43 44
# 31 32 33
# 21 22
# 11
# no_rows = int(input("Enter no of rows: "))
# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         print("{0}{1}".format(i,j),end=(" "))
#     print()

# for i in range(no_rows-1,0,-1):
# #     # We are using 4 in place of 5 bze 5 stars should be printed only once.
#     for j in range(1,i+1):
#         print("{0}{1}".format(i,j),end=(" "))
#     print()

# # NOTE: PATTERN 11
# A 
# A A
# A A A
# A A A A
# A A A A A
# no_rows = int(input("Enter no of rows: "))

# ch = 65
# NOTE:65 is chronological start no. of capital A.

# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         print("{0}".format(chr(ch)),end=(" "))
#     print()



# NOTE:PATTERN 12
# A 
# A B
# A B C
# A B C D
# A B C D E
# no_rows = int(input("Enter no of rows: "))

# ch = 64

# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         print("{0}".format(chr(ch+j)),end=(" "))
    # print()

# NOTE:PATTERN 13
# A 
# A B
# A B C
# A B C D
# A B C D E
# A B C D
# A B C
# A B
# A

# no_rows= int(input("Enter no of rows: "))

# ch = 64

# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#        print("{0}".format(chr(ch+j)),end=(" "))
#     print()

# for i in range(no_rows-1,0,-1):
# #     # We are using 4 in place of 5 bze 5 stars should be printed only once.
#     for j in range(1,i+1):
#         print("{0}".format(chr(ch+j)),end=(" "))
#     print()


# PATTERN 14
# A 
# B B
# C C C
# D D D D
# E E E E E
# D D D D
# C C C
# B B
# A
# no_rows= int(input("Enter no of rows: "))

# ch = 64

# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#        print("{0}".format(chr(ch+i)),end=(" "))
#     print()

# for i in range(no_rows-1,0,-1):
# #     # We are using 4 in place of 5 bze 5 stars should be printed only once.
#     for j in range(1,i+1):
#         print("{0}".format(chr(ch+i)),end=(" "))
#     print()

# # PATTERN 15
# A 
# B C
# D E F
# G H I J
# K L M N O
# P Q R S
# T U V
# W X
# Y
# no_rows= int(input("Enter no of rows: "))

# ch = 64

# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         ch = ch + 1
#         print("{0}".format(chr(ch)),end=(" "))
#     print()

# for i in range(no_rows-1,0,-1):
# #     # We are using 4 in place of 5 bze 5 stars should be printed only once.
#     for j in range(1,i+1):
#         ch = ch + 1
#         print("{0}".format(chr(ch)),end=(" "))
#     print()


# PATTERN 16
# A 
# B C
# D E F
# G H I J
# K L M N O
# no_rows= int(input("Enter no of rows: "))

# ch = 64

# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         ch = ch + 1
#         print("{0}".format(chr(ch)),end=(" "))
#     print()


# PATTERN 17
# A B C D 
# E F G
# H I
# J
# no_rows= int(input("Enter no of rows: "))

# ch = 64

# for i in range(no_rows-1,0,-1):
# #     # We are using 4 in place of 5 bze 5 stars should be printed only once.
#     for j in range(1,i+1):
#         ch = ch + 1
#         print("{0}".format(chr(ch)),end=(" "))
#     print()

# PATTERN 18
# 01 
# 02 03
# 04 05 06
# 07 08 09 10
# 11 12 13 14 15
# no_rows= int(input("Enter no of rows: "))

# sum = 0

# for i in range(1,no_rows+1):
#     for j in range(1,i+1):
#         sum = sum + 1
#         print("{:02d}".format(sum),end=(" "))
#         # Here we are using :02d since we want 2 spaces to save our no. like in formate of 01,11,02,22,etc.
#     print()


