# same e.g as lec 27
# import multiprocessing

# result = []

# def calc_square(numbers):
#     global result
#     for n in numbers:
#         result.append(n*n)
#     print("inside process " + str(result))

# if __name__ == "__main__":
#     numbers = [2,3,5]
#     p=multiprocessing.Process(target=calc_square, args=(numbers,))

#     p.start()
#     p.join

#     print("outside process "+ str(result))

# Shared memory through array
# append is not part of share memory method so append is not gona work, so we need to use simple index.

# import multiprocessing

# def calc_square(numbers, result, v):
#     v.value = 5.67
#     for idx,n in enumerate(numbers):
#         result[idx] =n*n


# if __name__ == "__main__":
#     numbers = [2,3,5]
#     result = multiprocessing.Array("i",3)
#     #For value, we have used used v
#     v = multiprocessing.Value("d", 0.0)
#     p = multiprocessing.Process(target=calc_square, args=(numbers, result, v))

#     p.start()
#     p.join()

#     print(result[:])
#     print(v.value)


# Data sharing using Queue
# Queue is basically shared memory

import multiprocessing

def cal_square(numbers ,q):
    for n in numbers:
        q.put(n*n)
     
if __name__ == "__main__":
    numbers = [2,3,5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=cal_square, args=(numbers, q))
    
    
    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())

