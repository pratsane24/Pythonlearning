# Question
# For a given list of numbers print square and cube of every numbers
# E.g :- Input :[2,3,8,9]
# Output:- Square list - [4,9,64,81]
# cube list - [8,27,512,729]

# import time
# def cal_square(numbers):
#     print("calculate square numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("square :",n*n)

# def cal_cube(numbers):
#     print("calculate cube of the numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("Cube",n*n*n)

# arr = [2,3,8,9]
# t=time.time()
# cal_square(arr)
# cal_cube(arr)

# print("done in :",time.time()-t)
# print("Haaa.....I am done with all my work now!")

# OUTPUT:-
# calculate square numbers
# square : 4
# square : 9
# square : 64
# square : 81
# calculate cube of the numbers
# Cube 8
# Cube 27
# Cube 512
# Cube 729
# done in : 1.6454122066497803
# Haaa.....I am done with all my work now!


# NOW to improve the speed we will be doing multithreading for the same program

# import time
# import threading
# def cal_square(numbers):
#     print("calculate square numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("square :",n*n)

# def cal_cube(numbers):
#     print("calculate cube of the numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("Cube",n*n*n)

# arr = [2,3,8,9]
# t=time.time()
# t1=threading.Thread(target=cal_square,args=(arr,))
# t2=threading.Thread(target=cal_cube,args=(arr,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print("done in :",time.time()-t)
# print("Haaa.....I am done with all my work now!")

# OUTPUT:- 
# calculate square numbers
# calculate cube of the numbers
# Cube 8
# square : 4
# Cube 27
# square : 9
# square : 64
# Cube 512
# square : 81
# Cube 729
# done in : 0.8433890342712402
# Haaa.....I am done with all my work now!

# Note:- Now compare the the time from e,g before using thread and after using thread.

# multi-threading in python is little spl bze there is something called group Global interpreted lock that prevents you from using
# the true benifits ofs multi-threading but in case whenever you are waiting or doing io bound operation u can still use
# multi-threading.

