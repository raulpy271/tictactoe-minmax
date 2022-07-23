
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
    playing = True
    while playing:
        minmax_game = minmax.GameWithMinMax()
        minmax_game.construct_tree()
        run_game(minmax_game)
        answer = input('do you want play again? [y/n] ')
        if answer != 'y':
            playing = False
    print('Godbye!')

