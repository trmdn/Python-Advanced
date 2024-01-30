number = int(input())

matrix = []
bunny_pos = []
bunny_path = []

best_dir = None
max_collected_eggs = float('-inf')

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(number):
    matrix.append(input().split())

    if "B" in matrix[row]:
        bunny_pos = [row, matrix[row].index("B")]

for direction, position in directions.items():
    row, col = [
        bunny_pos[0] + position[1],
        bunny_pos[1] + position[0],
    ]

    path = []
    collected_eggs = 0

    while 0 <= row < number and 0 <= col < number:
        if matrix[row][col] == "X":
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])
        
        row += position[0]
        col += position[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = direction
        best_path = path
    
print(best_direction)
print(*best_path, sep='\n')
print(max_collected_eggs)