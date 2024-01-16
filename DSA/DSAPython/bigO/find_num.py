def find_num(input, num):
    for number in input:
        if number == num:
            print("Found!")
            return True
    print("Not found :(")
    return False


lst = [2, 3, 77,6,5,4,5,5,4,3]

find_num(lst, 2)