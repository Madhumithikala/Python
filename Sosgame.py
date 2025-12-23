board = ["-"] * 9
choices = list(range(1, 10))
turn = 0
winner = "Game Tie"

show(board)

while choices:
    player = "X" if turn % 2 == 0 else "O"

    if choose(player, board, choices):
        winner = f"Winner is Player {player}"
        break

    turn += 1

print(winner)
print("Game Over")