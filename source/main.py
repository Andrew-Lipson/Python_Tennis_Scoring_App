import Scoreboard

def player_names():
    player1['Name'] = input("Player 1's name: ")
    player2['Name'] = input("Player 2's name: ")


def start_match():
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


def user_input():
    while True:
        try:
            val = int(input("\nWho won the point:\n1. " + player1['Name'] + "\n2. " + player2['Name'] + "\n"))
            if val == 1 or val == 2:
                return val
            print("\nPlease enter either '1' or '2'. ")
        except ValueError:
            print("\nPlease enter either '1' or '2'. ")


player1 = {'Name': "", 'score': []}
player2 = {'Name': "", 'score': []}

number_of_sets = start_match()
set_scoreboard = Scoreboard.scoreboard_main(player1, player2)
game_score = [str(15), str(30)]
Scoreboard.scoreboard_print(set_scoreboard, game_score)
game_score = [str(30), str(30)]
Scoreboard.scoreboard_print(set_scoreboard, game_score)
game_score = [str(40), str(30)]
Scoreboard.scoreboard_print(set_scoreboard, game_score)
