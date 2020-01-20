from itertools import count, cycle
from sys import argv


def getIterators(start_number, my_string):
    for el in count(start_number):
        if el > start_number + 10:
            break
        else:
            print(el)

    f = 0
    for el in cycle(my_string):
        if f > 10:
            break
        else:
            print(el)
            f += 1


number, string = argv
getIterators(number, string)
