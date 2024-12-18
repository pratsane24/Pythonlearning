# Issue:- 1. What is HTTP server down? Loss of messages
# 2. Managing multiple consumers becomes problematic
# What if u have a memory buffer like, that ppl pushes values/prices one after other and ppl on other sides receives this prices
# If there are two different guys of different sites which are receiving the data, 1st guys takes the 1st data and moves to 2nd
# and the same sequence follows by the 2nd guys.
# The data structure we have used here is called Queue. & queue allows you to establish loose coupling.
# Tomorrow let say money.com bonds to use this prices & new York Stock Exchange doesn't have to make any change actually,
# they can just keep on pushing the prices on the same memory buffer and monecy cintrol can just consume it.
# do it flexible infrastructure with minmum amount of issue this pbm is also called Producer consumer problem.
# Here 1 entity is producing the information while the other entoty is consuming the information produced by producer.
# Here FIRST IN FIRST OUT :- FIFO data structure.

# wmt_stock_price_queue = []
# wmt_stock_price_queue.insert(0,131.10)
# wmt_stock_price_queue.insert(0,132.12)
# wmt_stock_price_queue.insert(0,135)
# print(wmt_stock_price_queue)
# print(wmt_stock_price_queue.pop())
# print(wmt_stock_price_queue.pop())
# print(wmt_stock_price_queue.pop())
# print(wmt_stock_price_queue.pop()) NOTE :- Here the output comes as or error occurs as list is empty.
# This are the errors occur with list or dynamic array.

# from collections import deque
# q = deque()
# q.appendleft(5)
# q.appendleft(9)
# q.appendleft(27)
# print(q)
# print(q.pop())
# print(q.pop())
# print(q.pop())
# print(q.pop()) NOTE:- Here error occurs as empty deque

from collections import deque

class Queue:

    def  __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        # enqueue is placing the element in queue e.g u r standing in line to buy a ticket.
        self.buffer.appendleft(val)

    def dequeue(self):
        # dequeue means u brought ur tickets and ur out of queue.
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
    
pq = Queue()

pq.enqueue({
    'Company' : 'WalMart',
    'timpestamp' : '15 April, 11.01 Am',
    'price' : 131.10
})

pq.enqueue({
    'Company' : 'WalMart',
    'timpestamp' : '15 April, 11.02 Am',
    'price' : 132.20
})

pq.enqueue({
    'Company' : 'WalMart',
    'timpestamp' : '15 April, 11.03 Am',
    'price' : 135
})
        
# print(pq.buffer)
# print(pq.dequeue())
# print(pq.dequeue())
# print(pq.dequeue())
print(pq.size())