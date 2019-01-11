import random

class TicTacToeGame:

    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.history = []

    def print_board(self):
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print()

    def get_possible_actions(self):
        possible_actions = []
        for i in range(0, len(self.board)):
            if self.board[i] == 0:
                possible_actions.append(i)
        return possible_actions

    def is_winner(self, p):
        return ((self.board[0] == p and self.board[1] == p and self.board[2] == p) or
            (self.board[3] == p and self.board[4] == p and self.board[5] == p) or
            (self.board[6] == p and self.board[7] == p and self.board[8] == p) or
            (self.board[0] == p and self.board[3] == p and self.board[6] == p) or
            (self.board[1] == p and self.board[4] == p and self.board[7] == p) or
            (self.board[2] == p and self.board[5] == p and self.board[8] == p) or
            (self.board[0] == p and self.board[4] == p and self.board[8] == p) or
            (self.board[2] == p and self.board[4] == p and self.board[6] == p))

    def is_finished(self, p1, p2):
        return (self.is_winner(p1.id) == True or self.is_winner(p2.id) == True or len(self.get_possible_actions()) == 0)

    def split_history(self, p1, p2, winner_id):
        p2.history = [(s, sp, 0) for s, sp in zip(self.history[0::2], self.history[2::2])]
        p1.history = [(s, sp, 0) for s, sp in zip(self.history[1::2], self.history[3::2])]

        if winner_id == p1.id:
            s, sp, r = p1.history[len(p1.history) - 1]
            p1.history.append((sp, self.board, 1))
            s, sp, r = p2.history[len(p2.history) - 1]
            p2.history[len(p2.history) - 1] = (s, sp, -1)
        elif winner_id == p2.id:
            s, sp, r = p2.history[len(p2.history) - 1]
            p2.history.append((sp, self.board, 1))
            s, sp, r = p1.history[len(p1.history) - 1]
            p1.history[len(p1.history) - 1] = (s, sp, -1)

    def process_game(self, p1, p2):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        players = [p1, p2]
        random.shuffle(players)
        starter_id = players[0].id
        self.history = [list(self.board)]
        i = 0

        while self.is_finished(p1, p2) is False:
            pos = players[i % 2].do_action(self.board, self.get_possible_actions())
            self.board[pos] = players[i % 2].id
            self.history.append(list(self.board))
            i = i + 1

        if self.is_winner(p1.id) is True:
            winner_id = p1.id
        elif self.is_winner(p2.id) is True:
            winner_id = p2.id
        else:
            winner_id = 0

        self.split_history(players[0], players[1], winner_id)

        return winner_id