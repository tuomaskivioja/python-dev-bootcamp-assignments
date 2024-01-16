
# Write a Python function that takes in a list of integers and returns a new list with the elements in reverse order.


example_list = [1,2,4,3,6]
# -> [6,3,4,2,1]


def reverse_list(lst):
    rev = []
    for item in lst:
        rev = [item] + rev
    return rev


print(reverse_list(example_list))