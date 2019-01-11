import random

class PlayerAI:

    def __init__(self, id, random=False):
        self.V = {}
        self.history = []
        self.id = id
        self.random = random
        self.learning_rate = 0.1
        self.epsilon_greedy = 1

    def do_random_action(self, possible_actions):
        return random.choice(possible_actions)

    def do_best_action(self, board, possible_actions):
        action_values = {}
        for action in possible_actions:
            next_state = list(board)
            next_state[action] = self.id
            if str(next_state) in self.V:
                action_values[action] = self.V[str(next_state)]
            else:
                action_values[action] = 0
        max_value = -1
        best_action = None
        for action, value in action_values.items():
            if value > max_value:
                max_value = value
                best_action = action
        return best_action

    def do_action(self, board, possible_actions):
        if self.random is True:
            return self.do_random_action(possible_actions)
        elif random.uniform(0, 1) > self.epsilon_greedy:
            return self.do_best_action(board, possible_actions)
        else:
            return self.do_random_action(possible_actions)

    def train(self):
        first = True
        for s, sp, r in reversed(self.history):
            s = str(s)
            sp = str(sp)
            if s not in self.V:
                self.V[s] = 0.0
            if sp not in self.V:
                self.V[sp] = 0.0
            if first is True:
                self.V[sp] = self.V[sp] + self.learning_rate * (r - self.V[sp])
            self.V[s] = self.V[s] + self.learning_rate * (self.V[sp] - self.V[s])
            first = False