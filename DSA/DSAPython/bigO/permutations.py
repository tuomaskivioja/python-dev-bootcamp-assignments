

def permutations(lst):
    """
    This function generates all possible permutations of a list.

    Parameters:
    lst (list): The list to generate permutations for.

    Returns:
    list: A list of all possible permutations of the input list.
    """
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        result = []
        for i in range(len(lst)): # [1, 2, 3]
            remaining_list = lst[:i] + lst[i+1:] # [2, 3]
            print(remaining_list)
            for permutation in permutations(remaining_list):
                result.append([lst[i]] + permutation)
        return result


print(permutations([1,2,3]))


# For example, consider the list [1, 2, 3]. The following are some permutations of this list:
#
# - [1, 2, 3]
# - [1, 3, 2]
# - [2, 1, 3]
# - [2, 3, 1]
# - [3, 1, 2]
# - [3, 2, 1]