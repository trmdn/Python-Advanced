number = int(input())
longest_intersection = set()
for _ in range(number):
    a, b = map(int, input().split("-"))

    first_start, first_end = [int(first) for first in a.split(",")]
    second_start, second_end = [int(second) for second in b.split(",")]
    first_set = set()
    second_set = set()
    for number in range(first_start, first_end + 1):
        second_set.add(number)
    for number in range(second_start, second_end + 1):
        first_set.add(number)
    current_intersection = set(first_set & second_set)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

formatted_intersection = f"{', '.join([f'{i}' for i in longest_intersection])}"
print(f"Longest intersection is [{formatted_intersection}] with length {len(longest_intersection)}")