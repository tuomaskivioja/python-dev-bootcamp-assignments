

def quick_sort(lst):

    if len(lst) <= 1:
        return lst

    else:
        pivot = lst[0]
        less = [x for x in lst[1:] if x <= pivot]
        more = [x for x in lst[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)








# Printing the sorted results for multiple test cases
print("Sorted [8, 4, 3, 7, 6]:", quick_sort([8, 4, 3, 7, 6]))
print("Sorted [1, 2, 3, 4, 5]:", quick_sort([1, 2, 3, 4, 5]))
print("Sorted [4, 2, 2, 3, 1]:", quick_sort([4, 2, 2, 3, 1]))
print("Sorted [5, 5, 5, 5, 5]:", quick_sort([5, 5, 5, 5, 5]))
print("Sorted [9, 1, 0, 3, 2]:", quick_sort([9, 1, 0, 3, 2]))
print("Sorted [11, 14, 13, 12, 15]:", quick_sort([11, 14, 13, 12, 15]))
