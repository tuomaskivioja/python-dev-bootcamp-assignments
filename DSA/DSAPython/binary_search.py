
def binary_search(arr, x):
    """
    This function performs binary search on a sorted array.
    arr: The sorted array to search.
    x: The value to search for.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1