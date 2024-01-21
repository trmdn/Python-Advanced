rows = int(input())
matrix = []

for index in range(rows):
    rows_data = [int(element) for element in input().split(", ")]
    for elements in rows_data:
        matrix.append(elements)

print(matrix)