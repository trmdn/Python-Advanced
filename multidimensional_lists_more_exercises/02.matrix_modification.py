number = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(number)]

command = input().split()

while command[0] != "END":
    command_type, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= row < number and 0 <= col < number):
        print("Invalid coordinates")
    elif command_type == "Add":
        matrix[row][col] += value
    elif command_type == "Subtract":
        matrix[row][col] -= value
    
    command = input().split()

[print(*row) for row in matrix]