import numpy as np

# Saving as text file 
'''x = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]],np.int32)
np.savetxt("numpy/test.txt",x)'''


y= np.loadtxt(("numpy/test.txt"))
print(y)

# np.savetxt("numpy/test.txt", x)
# print("Array saved to test.txt")