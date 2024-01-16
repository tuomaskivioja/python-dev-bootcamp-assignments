import random



def search(numbers, target):
    for i in range(numbers):
        if i == target:
            print("Found!!!")
            return 0

#


book_pages = 1000
target = 300
search(book_pages, target)