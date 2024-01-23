rows = int(input())

matrix = []

for i in range(rows):
    matrix.append(list(input()))

search_element = input()

for row_index in range(rows):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == search_element:
            print(f"({row_index}, {col_index})")
            exit()

print(f"{search_element} does not occur in the matrix")