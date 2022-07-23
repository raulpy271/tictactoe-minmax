
from src.game import Game, Player, flip_player


class Node:
    def __init__(self, value):
        self.value = value
        self.children: list[Node] = []

def construct_tree_from_game(game: Game):
    node = Node({'weight': None, 'game': game})
    if not game.player_wins():
        positions = game.possible_moves()
        for position in positions:
            new_game = game.copy()
            new_game.execute_move(position)
            children_node = construct_tree_from_game(new_game)
            node.children.append(children_node)
    return node

def evaluate_terminal(node: Node):
    game: Game = node.value['game']
    if game.is_draw():
        value = 0
    else:
        winner = game.get_winner()
        if winner == Game.FIRST_PLAYER:
            value = 1
        else:
            value = -1
    node.value['weight'] = value

def evaluate_tree(node: Node, current_player: Player = Game.FIRST_PLAYER):
    if not node.children:
        evaluate_terminal(node)
    else:
        has_found_one_weight = False
        has_found_minus_one_weight = False
        has_found_zero_weight = False
        for one_child in node.children:
            evaluate_tree(one_child, flip_player(current_player))
            if one_child.value['weight'] == 1:
                has_found_one_weight = True
            elif one_child.value['weight'] == -1:
                has_found_minus_one_weight = True
            else:
                has_found_zero_weight = True
        if current_player == Game.FIRST_PLAYER:
            if has_found_one_weight:
                value = 1
            elif has_found_zero_weight:
                value = 0
            else:
                value = -1
        else:
            if has_found_minus_one_weight:
                value = -1
            elif has_found_zero_weight:
                value = 0
            else:
                value = 1
        node.value['weight'] = value
