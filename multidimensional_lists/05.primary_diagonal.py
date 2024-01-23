rows = int(input())
matrix = []

for index in range(rows):
    matrix.append([int(element) for element in input().split()])

diagonal_sum = 0

for row_index in range(rows):
    diagonal_sum += matrix[row_index][row_index]
print(diagonal_sum)