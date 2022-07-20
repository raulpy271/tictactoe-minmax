
from src.game import Game
from src.show import show_game

if __name__ == '__main__':
    g = Game()
    show_game(g)
    for _ in range(9):
        pos = int(input('Digite proximo input: '))
        g.execute_move(pos)
        show_game(g)
        has_winner = g.player_wins()
        if has_winner:
            print(f'Winner: {g.get_winner()}')
            break

