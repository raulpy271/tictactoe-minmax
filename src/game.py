
from typing import Literal, Optional

Player = Literal['X', 'O']

def flip_player(p: Player) -> Player:
    if p == Game.FIRST_PLAYER:
        next_player = Game.OPONENT_PLAYER
    else:
        next_player = Game.FIRST_PLAYER
    return next_player


class Game:

    FIRST_PLAYER: Player = 'X'
    OPONENT_PLAYER: Player  = 'O'

    def __init__(self):
        self.positions: list[Optional[Player]] = [None] * 9
        self.current_player: Player = Game.FIRST_PLAYER

    def execute_move(self, pos: int):
        if self.player_wins():
            raise Exception('Já existe vencedor!')
        elif self.can_move(pos):
            self.positions[pos] = self.current_player
            self._change_player()
        else:
            raise Exception('Não possível mover para esta posição, ela já foi usada!')

    def can_move(self, pos: int) -> bool:
        return self.positions[pos] == None

    def player_wins(self) -> bool:
        same_player_in = lambda l: (l[0] == l[1] == l[2]) and (l[0] != None)
        lines = [
            [self.positions[0], self.positions[1], self.positions[2]], # row 0
            [self.positions[3], self.positions[4], self.positions[5]], # row 1
            [self.positions[6], self.positions[7], self.positions[8]], # row 2
            [self.positions[0], self.positions[3], self.positions[6]], # column 0
            [self.positions[1], self.positions[4], self.positions[7]], # column 1
            [self.positions[2], self.positions[5], self.positions[8]], # column 2
            [self.positions[0], self.positions[4], self.positions[8]], # diagonal 0
            [self.positions[2], self.positions[4], self.positions[6]], # diagonal 1
        ]
        same_player_in_any_line_or_column = any(map(same_player_in, lines))
        return same_player_in_any_line_or_column

    def get_winner(self) -> Player:
        if self.player_wins():
            return flip_player(self.current_player)
        else:
            raise Exception('Não há vencendores')

    def is_draw(self) -> bool:
        return not self.possible_moves() and not self.player_wins()

    def possible_moves(self) -> list[int]:
        moves = []
        for i in range(9):
            if self.positions[i] == None:
                moves.append(i)
        return moves

    def copy(self):
        game = Game()
        game.positions = self.positions.copy()
        game.current_player = self.current_player
        return game

    def _change_player(self):
        next_player = flip_player(self.current_player)
        self.current_player = next_player

    def __eq__(self, obj):
        if isinstance(obj, Game):
            return self.positions == obj.positions and self.current_player == obj.current_player
        else:
            return False

    def __str__(self):
        positions = self.positions.copy()
        for i in range(9):
            if positions[i] == None:
                positions[i] = i
            elif positions[i] == Game.FIRST_PLAYER:
                positions[i] = "\033[91mX\033[00m"
            else:
                positions[i] = "\033[92mO\033[00m"
        game_str = """ {} | {} | {}
 {} | {} | {}
 {} | {} | {}""".format(*positions)
        return game_str
