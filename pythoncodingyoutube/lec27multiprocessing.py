# Question:-
# Create two processes,
# 1. First is to calculate square of all numbers
# 2. Second  one is to calculate cube of numbers

# solution:-

# import time
# import multiprocessing

# def cal_square(numbers):
#     for n in numbers:
#         time.sleep(5)
#         print("square" + str(n*n))

# def cal_cube(numbers):
#     for n in numbers:
#         time.sleep(5)
#         print("cube" + str(n*n*n))
       
# if __name__ == "__main__":
#     arr = [2,3,8,9]
#     p1 = multiprocessing.Process(target=cal_square, args=(arr,))
#     p2 = multiprocessing.Process(target=cal_cube, args=(arr,))
    
#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

# print("Done")

# Lets Store the result in global variable

import time
import multiprocessing

square_result=[]

def cal_square(numbers):
    global square_result
    for n in numbers:
        print("square " + str(n*n))
        square_result.append(n*n)
    print("with in process: result " + str(square_result))
       
if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=cal_square, args=(arr,))
    
    
    p1.start()
    p1.join()
    
    print("result " + str(square_result))
    print("Done")

# Every process has its own address space(virtual memory).Thus program variables are not shared between two processes.
# you need to use interprocess communication(IPC) techniques if you want to share data between two processes.

# NOTE:- Always write __main__ at the end of code in every code in python.
