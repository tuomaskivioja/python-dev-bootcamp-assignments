


def optimized_bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        # Flag to check if any swap happens
        swapped = False

        # Perform the bubble sort by comparing adjacent elements
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap if elements are in the wrong order
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        # If no two elements were swapped, then the list is already sorted
        if not swapped:
            break

    return lst