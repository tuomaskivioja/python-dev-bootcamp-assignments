# create a dictionary to store the complement of each element in nums
complements = {}
# loop through nums
for i in range(len(nums)):
    # check if the complement of the current element exists in the dictionary
    if nums[i] in complements:
        # if it does, return the indices of the two elements that add up to target
        return [complements[nums[i]], i]
    else:
        # if it doesn't, add the complement of the current element to the dictionary
        complements[target - nums[i]] = i