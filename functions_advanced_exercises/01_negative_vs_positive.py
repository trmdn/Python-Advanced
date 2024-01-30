from typing import List

def print_numbers(nums: List[int]) -> None:
    positive_num = sum(num for num in nums if num > 0)
    negative_num = -sum(abs(num) for num in nums if num < 0)

    print(negative_num)
    print(positive_num)

    if positive_num > abs(negative_num):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")

numbers = [int(x) for x in input().split()]
print_numbers(numbers)