
from typing import Literal
from random import choice

from src import minmax 

def run_game(first_player : Literal['human', 'ia']):
    first_player_is_ia = first_player == 'ia'
    game = minmax.GameWithMinMax(first_player_is_ia=first_player_is_ia)
    game.construct_tree()
    print(game.game)
    print('Game started')
    current_player_is_ia = first_player_is_ia
    for _ in range(9):
        if current_player_is_ia:
            game.execute_ia_move()
            print('IA move: ')
        else:
            human_move = int(input('Your move: '))
            game.execute_human_move(human_move)
        print(game.game)
        if game.game.player_wins():
            print('Somebody has win')
            break
        elif game.game.is_draw():
            print('The game has draw')
            break
        else:
            current_player_is_ia = not current_player_is_ia

if __name__ == '__main__':
    playing = True
    while playing:
        run_game(choice(['ia', 'human']))
        answer = input('do you want play again? [y/n] ')
        if answer != 'y':
            playing = False
    print('Godbye!')

