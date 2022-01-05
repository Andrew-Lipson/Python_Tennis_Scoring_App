import Scoreboard
import Game
import Variable


def a_set(set_number):
    while True:
        Scoreboard.set_scoreboard()
        player_number = Game.a_game()
        Variable.scores[set_number-1][player_number] += 1
        if won_the_set(set_number):
            return player_number


def won_the_set(set_number):
    game_winner_score = Variable.scores[set_number - 1][0]
    other_score = Variable.scores[set_number - 1][1]
    if game_winner_score == 7:
        return True
    if game_winner_score == 6 and other_score < 5:
        return True
    return False
