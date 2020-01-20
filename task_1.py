from sys import argv


def calculateIncome():
    hours, rate, bounty = argv

    try:
        print(f"Income is: {hours * rate + bounty}")
    except ValueError:
        print("value error")


calculateIncome()
