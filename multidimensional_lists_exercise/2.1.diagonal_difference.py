number = int(input())
matrix = [[int(x) for x in input().split()] for i in range(number)]
primary_diagonal = [matrix[r][r] for r in range(number)]
secondary_diagonal = [matrix[r][number - r - 1] for r in range(number)]

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)

print(abs(primary_sum - secondary_sum))