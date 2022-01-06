import Scoreboard
import Variable
import Set


def player_names():
    Variable.player1['name'] = input("Player 1's name: ")
    Variable.player2['name'] = input("Player 2's name: ")


def initialise_match():
    player_names()
    while True:
        try:
            val = int(input("\nHow many sets(1,3,5): "))
            if val == 1 or val == 3 or val == 5:
                for x in range(val):
                    Variable.scores.append([0, 0])
                return val
            print("\nPlease enter either '1', '3' or '5'. ")
        except ValueError:
            print("\nPlease enter either '1', '3' or '5'. ")


def start_match():
    Scoreboard.initialise_scoreboard()
    Set.a_set(1-1)


number_of_sets = initialise_match()
start_match()
