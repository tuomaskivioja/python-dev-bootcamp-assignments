

# Write a program that counts the frequency of each character in a string using a hash map.
# For example, given the string "hello world", the program should output something like:
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}.

def count_chars(s):

    char_counts = {}

    for c in s:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1

    return char_counts


print(count_chars("hellooooooo"))