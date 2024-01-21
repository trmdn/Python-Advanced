rows = int(input())
matrix = []

for i in range(rows):
    row_data = [int(element) for element in input().split(", ") if int(element) % 2 == 0]
    matrix.append(row_data)

print(matrix)