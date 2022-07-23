
from src import minmax 

def run_game(game: minmax.GameWithMinMax):
    print(game.game)
    print('Game started')
    for _ in range(9):
        game.execute_ia_move()
        print(game.game)
        if game.game.player_wins():
            print('The IA has win')
            break
        elif game.game.is_draw():
            print('The game has draw')
            break
        else:
            human_move = int(input('Your move: '))
            game.execute_human_move(human_move)
            if game.game.player_wins():
                print('The human has win')
                break
            elif game.game.is_draw():
                print('The game has draw')
                break
            else:
                continue

if __name__ == '__main__':
    pre_loaded_game_tree = minmax.GameWithMinMax()
    pre_loaded_game_tree.construct_tree()
    playing = True
    while playing:
        current_game = pre_loaded_game_tree.copy()
        run_game(current_game)
        answer = input('do you want play again? [y/n] ')
        if answer != 'y':
            playing = False
    print('Godbye!')

