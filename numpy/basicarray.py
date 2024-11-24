import numpy as np
# a = np.array([5,6,9])
# print(a[0])
# print(a[1])

# NOTE:- HERE ndim means no of dimensions
# a=np.array([[1,2],[3,4],[5,6]])
# print(a.ndim)

# a=np.array([5,6,9])
# print(a.ndim)
# print(a.itemsize)
# print(a.dtype)
# a=np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
# print(a.itemsize)
# print(a)

# print(a.size)
# print(a.shape)



# a=np.array([[1,2],[3,4],[5,6]], dtype=np.complex64)
# print(a)

# 
# print(np.zeros((3,4)))
# print(np.ones((3,4)))

# l = range(5)
# print(l)
# print(l[0])

# print(np.arange(1,5))

# # U start at 1 and take a step at 2 n then print 3 for that follow
# print(np.arange(1,7,2))

# # lin space 
# print(np.linspace(1,5,10))
# print(np.linspace(1,5,5))

# u can reshape array
a=np.array([[1,2],[3,4],[5,6]])
print(a)
print(a.shape)
# reshaped_a = a.reshape(2, 3)  
# # Change the shape to (2, 3)
# print(reshaped_a)
# another method
print(a.reshape(2,3))
print(a.ravel())
print(a)
print(a.min())
print(a.max())
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(np.sqrt(a))
print(np.std(a))
