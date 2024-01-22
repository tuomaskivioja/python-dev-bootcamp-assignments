

def merge_sort(lst):

    if len(lst) == 1:
        return lst

    if len(lst) == 2:
        if lst[1] < lst[0]:
            lst[1], lst[0] = lst[0], lst[1]
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    print(mid)
    print(left_half)
    print(right_half)

    # return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += right[j:]
    merged += left[i:]

    return merged

example_array = [3, 1, 4, 1]

# Sorting the array using merge sort
sorted_array = merge_sort(example_array)
print(sorted_array)