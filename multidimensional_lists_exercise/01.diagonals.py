number = int(input())
matrix = [[int(x) for x in input().split(", ")] for i in range(number)]
primary_diagonal = [matrix[r][r] for r in range(number)]
secondary_diagonal = [matrix[r][number - r - 1] for r in range(number)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")