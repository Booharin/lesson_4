def getCorrectList():
    my_list = [i for i in [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]]
    print(my_list)
    correct_list = [item for i, item in enumerate(my_list) if i > 0 and item > my_list[i - 1]]
    print(correct_list)


getCorrectList()