from collections import deque
from datetime import datetime, timedelta

robots = {}

for r in input().split(";"):
    name, time_needed = r.split("-")
    robots[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()
product_times = {}

while True:
    product = input()

    if product == "End":
        break

    products.append((product, factory_time))
    product_times[product] = factory_time


while products:
    factory_time += timedelta(0, 1)
    product, product_times = products.popleft()

    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1
        elif product_times >= factory_time:
            break
        else:
            free_robots.append([name, value])
    
    if not free_robots:
        products.append(product, product_times)
        continue

robots_name, data = free_robots[0]
robots[robots_name][1] = data[0] + (factory_time - product_times).seconds

print(f"{robots_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")