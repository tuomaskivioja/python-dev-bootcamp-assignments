
def rotate(lst, k):
    n = len(lst)
    k = k % n
    return lst[-k:] + lst[:-k]

print(rotate([1, 2, 3, 4, 5], 5))
