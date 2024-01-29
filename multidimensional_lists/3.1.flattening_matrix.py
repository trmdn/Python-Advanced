rows = int(input())
flattening = []

for index in range(rows):
    rows_data = [int(elements) for elements in input().split(", ")]
    flattening.extend(rows_data)

print(flattening)