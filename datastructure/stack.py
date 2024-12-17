# Using list as Stack
# s = []
# s.append('https://timesofindia.indiatimes.com/')
# s.append('https://timesofindia.indiatimes.com/world')
# s.append('https://timesofindia.indiatimes.com/world/china')
# s.append('https://timesofindia.indiatimes.com/world/uk')
# # print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop()) Here the error occurs u can not remove the element from empty list.

# If u don't want to remove the element from the list but only get the element then,
# - index to get the last one.
# print(s[-1])
# print(s)
# And ur list is also not changed.
# Issue with list is only that it is a dynamic array & if it doesn't have space then it relocates and copies the previous data too.
# If u have million elements then u have to copy million elements which might be costly.
# So for that reason using list as Stack is not recommended in python.
# The recommended approach is collections.deque

from collections import deque
# stack = deque()
# print(dir(stack))
# stack.append('https://timesofindia.indiatimes.com/')
# stack.append('https://timesofindia.indiatimes.com/world')
# stack.append('https://timesofindia.indiatimes.com/world/china')
# stack.append('https://timesofindia.indiatimes.com/world/uk')
# print(stack)
# print(stack.pop())
# # In this it removes the last element
# print(stack)

class Stack:
    def  __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
s = Stack()
# print(s.push(5))
# print(s.peek())
# print(s.pop())
# # pop will display 5 but it will remove 5 aswell.
# # print(s.pop())
# print(s.is_empty())

s.push(67)
s.push(7)
s.push(4357)
print(s.size())