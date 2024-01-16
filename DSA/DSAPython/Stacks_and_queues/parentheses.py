from stack import Stack

def is_valid_parentheses(s):
    stack = Stack()

    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map:
            latest_opening_bracket = stack.pop()
            if bracket_map[char] != latest_opening_bracket:
                return False
        else:
            stack.push(char)

    return len(stack.items) == 0



# Testing the function
print(is_valid_parentheses("["))  # True
print(is_valid_parentheses("([)]"))  # False