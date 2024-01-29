number = int(input())
matrix = [[int(x) for x in input().split()] for i in range(number)]
coordinates = ((int(x) for x in z.split(",")) for z in input().split())

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    bomb_value = matrix[row][col]

    for x in range(-1, 2):
        for y in range(-1, 2):
            r, c = row + x, col + y

            if 0 <= r < number and 0 <= c < number:
                matrix[r][c] -= bomb_value if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(number) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]