def bubble_sort(elements):
    size = len(elements)
    

    for k in range(size - 1):
        swapped = False
        # If the list is already sorted then what we can do, so it will save time & not stop iterating. 
        for i in range(size - 1):
            if elements[i] > elements[i+1]:
                tmp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = tmp
                swapped = True
        if not swapped:
            break
    # NOTE :- when u write this code from [for loop & ends at tmp] & run u get 88 at last position at it's correct position.
    # If you write this code of 5 lines again you will get 67 at 2nd last position which is it's correct position.
    # So we will add range in this loop so we can get iteration directly without writing code again & again.


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    # elements  = [1,2,4]
    elements = ["Mona","Dhawal","Aamir","Tina","Chang"]
    # In this strings are sorted by alphabetical order.

    bubble_sort(elements)
    print(elements)