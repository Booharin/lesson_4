from math import factorial


def fact(nums):
    for i in nums:
        yield factorial(i)


f = fact([1, 2, 3, 4, 5])

print(next(f))
print(next(f))
print(next(f))
