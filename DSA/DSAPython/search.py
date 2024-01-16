def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target element is found
    return -1  # Return -1 if the target element is not in the list


# Example usage:
my_list = [3, 6, 8, 2, 9, 4, 1]
target_element = 9
result1 = linear_search(my_list, target_element)
print(result1)


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Return the index where the target element is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Return -1 if the target element is not in the list


# Example usage (assuming the list is sorted):
my_sorted_list = [1, 2, 3, 4, 6, 8, 9]
target_element = 6
result2 = binary_search(my_sorted_list, target_element)
print(result2)
