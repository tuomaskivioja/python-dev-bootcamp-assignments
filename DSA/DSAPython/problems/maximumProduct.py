

def max_product(lst):
    if len(lst) < 2:
        return 0

    max_product = lst[0] * lst[1]
    for i in range(1, len(lst) -1):
        max_product = max(max_product, lst[i] * lst[i + 1])

    return max_product

input_list = [3, 6, -2, -5, 7, 3]
print(max_product(input_list))
