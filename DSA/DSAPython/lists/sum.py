
# Write a Python function that takes in a list of integers and returns the sum of all the elements in the list.
#
def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

example_list = [1,2,4,3,6]

print(sum_list(example_list))
