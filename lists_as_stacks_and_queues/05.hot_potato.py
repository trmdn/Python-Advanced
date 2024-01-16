from collections import deque

names = deque(input().split())
round = int(input())

while len(names) > 1:
    names.rotate(-round)
    removed_kids = names.popleft()
    print(f"Removed {removed_kids}")

print(f"Last is {names.popleft()}")