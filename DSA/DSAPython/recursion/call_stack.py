

def add_two_numbers(x, y):
    return x + y

def multiply_and_add(x, y, z):
    return add_two_numbers(x, y) * z

result = multiply_and_add(2, 3, 4)  # This will first add 2 and 3, then multiply the sum by 4.
print(result)  # Output: 20
