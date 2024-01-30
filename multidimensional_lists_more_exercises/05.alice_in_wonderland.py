number = int(input())
matrix = []
alice_position = []

tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(number):
    matrix.append(input().split())
    
    if "A" in matrix[row]:
        alice_position = [row, matrix[row].index('A')]
        matrix[row][alice_position[1]] = "*"
    
while tea_bags < 10:
    direction = input()

    row = alice_position[0] + directions[direction][0]
    col = alice_position[1] + directions[direction][1]
    
    if not (0 <= row < number and 0 <= col < number):
        break

    alice_position = [row, col]
    position = matrix[row][col]
    matrix[row][col] = "*"

    if position == "R":
        break

    if position.isdigit():
        tea_bags = int(position)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")

else:
    print("She did it! She went to the party.")

print(*[' '.join(row) for row in matrix], sep='\n')