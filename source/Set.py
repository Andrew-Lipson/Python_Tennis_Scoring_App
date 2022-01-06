import Scoreboard
import Game
import Variable


def a_set(set_number):
    while True:
        Scoreboard.set_scoreboard()
        player_number = Game.a_game()
        Variable.scores[set_number][player_number] += 1
        if won_the_set(set_number, player_number):
            return player_number
        if sum(Variable.scores[set_number]) == 12:
            print("tiebreaker")


def won_the_set(set_number, player_number):
    game_winner_score = Variable.scores[set_number][player_number]
    other_score = Variable.scores[set_number][(player_number+1) % 2]
    if game_winner_score == 7:
        return True
    if game_winner_score == 6 and other_score < 5:
        return True
    return False
