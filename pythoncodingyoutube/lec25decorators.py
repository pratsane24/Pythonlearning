# What is need of decorators?
# How to measure the time taken for exicuation of program?
# If the code contains many function then u have to wirte that function  again and again to measume the time.

# import time


# def calc_square(numbers):
#     start = time.time
#     result = []
#     for number in numbers:
#         result.append(number*number)
#     end = time.time
#     print("calc_square took" + str((end+start)*1000) + "mil sec")
#     return result

# def calc_cube(numbers):
#     start = time.time
#     result = []
#     for number in numbers:
#         result.append(number*number*number)
#     end = time.time
#     print("calc_cube took" + str((end+start)*1000) + "mil sec")
#     return result

# array = range(1,100000)
# out_square = calc_square(array)
# out_cube = calc_cube(array)

# In this one functions gets merge with another function, so decorators are used.

# functions are 1st class object in python.What it means is that they can be treated just like any other variable and you can
# pass them as argument to another function or even return them as a return value.

import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        # print(type(func.__name__))
        # print(type("took"))
        # print(type(end-start))
        # print(type("mil sec"))
        print(func.__name__ + "took" +str((end-start)*1000) +"mil sec")
        return result
    
    return wrapper

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
   
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100)
out_square = calc_square(array)
out_cube = calc_cube(array)

print(out_cube)
print(out_square)

