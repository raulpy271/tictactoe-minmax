
from src.game import Game

def show_game(game: Game):
    positions = game.positions.copy()
    for i in range(9):
        if positions[i] == None:
            positions[i] = i
    game_str = """ {} | {} | {}
 {} | {} | {}
 {} | {} | {}""".format(*positions)
    print(game_str)