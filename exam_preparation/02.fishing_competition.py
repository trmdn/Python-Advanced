def get_next_position(position, direction_mapper, direction, matrix):
    current_row_index, current_col_index = position
    row_movement, col_movement = direction_mapper[direction]
    desired_row_movement = current_row_index + row_movement
    desired_col_movement = current_col_index + col_movement

    desired_row_movement = (desired_row_movement + len(matrix)) % len(matrix)
    desired_col_movement = (desired_col_movement + len(matrix)) % len(matrix)

    return desired_row_movement, desired_col_movement


number = int(input())

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []
position = None

for row_index in range(number):
    data = list(input())

    if "S" in data:
        current_col = data.index("S")
        position = [row_index, current_col]
    matrix.append(data)


command = input()
collected_fish = 0

while command != "collect the nets":
    current_row_index, current_col_index = position
    next_row_index, next_col_index = get_next_position(position, direction_mapper, command, matrix)

    symbol = matrix[next_row_index][next_col_index]
    matrix[next_row_index][next_col_index] = "S"
    matrix[current_row_index][current_col_index] = "-"
    position = [next_row_index, next_col_index]

    if symbol.isdigit():
        collected_fish += int(symbol)
    elif symbol == "W":
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{position[0]},{position[1]}]")
        exit()
    
    command = input()


if collected_fish >= 20:
    print(f"Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {20 - collected_fish} tons of fish more.")

if collected_fish > 0:
    print(f"Amount of fish caught: {collected_fish} tons.")

for row in matrix:
    print(f"{''.join(row)}")