clothes = [int(x) for x in input().split()]
capacity = int(input())

racks_count = 1
current_rack_capacity = capacity

while clothes:
    cloth = clothes.pop()

    if current_rack_capacity >= cloth:
        current_rack_capacity -= cloth
    else:
        racks_count += 1
        current_rack_capacity = capacity - cloth

print(racks_count)