# Eg. 1
# def get_squared_numbers(numbers):
#     squared_numbers = []
#     for n in numbers:
#         squared_numbers.append(n*n)
#     return squared_numbers

# numbers = [2,4,8,9]
# print(get_squared_numbers(numbers))

# In this there are n nos, we are doing for 4 but there might be millions or thousands of data,
# As the data or input increase time increases to perform the function.
# Time is directly proportion to input
# i.e O(n).

# E.g 2
# def find_first_pe(prices,eps,index):
#     pe = prices[index]/eps[index]
#     return pe
   
# Here it is time = O(1)


# E.g 3
# Here we are finding duplicate from a list
# numbers = [3,6,2,4,3,6,8,9]
# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i] == numbers[j]:
#             print(numbers[i], "is a dupicate")
#             break

# [4,9,15,21,34,57,68,91] Search for 68 from this?
# Easiest method is O(n)
numbers =[4,9,15,21,34,57,68,91]
for i in range(len(numbers)):
    if numbers[i] == 68:
        print(i)
# Another method is binary element
