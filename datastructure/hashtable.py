# In form of list (ARRAY).
# stock_price = []
# with open("datastructure/hashtable.csv","r") as f:
#     for line in f :
#         tokens = line.split(',')
#         day = tokens[0]
#         price = float(tokens[1])
#         stock_price.append([day,price])   
        # Here we are reading the file and going throught the line one by one
        # HEre we are spliting them by , & storing them in day and price into an ARRAY.
    # print(stock_price)    
    # NOTE :- In output 0th element is day and 1st is price.

# If u want price on march 9
    # for element in stock_price:
    #      if element[0] == '09-Mar':
    #         print(element[1])

# If there are million of u have to do that no of iteration, So the complexity of is of the order of n.

# To find price according to day it is pbm of n complexitiy.
# In python there is dictonary which does the same thing in order of 1 which is constant time operation.

# In form of dictonary
# stock_price = {}
# with open("datastructure/hashtable.csv","r") as f:
#     for line in f :
#         tokens = line.split(',')
#         day = tokens[0]
#         price = float(tokens[1])
#         stock_price[day] = price
#     print(stock_price)
# print(stock_price["09-Mar"])

# Dictonary uses a hashtable.
# Hashtable/hashmap is a internal datastrucuture and dictonary is a python specific implementation of hashtable.
# LOOKUP by key is O(1) (Order of 1) on average
# Insertion/Deletion is O(1)(Order of 1) on average
# Hash table uses table which has values of all characters n no then sum up then get MOD.
# E.G MOD(609/10)=9 (where 10 is the size of array, which can differ.)

# def get_hash(key):
#     h = 0 
#     for char in key :
#         h += ord(char)
#     return h % 100
#     # Here 100 is size of array.
# print(get_hash("march 28"))
# print(ord('a'))

# class hashtable:
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [None for i in range(self.MAX)]

#     def get_hash(self,key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.MAX
# t = hashtable()
# print(t.get_hash('march 6')) 

# Now we want to implement a function which can add/remove an item into a hashmap.
# Like from previous eg me have day and price, we have to add key value pair.

# class hashtable:
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [None for i in range(self.MAX)]

#     def get_hash(self,key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.MAX

#     def add(self,key,val):
#         h = self.get_hash(key)
#         self.arr[h] = val

#     def get(self,key):
#         h = self.get_hash(key)
#         return self.arr[h]

# t = hashtable()
# t.add('march 6',130)
# print(t.arr) 

# NOTE :- IN OUTPUT THE VALUE 130 IS DISPLAYED AT 9TH POSITION, SINCE THE HASHMAP FOR MARCH 6 IS 9.
# print(t.get('march 6'))
# NOTE :- HERE U GET THE OUTPUT AS 130.

# NOTE:- HERE WE CAN DO THIS BY USING METHOD USED FOR DICTONARY FUNCTION LIKE ARRAY, THIS WILL REDUCE THE WORK OF DEFINING THE ADD & GET FUNCTION ,ETC.
# E.G
# class hashtable:
#     def __init__(self):
#         self.MAX = 10
#         self.arr = [None for i in range(self.MAX)]

#     def get_hash(self,key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.MAX

#     def __setitem__(self,key,val):
#         h = self.get_hash(key)
#         self.arr[h] = val

#     def __getitem__(self,key):
#         h = self.get_hash(key)
#         return self.arr[h]

#     def __delitem__(self,key):
#        h = self.get_hash(key)
#        self.arr[h] = None 

# t = hashtable()
# t['march 6'] = 130
# t['march 1'] = 20
# t['dec 10'] = 30
# # print(t.arr) 
# # print(t['march 17'])
# # print(t['march 1'])
# # del t['march 6']
# print(t.arr)


# It does not handle collision since if the index repeats it over-right the value of 1st element.
# t = hashtable()
# t['march 6'] = 130
# t['march 1'] = 20
# t['dec 10'] = 30
# t['march 17'] = 204
# print(t.arr) 
# print(t['march 6'])

# How to Implemement collision
# There are 2 two to handle collision
# In this if there are more than 1 element showing same index then where to save other elements so there are this methods.
# 1. Chaining :- In this you have to save all the element in same index by creating a list which is known as chaining.
# 2. Linear Pobing :- In this method if the index is full then the other element with same index no will go to next index and if the other 
# index is also full or pre-occupied then it will move to next index.
# for Digramatic representation is refer notes
# E.G TO REMOVE COLLISION OR OVER-LAPPING ERROR
# class hashtable:
#     def __init__(self):
#         self.MAX = 10
#         self.arr = [[] for i in range(self.MAX)]

#     def get_hash(self,key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.MAX

#     def __getitem__(self,key):
#         h = self.get_hash(key)
#         return self.arr[h]

# # QUESTION :- IF U WANT TO UPDATE ANY VALUE AT SAME DATE THEN FOLLOW THIS SYNTAX
#     def __setitem__(self,key,val):
#         h = self.get_hash(key)
#         found = False
#         for idx, element in enumerate(self.arr[h]):
#             if len(element)==2 and element[0]==key:
#                 self.arr[h][idx] = (key,val)
#                 found = True
#                 break
#         if not found:
#             self.arr[h].append((key,val))

# t = hashtable()
# t['march 6'] = 130
# t['march 6'] = 78
# t['march 8'] = 30
# t['march 9'] = 30
# t['march 17'] = 204
# print(t.arr) 
# print(t['march 6'])
# NOTE:- HERE IN THIS OUTOUT U GET THE VALUE OF MARCH 6 AS 78 AND NOT 130, SINCE THE VALUE GETS OVERLAPP OR UPDATED.


# this is the eg for running the list in the same index and getting the value for the desired elelment.
class hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))

# To delete something
    def __delitem__(self,key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
t = hashtable()
t['march 6'] = 130
t['march 6'] = 78
t['march 8'] = 30
t['march 9'] = 30
t['march 17'] = 204
print(t.arr)
# print(t['march 17'])
# print(t['march 6'])
del t['march 17']
print(t.arr)
del t['march 6']
print(t.arr)