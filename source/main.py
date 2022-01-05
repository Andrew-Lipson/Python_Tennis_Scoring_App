import Scoreboard
import Game


def player_names():
    player1['Name'] = input("Player 1's name: ")
    player2['Name'] = input("Player 2's name: ")
    Game.player1_name = player1['Name']
    Game.player2_name = player2['Name']


def initialise_match():
    player_names()
    while True:
        try:
            val = int(input("\nHow many sets(1,3,5): "))
            if val == 1 or val == 3 or val == 5:
                player1['score'].append(0)
                player2['score'].append(0)
                return val
            print("\nPlease enter either '1', '3' or '5'. ")
        except ValueError:
            print("\nPlease enter either '1', '3' or '5'. ")


def start_match():
    set_scoreboard = Scoreboard.scoreboard_main(player1, player2)
    Game.a_game(set_scoreboard)


player1 = {'Name': "", 'score': []}
player2 = {'Name': "", 'score': []}

number_of_sets = initialise_match()
start_match()
