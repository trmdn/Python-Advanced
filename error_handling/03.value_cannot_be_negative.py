class ValueCannotBeNegative(Exception):
    pass

for i in range(5):
    numbers = int(input())

    if numbers < 0:
        raise ValueCannotBeNegative