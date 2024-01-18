name_count = input()
name = set()

for _ in range(name_count):
    name.add(input())

print(*name, sep="\n")