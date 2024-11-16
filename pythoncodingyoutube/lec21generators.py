# What is generator?
# Generator is a simple way of creating iterator.
# This tool is IDLE that comes free with python installation.

# def remote_control_next():
#     yield "Cnn"
#     yield "espn"
    
# itr = remote_control_next()
# # print(itr)
# # print(next(itr))
# # print(next(itr))

# for c in remote_control_next():
#     print(c)

# We are going to produce fibonacci sequence using generator.
#  What is fibonacci sequence:-
#  0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , .........
# It is sum of 1st two nos, & the sequence goes on.

# def fib():
#     a,b = 0,1
#     while True:
#         yield a 
#         a,b = b,a+b

# for f in fib():
#     if f>100:
#         break
#     print(f)

# Benifits of using generator over class based iterator
# 1.You don't need to define iter() and next() method.
# 2.You don't need to raise StopIteration exception.