from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
filled_capacity = deque([int(y) for y in input().split()])

wasted_liters = 0

while cups_capacity and filled_capacity:
    current_cup = cups_capacity.popleft()
    current_bottle = filled_capacity.pop()

    if current_cup <= current_bottle:
        wasted_liters += current_bottle - current_cup
    else:
        cups_capacity.appendleft(current_cup - current_bottle)

if current_cup:
    print(f"Cups:", *cups_capacity)
else:
    print(f"Bottles:", *filled_capacity)

print(f"Wasted litters of water: {wasted_liters}")