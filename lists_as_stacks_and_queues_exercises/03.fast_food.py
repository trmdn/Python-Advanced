from collections import deque

quantity_of_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    order = orders.popleft()

    if quantity_of_food >= order:
        quantity_of_food -= order
    else:
        print("Orders left:", order, *orders)
        break
else:
    print("Orders complete")