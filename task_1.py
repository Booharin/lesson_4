from sys import argv


def calculateIncome():
    _, hours, rate, bounty = argv

    try:
        print(f"Income is: {int(hours) * int(rate) + int(bounty)}")
    except ValueError:
        print("value error")


calculateIncome()
# print(list(map(int, input().split())))
