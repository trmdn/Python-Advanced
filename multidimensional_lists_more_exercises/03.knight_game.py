number = int(input())
matrix = [list(input()) for i in range(number)]

positions = {
    (-2, -1), # up 2 and left 1
    (-2, 1), # up 2 and right 1
    (-1, -2), # up 1 and left 2
    (-1, 2), # up 1 and right 2 
    (2, 1), # down 2 and right 1
    (2, -1), # down 2 and left 1 
    (1, 2), # down 1 and right 2
    (1, -2), # down and left 2
}

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(number):
        for col in range(number):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < number and 0 <= pos_col < number:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1
                
                if attacks > max_attacks:
                    knight_with_most_attacks_pos = [row, col]
                    max_attacks = attacks
    
    if knight_with_most_attacks_pos:
        r, c = knight_with_most_attacks_pos
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)