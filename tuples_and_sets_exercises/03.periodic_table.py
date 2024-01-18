table = set()
number = int(input())

for _ in range(number):
    for element in input().split():
        table.add(element)

print(*table, sep="\n")