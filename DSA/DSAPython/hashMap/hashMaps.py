

def is_unique(string):
    # A hash map to keep track of characters that we have seen.
    char_map = {}
    for char in string:
        if char in char_map:
            # If the character is already in the hash map, it's not unique.
            return False
        char_map[char] = True
    return True

# Testing Exercise 8
print(is_unique("abcdef"))  # Should return True
print(is_unique("abcadef")) # Should return False

def are_anagrams(str1, str2):
    # If the lengths are different, they cannot be anagrams.
    if len(str1) != len(str2):
        return False

    # Create a hash map for counting characters in str1.
    count_map = {}
    for char in str1:
        count_map[char] = count_map.get(char, 0) + 1

    # Subtract the count for each character in str2.
    for char in str2:
        if char not in count_map:
            return False
        count_map[char] -= 1
        if count_map[char] < 0:
            return False

    return True

# Testing Exercise 9
print(are_anagrams("listen", "silent")) # Should return True
print(are_anagrams("hello", "billion")) # Should return False

def group_anagrams(strs):
    result = {}
    for s in strs:
        # Sort the string and use it as a key.
        sorted_str = ''.join(sorted(s))
        if sorted_str not in result:
            result[sorted_str] = [s]
        else:
            result[sorted_str].append(s)
    return list(result.values())

# Testing Exercise 10
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

def count_frequencies(numbers):
    frequency_map = {}
    for num in numbers:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    return frequency_map

# Testing Exercise 11
print(count_frequencies([1, 2, 3, 2, 1, 4, 1]))

def find_first_recurring_char(string):
    char_map = set()
    for char in string:
        if char in char_map:
            return char
        char_map.add(char)
    return None

# Testing Exercise 12
print(find_first_recurring_char("acbbac")) # Should return 'b'
print(find_first_recurring_char("abcdef")) # Should return None

def has_pair_with_sum(numbers, target_sum):
    complements = set()
    for num in numbers:
        if target_sum - num in complements:
            return True
        complements.add(num)
    return False

# Testing Exercise 13
print(has_pair_with_sum([1, 4, 45, 6, 10, -8], 16)) # Should return True
print(has_pair_with_sum([1, 2, 3, 9], 8))           # Should return False