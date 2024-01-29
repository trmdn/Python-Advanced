rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for i in range(rows)]

max_sum = float('-inf')
biggest_matrix = []

for sub_row in range(rows - 2):
    for sub_col in range(cols - 2):
        first_row = matrix[sub_row][sub_col:sub_col+3]
        second_row = matrix[sub_row + 1][sub_col:sub_col+3]
        third_row = matrix[sub_row + 2][sub_col:sub_col+3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > max_sum:
            max_sum = current_sum
            biggest_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*row) for row in biggest_matrix]