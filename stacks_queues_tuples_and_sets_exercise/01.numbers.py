nums_one = set(int(x) for x in input().split())
nums_two = set(int(y) for y in input().split())
count = int(input())

for index in range(count):
    first_command, second_command, *data = input().split()

    command = first_command + " " + second_command

    if command == "Add First":
        [nums_one.add(int(i)) for i in data]
    elif command == "Add Second":
        [nums_two.add(int(i)) for i in data]
    elif command == "Remove First":
        [nums_one.discard(int(i)) for i in data]
    elif command == "Remove Second":
        [nums_two.discard(int(i)) for i in data]
    elif command == "Check Subset":
        print(nums_one.issubset(nums_two) or nums_two.issubset(nums_one))

print(*sorted(nums_one), sep=", ")
print(*sorted(nums_two), sep=", ")