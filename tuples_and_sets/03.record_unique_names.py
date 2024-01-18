number = int(input())

names = set()

for _ in range(number):
    name = input()
    names.add(name)

for name in names:
    print(name)