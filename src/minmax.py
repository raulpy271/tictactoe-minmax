
from random import choice, randint

from src.game import Game, Player, flip_player
from src.tree import construct_tree_from_game, evaluate_tree

            
class GameWithMinMax:
    def __init__(self, first_player_is_ia=True):
        self.game = Game()
        self.tree = None
        self.ia_player: Player = Game.FIRST_PLAYER
        if not first_player_is_ia:
            self.ia_player: Player = Game.OPONENT_PLAYER

    def get_best_children_for_ia(self):
        draw_children = []
        best_children = []
        for i in range(len(self.tree.children)):
            child = self.tree.children[i]
            weight = child.value['weight']
            if weight == 1:
                best_children.append(i)
            elif weight == 0:
                draw_children.append(i)
            else:
                continue
        if best_children:
            return choice(best_children)
        elif draw_children:
            return choice(draw_children)
        else:
            print('all bad moves')
            return randint(0, len(self.tree.children) - 1)

    def execute_ia_move(self):
        if self.game.current_player == self.ia_player:
            next_children = self.get_best_children_for_ia()
            self._execute_move_from_tree(next_children)
        else:
            raise Exception("It's not time of ia move, execute the human move first")

    def execute_human_move(self, human_move: int):
        human_player = flip_player(self.ia_player)
        if self.game.current_player == human_player:
            if self.game.can_move(human_move):
                self.game.execute_move(human_move)
                next_children = None
                for i in range(len(self.tree.children)):
                    child = self.tree.children[i]
                    if self.game == child.value['game']:
                        next_children = i
                        break
                if next_children != None:
                    self._execute_move_from_tree(next_children)
                else: raise Exception('Move dont found in tree')
            else: raise Exception('Invalid move')
        else: raise Exception("It's not time of human move, execute the ia move first")

    def construct_tree(self, tree=None):
        if tree:
            self.tree = tree
        else:
            print('Constructing decision tree')
            self.tree = construct_tree_from_game(self.game)
            print('Evaluating the decision tree')
            evaluate_tree(self.tree, self.ia_player, Game.FIRST_PLAYER)

    def _execute_move_from_tree(self, tree_children: int):
        self.tree = self.tree.children[tree_children]
        self.game = self.tree.value['game']
