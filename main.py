import tictactoe
import player

def evaluate(nb_games, trained_player):
    game = tictactoe.TicTacToeGame()
    random_player = player.PlayerAI(2, True)
    win = 0
    loose = 0
    for _ in range(0, 1000):
        winner_id = game.process_game(trained_player, random_player)
        if winner_id == trained_player.id:
            win = win + 1
        elif winner_id == random_player.id:
            loose = loose + 1
    print("After {} games: {} wins, {} looses, {} draws".format(nb_games, win, loose, 1000 - loose - win))

def main():
    game = tictactoe.TicTacToeGame()
    p1 = player.PlayerAI(1)
    p2 = player.PlayerAI(2)
    total_games = 100000
    limit = 0.95 * total_games

    for nb_games in range(0, total_games):

        winner_id = game.process_game(p1, p2)
        p1.train()
        p2.train()

        # Reduce the value of epsilon_greedy every 10 games played
        if nb_games % 10 == 0 and nb_games <= limit:
            p1.epsilon_greedy = (limit - nb_games) / limit
            p2.epsilon_greedy = (limit - nb_games) / limit

        # Evaluate level of p1 every 1000 games played
        if nb_games % 1000 == 0:
            evaluate(nb_games, p1)

if __name__ == "__main__":
    main()