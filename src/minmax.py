
from random import choice, randint

from src.game import Game
from src.tree import construct_tree_from_game, evaluate_tree

            
class GameWithMinMax:
    def __init__(self):
        self.game = Game()
        self.tree = None

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
        if self.game.current_player == Game.FIRST_PLAYER:
            next_children = self.get_best_children_for_ia()
            self._execute_move_from_tree(next_children)
        else:
            raise Exception("It's not time of ia move, execute the human move first")

    def execute_human_move(self, human_move: int):
        if self.game.current_player == Game.OPONENT_PLAYER:
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
            evaluate_tree(self.tree)

    def _execute_move_from_tree(self, tree_children: int):
        self.tree = self.tree.children[tree_children]
        self.game = self.tree.value['game']
