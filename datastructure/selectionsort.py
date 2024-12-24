# NOTE:- THIS IS TO FIND MIN NO FROM THE LIST
# def find_min_element(arr):
#     min = 1000000
#     for i in range(len(arr)):
#         if arr[i] < min:
#             min = arr[i]
#     return min



def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        if i!= min_index:       
            arr[i], arr[min_index] = arr[min_index],arr[i]        



if __name__ == "__main__":
    # elements = [78,12,15,8,61,53,23,27]
    # selection_sort(elements)
    # # print(find_min_element(elements))
    # print(elements)

    tests = [
        [89,78,61,53,23,21,17,12,9,7,6,2,1],
        [ ],
        [1,5,8,9],
        [235,3,1,56,32,12,9,34,1300],
        [5]
    ]
    for elements in tests:
        selection_sort(elements)
        print(elements)