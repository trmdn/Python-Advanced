number = int(input())
matrix = [[int(x) for x in input().split()] for i in range(number)]

primary_sum, secondary_sum = 0, 0

for i in range(number):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][number - i - 1]

print(abs(primary_sum - secondary_sum))