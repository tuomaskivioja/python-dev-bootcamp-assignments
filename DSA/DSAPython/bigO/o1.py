



def sum_first_two(items):
    ops = 0
    ops += 1
    first = items[0]
    ops += 1
    second = items[1]

    for i in range(100):
        print('hey')

    print("number of ops: ", ops)
    return first + second

nums = [2, 5, 7, 4, 5, 2, 5, 7, 4, 5]
print(sum_first_two(nums))
