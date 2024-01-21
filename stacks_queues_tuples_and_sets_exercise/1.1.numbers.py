nums_one = set(int(x) for x in input().split())
nums_two = set(int(y) for y in input().split())

count = int(input())

functions = {
    "Add First": lambda x: [nums_one.add(int(i)) for i in input().split()],
    "Add Second": lambda x: [nums_two.add(int(i)) for i in input().split()],
    "Remove First": lambda x: [nums_one.remove(int(i)) for i in input().split()],
    "Remove Second": lambda x: [nums_two.remove(int(i)) for i in input().split()],
    "Check Subset": lambda x: print(nums_one.issubset(nums_two) or nums_two.issubset(nums_one)),
}

for index in range(count):
    first_command, second_command, *data = input().split()

    command = first_command + " " + second_command

    functions[command](data)

print(*sorted(nums_one), sep=", ")
print(*sorted(nums_two), sep=", ")