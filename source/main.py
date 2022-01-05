import Scoreboard
import Game
import Variable


def player_names():
    Variable.player1['Name'] = input("Player 1's name: ")
    Variable.player2['Name'] = input("Player 2's name: ")

def initialise_match():
    player_names()
    while True:
        try:
            val = int(input("\nHow many sets(1,3,5): "))
            if val == 1 or val == 3 or val == 5:
                Variable.player1['score'].append(0)
                Variable.player2['score'].append(0)
                return val
            print("\nPlease enter either '1', '3' or '5'. ")
        except ValueError:
            print("\nPlease enter either '1', '3' or '5'. ")


def start_match():
    Scoreboard.initialise_scoreboard()
    Scoreboard.set_scoreboard()
    Game.a_game()


number_of_sets = initialise_match()
start_match()
