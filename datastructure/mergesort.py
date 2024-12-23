# def merge_two_sorted_lists(a,b):
#     sorted_list = []
#     len_a = len(a)
#     len_b = len(b)
#     i = j = 0
#     while i < len_a and j < len_b :
#         if a[i] <= b[j]:
#             sorted_list.append(a[i])
#             i += 1
#         else:
#             sorted_list.append(b[j])
#             j += 1
#     while i < len_a:
#         sorted_list.append(a[i])
#         i += 1
#     while i < len_b:
#         sorted_list.append(b[j])
#         j += 1

#     return sorted_list

# if __name__ =="__main__":
    # a = [5,8,12,56,89,100]
    # b = [7,9,45,51]

    # print(merge_two_sorted_lists(a,b))

    # Another E.g


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)  # Recursively sort the left half
#     right = merge_sort(right)  # Recursively sort the right half

#     return merge_two_sorted_lists(left, right)

# def merge_two_sorted_lists(a, b):
#     sorted_list = []
#     len_a = len(a)
#     len_b = len(b)
#     i = j = 0

#     # Merge elements from both lists in sorted order
#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             sorted_list.append(a[i])
#             i += 1
#         else:
#             sorted_list.append(b[j])
#             j += 1

#     # Add the remaining elements from list `a`, if any
#     while i < len_a:
#         sorted_list.append(a[i])
#         i += 1

#     # Add the remaining elements from list `b`, if any
#     while j < len_b:
#         sorted_list.append(b[j])
#         j += 1

#     return sorted_list



# if __name__ == '__main__':
#     arr = [5, 9, 2, 1, 67, 34, 88, 34]
#     print("Original Array:", arr)
#     sorted_arr = merge_sort(arr)
#     print("Sorted Array:", sorted_arr)

# Merge two array

def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_lists(left,right,arr)

def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    while i < len_a:
        arr[k] = a[i]
        i+=1 
        k+=1
    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1
# if __name__ =='__main__':
#     arr = [10,3,15,7,8,23,98,29]
#     merge_sort(arr)
#     print(arr)

if __name__ == '__main__':
    test_cases = [
        [11,9,29,7,2,15,28],
        [3,7,9,11],
        [25,22,21,10],
        [29,15,28],
        [],
        [6]
    ]
    for arr in test_cases:
        merge_sort(arr)
        print(arr)


