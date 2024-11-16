# List Comprehension provides a way to transform one list into another.

# Queston:- to print even no?
# numbers = [1,2,3,4,5,6,7]
# even=[]
# for i in numbers:
#     if i%2==0:
#         even.append(i)
# print(even)
# Another method
# numbers = [1,2,3,4,5,6,7]
# even = [i for i in numbers if i%2==0]
# print(even)

# Question:- To find sqr of numbers
# numbers = [1,2,3,4,5,6,7]
# sqr_numbers =[i*i for i in numbers]
# print(sqr_numbers)

# Set
# Set is an unordered collection of items .
# Basic difference betn set n list is:- set doesn't allow u to contain duplicate items n it is unordered.
# s=set([1,2,3,4,5,2,3])
# print(s)
# even = {i for i in s if i%2==0}
# print(even)

# Dictionary comprehension
# cities = ["mumbai","new york","paris"]
# countries = ["india","usa","france"]
# z=zip(cities,countries)
# print(z)
# for a in z:
#     print(a)

# d={city:country for city, country in zip(cities,countries)}
# print(d)
