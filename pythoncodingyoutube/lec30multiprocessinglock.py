# Why lock is needed in real life?
# In our day to day life there are things that cannot be accessed by two ppl at the same time.
#  for e.g bathroom, there is lock at bathroom door, two ppl cannot share it at same time so it has lock


import time
import multiprocessing

def deposite(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ =="__main__":
    balance = multiprocessing.Value("i" ,200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposite, args=(balance,lock))
    w = multiprocessing.Process(target=withdraw, args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)

