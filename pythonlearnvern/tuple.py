# What is tuple?
# Tuple is collection in python.
# Tuple is immutable(No Changeable at runtime).
# Tuple allows multiple datatype values to be stored
# Tuple is working on Index value starting from zero(0)

# What can be done?
# create tuple
# Indexing & slicing.

# 1.Create tuple
# It is identified by () Brackets.

# t1=("Apple","Mango","Cherry","Orange",1,2,3,4,5,10,5,12.5,5,4)
# print("Current Tuple :",t1)

# # How to Check length of tuple?
# t2=(1,2,3,4,5,6,7,8,9)
# print("Size of tuple :",len(t2))

# Slicing/Indexing Of tuple
# t1=("Apple","Mango","Cherry","Orange",1,2,3,4,5,10,5,12.5,5,4)
# print("Current Tuple :",t1)
# # Accessing the value by using tuple
# print("Index 1 Value :",t1[1])
# # Accessing the value betn index 1 to 6
# print("Index 1-6 Value :",t1[1:6])
# # Access  the last value
# print("Last value :",t1[-1])
# # Access the value till index 6.
# print("Till index 6 :",t1[:6])




# Convert tuple to list
# t1=("Apple","Mango","Cherry","Orange",1,2,3,4,5,10,5,12.5,5,4)
# #  Before Change
# print("Current Tuple :",t1)

# x=list(t1)
# print("After Converting :",x)

# Tuple Constructor
# t3 = tuple(("apple","mango","cherry"))
# # NOTE: the double round brackets(()) doesn't mean truple, You have created tuple by using tuple construtor.
# print(t3)

# Add Item but after converting tuple into list

# t4=("Apple","Mango","Cherry","Orange")
# print("Current Tuple :",t4)
# print(type(t4))
# # Convert tuple into list
# x=list(t4)
# print("Converted into list:",x)
# print(type(x))
# # After Converting
# # Add value
# x[1]="kiwi"
# print("Updated list :",x)
# # Convert list into tuple again
# y=tuple(x)
# print("updated tuple :",y)


# Loops with tuple

# For loops with tuple
# t5=("Apple","Mango","Kiwi","Orange")
# for i in t5:
#     print(i)

# While loop with tuple NOTE:- While loop is infinite it will run in loop until u stop it, so condition is need to be provided.
# t5=("Apple","Mango","Kiwi","Orange")
# i=0
# while i<len(t5):
#     print(i)
#     i=i+1
# else: 
#     print("loop finished")

# Output is this since we printed i, We need to print index also.
# 0
# 1
# 2
# 3
# loop finished.

# After Changes, We will get desired output.

# t5=("Apple","Mango","Kiwi","Orange")
# i=0
# while i<len(t5):
#     print(t5[i])
#     i=i+1
# else: 
#     print("loop finished")

# How to compare tuple?
# tuple1=(1,2,3)
# tuple2=(1,2,4)
# # Tuple1 is equal to tuple2
# print(tuple1==tuple2)

# # tuple1 is less than tuple2
# print(tuple1<tuple2)
# # Note:- Tuple2 is greater since 4 is greater than 3.

# # tuple1 is greater than tuple 2
# print(tuple1>tuple2)