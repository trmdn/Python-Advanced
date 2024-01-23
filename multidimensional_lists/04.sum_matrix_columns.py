rows, cols = [int(element) for element in input().split(", ")]
matrix = []

for index in range(rows):
    row_elements = [int(x) for x in input().split()]
    matrix.append(row_elements)

for column_index in range(cols):
    col_total = 0
    for row_index in range(rows):
        col_total += matrix[row_index][column_index]
    print(col_total)