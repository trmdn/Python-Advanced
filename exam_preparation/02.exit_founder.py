def find_exit(player):
    print(f"{player[0]} found the exit and wins the game!")
    exit()

def trap(player):
    print(f"{player[0]} is out of the game! The winner is {player[1]}")
    exit()

def wall(player):
    players[player[0]] = True
    print(f"{player[0]} hits the wall and needs to rest")

MATRIX_SIZE = 6
players = {x: False for x in input().split(", ")}

matrix = [input().split() for x in range(MATRIX_SIZE)]


# direction_mapper = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }


commands = {
    "E": find_exit,
    "T": trap,
    "W": wall,
}

player_one, player_two = list(players.keys())
counter = 0


while True:
    counter += 1
    row, col = [int(x) for x in input()[1:-1].split(", ")]
    if counter % 2 == 0:
        player = (player_two, player_one)
    else:
        player = (player_one, player_two)
    
    if players[player[0]]:
        players[player[0]] = False
        continue

    player_steps_on = matrix[row][col]
    if player_steps_on != ".":
        commands[player_steps_on](player)