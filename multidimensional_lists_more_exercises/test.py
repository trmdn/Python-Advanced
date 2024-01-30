number = int(input())

matrix = []
bunny_pos = []
best_direction = None

for row in range(number):
    matrix.append(input().split())
    if "B" in matrix[row]:
        bunny_pos = [row, matrix[row].index("B")]

def explore(row, col, path, eggs):
    global max_collected_eggs

    # check if the current position is out of bounds or contains an obstacle
    if not (0 <= row < number and 0 <= col < number) or matrix[row][col] == "X":
        return eggs

    # check if the current path contains more eggs than the best path found so far
    if eggs > max_collected_eggs:
        max_collected_eggs = eggs
        best_path = path

    # explore the four possible directions
    for direction, position in directions.items():
        new_row, new_col = row + position[0], col + position[1]
        new_path = path + [(row, col)]
        eggs += int(matrix[row][col])
        eggs = explore(new_row, new_col, new_path, eggs)

    return eggs

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

max_collected_eggs = float('-inf')
best_path = []

explore(bunny_pos[0], bunny_pos[1], [(bunny_pos[0], bunny_pos[1])], 0)

print(best_direction)
print(*best_path, sep='\n')
print(max_collected_eggs)