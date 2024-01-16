import time
import random

# Create a list of 1000 numbers
list_of_1000000 = [random.randint(1, 1000000) for _ in range(1000000)]

# Create a list of 100000 numbers
list_of_100000 = [random.randint(1, 100000) for _ in range(100000)]

# def find_duplicates(numbers):
#     unique_numbers = set()
#     duplicates = []
#     ops = 0
#     for number in numbers:
#         ops += 1
#         print(number)
#         if number in unique_numbers:
#             duplicates.append(number)
#             ops += 1
#         else:
#             unique_numbers.add(number)
#             ops += 1
#     print("Operations:", ops)
#     return duplicates




def find_duplicates(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.append(numbers[i])
    return duplicates



numbers = [1, 2, 3, 4, 2, 5, 1]







# start_time = time.time()  # Capture start time
duplicates = find_duplicates(list_of_1000000)
# end_time = time.time()  # Capture end time

# print("Duplicates:", duplicates)
