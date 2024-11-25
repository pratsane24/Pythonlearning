# Topis t be covered in this tutorial ArithmeticError
# 1.Indexing and slicing
# 2.Iterating through arrays
# 3.Stacking together two arrays
# 4.Indexing with boolean arrays. 

# 1.Indexing and slicing
import numpy as np
# n=[6,7,8]
# print(n[0:2])

# OUTPUT:
# [6, 7]

# -1 means the last element in the row.
# print(n[-1])

# Same for array
# a=np.array([6,7,8])
# print(a[0:2])
# print(a[-1])

# multi-dimension array
# a=np.array([[6,7,8],[1,2,3],[9,3,2]])
# print(a)
# print(a[1,2])
# print(a[0:2,2])
# print(a[-1])
# print(a[-1,0:2])
# print(a[:,1:3])

#  2.Iterating through arrays
# a=np.array([[6,7,8],[1,2,3],[9,3,2]])
# print(a)
# for row in a:
#     print(row)

# for cell in a.flat:
#     print(cell)

#  3.Stacking together two arrays

# a= np.arange(6).reshape(3,2)
# b= np.arange(6,12).reshape(3,2)
# print(a)
# print(b)
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))
# a=np.arange(30).reshape(2,15)
# print(a)
# print(np.hsplit(a,3))
# result = np.hsplit(a,3)
# print(result[0])
# print(result[1])
# print(result[2])

# result = np.vsplit(a,2)
# print(result[0])
# print(result[1])

a=np.arange(12).reshape(3,4)
# print(a)
b= a>4
# print(b)

# When u look from a towards b then they print value 
# print(a[b])

# IF u want to replace any no. with any other no. or value
a[b]=-1
print(a)
