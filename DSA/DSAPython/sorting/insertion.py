

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key
    return lst

# Printing the sorted results for multiple test cases
print("Sorted [8, 4, 3, 7, 6]:", insertion_sort([8, 4, 3, 7, 6]))
print("Sorted [1, 2, 3, 4, 5]:", insertion_sort([1, 2, 3, 4, 5]))
print("Sorted [4, 2, 2, 3, 1]:", insertion_sort([4, 2, 2, 3, 1]))
print("Sorted [5, 5, 5, 5, 5]:", insertion_sort([5, 5, 5, 5, 5]))
print("Sorted [9, 1, 0, 3, 2]:", insertion_sort([9, 1, 0, 3, 2]))
print("Sorted [11, 14, 13, 12, 15]:", insertion_sort([11, 14, 13, 12, 15]))
